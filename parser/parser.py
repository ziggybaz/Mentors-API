from copy import deepcopy


class ParseRow:
    def __init__(self, data) -> None:
        self.data = data

    def get_flat_data(self):
        return {
            "submission_id": self.data["_id"],
            "mentor_name": self.data["mentor_checklist/mentor/name"],
            "county": self.data["mentor_checklist/mentor/q_county"],
            "date_submitted": self.data["_submission_time"],
            "cme_completion_date": self.data[
                "mentor_checklist/cme_grp/cme_completion_date"
            ],
            "success_story": "null",
        }

    def get_facility_details(self):
        for key, value in self.data.items():
            if key.startswith("mentor_checklist/mentor/q_facility_") and value.strip():
                facility_code, facility_name = value.split("_", 1)
                return {
                    "facility_code": facility_code,
                    "facility_name": facility_name,
                }

    def get_cme_and_drill_topics(self):
        cme_topics = ["null"]
        drill_topics = ["null"]
        cme_topic_count = int(self.data["mentor_checklist/cme_grp/cme_total"])
        # FIXME :Taking into account cme_topic count only not drill count
        # drill_topic_count = int(self.data["mentor_checklist/drills_grp/drills_total"])
        for key, value in self.data.items():
            if key.startswith("mentor_checklist/cme_grp/cme_topics") and value.strip():
                temp_value = [value] * cme_topic_count
                cme_topics.extend(temp_value)
            if (
                key.startswith("mentor_checklist/drills_grp/drill_topics")
                and value.strip()
            ):
                temp_value = [value] * 1
                drill_topics.extend(temp_value)
        return cme_topics, drill_topics

    def get_cme_and_drill_particpants(self):
        drill_partcipants = []
        cme_partcipants = []
        for key, value in self.data.items():
            if (
                key.startswith(
                    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number"
                )
                and value.strip()
            ):
                cme_partcipants.append(value)
            if (
                key.startswith("mentor_checklist/drills_grp/id_numbers_drill/id_drill")
                and value.strip()
            ):
                drill_partcipants.append(value)
        return cme_partcipants, drill_partcipants

    def match_particpant_and_topics_to_rows(self):
        participations = []
        processed_data = self.get_flat_data()
        processed_data.update(self.get_facility_details())
        cme_t, drill_t = self.get_cme_and_drill_topics()
        cme_p, drill_p = self.get_cme_and_drill_particpants()
        for participant in cme_p:
            matching_data = deepcopy(processed_data)
            matching_data.update(
                {
                    "id_number_cme": participant,
                    "id_number_drill": "",
                    "essential_cme_topic": False,
                    "essential_drill_topic": False,
                }
            )
            for topic in cme_t:
                row = deepcopy(matching_data)
                row.update(
                    {
                        "cme_topic": topic,
                        "drill_topic": "null",
                        "essential_cme_topic": True,
                    }
                )
                participations.append(row)

        for participant in drill_p:
            matching_data = deepcopy(processed_data)
            matching_data.update(
                {
                    "id_number_drill": participant,
                    "id_number_cme": "",
                    "essential_cme_topic": False,
                    "essential_drill_topic": False,
                }
            )
            for topic in drill_t:
                row = deepcopy(matching_data)
                row.update(
                    {
                        "drill_topic": topic,
                        "cme_topic": "null",
                        "essential_drill_topic": True,
                    }
                )
                participations.append(row)

        return participations


class ParseRows:
    def __init__(self, data_rows) -> None:
        self.data_rows = data_rows

    def compute_cms_and_drill_topics(self):
        cme_topics = ["null"]
        drill_topics = ["null"]
        for row in self.data_rows:
            processor = ParseRow(row)
            cme_t, drill_t = processor.get_cme_and_drill_topics()
            cme_topics.extend(cme_t)
            drill_topics.extend(drill_t)
        return set(cme_topics), set(drill_topics)
