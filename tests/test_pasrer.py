import pytest
import logging
import unittest
from pprint import pformat

from parser.parser import ParseRow, ParseRows

row_data = {
    "__version__": "vTJqT982rXnKw8jxwRsiuX",
    "_attachments": "[]",
    "_geolocation": "[None, None]",
    "_id": "464111771",
    "_notes": "[]",
    "_status": "submitted_via_web",
    "_submission_time": "2023-08-10T15:01:24",
    "_submitted_by": "",
    "_tags": "[]",
    "_uuid": "6aae8df2-b9a1-445a-8838-bed5eb64e7c8",
    "_validation_status": "{}",
    "_xform_id_string": "aKSyCXHYbyfGEyYQwxAuvt",
    "formhub/uuid": "a4dfd3a7c2ba4b1f9f43bebd48e124b1",
    "mentor_checklist/cme_grp/cme_comments": "",
    "mentor_checklist/cme_grp/cme_completion_date": "2023-08-03",
    "mentor_checklist/cme_grp/cme_topics": "Hypertension_in_pregnancy",
    "mentor_checklist/cme_grp/cme_topics_2": "Postpartum_haemorrhage_(PPH)",
    "mentor_checklist/cme_grp/cme_total": "2",
    "mentor_checklist/cme_grp/female_providers": "0",
    "mentor_checklist/cme_grp/male_providers": "1",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_10": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_11": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_12": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_13": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_14": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_15": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_16": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_17": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_18": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_19": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_1_001": "712345678",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_2": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_20": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_3": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_4": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_5": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_5": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_6": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_7": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_8": "",
    "mentor_checklist/cme_grp/standard_phone_numbers_cme/id_number_9": "",
    "mentor_checklist/drills_grp/comments_001": "",
    "mentor_checklist/drills_grp/date_002": "2023-08-03",
    "mentor_checklist/drills_grp/drill_topics": "Eclampsia",
    "mentor_checklist/drills_grp/drill_topics_2": "Shoulder_dystocia_birth_of_a_non-vigorou",
    "mentor_checklist/drills_grp/drills_total": "2",
    "mentor_checklist/drills_grp/female_providers_001": "1",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_1": "789765432",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_10": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_11": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_12": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_13": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_14": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_15": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_16": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_17": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_18": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_19": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_2": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_20": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_3": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_4": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_5": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_6": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_7": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_8": "",
    "mentor_checklist/drills_grp/id_numbers_drill/id_drill_9": "",
    "mentor_checklist/drills_grp/male_providers_001": "0",
    "mentor_checklist/mentor/name": "Dr Lex",
    "mentor_checklist/mentor/q_county": "Bungoma",
    "mentor_checklist/mentor/q_facility_bungoma": "15808_Bokoli_Hospital",
    "mentor_checklist/mentor/q_facility_busia": "",
    "mentor_checklist/mentor/q_facility_kajiado": "",
    "mentor_checklist/mentor/q_facility_kakamega": "",
    "mentor_checklist/mentor/q_facility_kiambu": "",
    "mentor_checklist/mentor/q_facility_kilifi": "",
    "mentor_checklist/mentor/q_facility_kirinyaga": "",
    "mentor_checklist/mentor/q_facility_kisii": "",
    "mentor_checklist/mentor/q_facility_kitui": "",
    "mentor_checklist/mentor/q_facility_machakos": "",
    "mentor_checklist/mentor/q_facility_makueni": "",
    "mentor_checklist/mentor/q_facility_meru": "",
    "mentor_checklist/mentor/q_facility_muranga": "",
    "mentor_checklist/mentor/q_facility_nairobi": "",
    "mentor_checklist/mentor/q_facility_nakuru": "",
    "mentor_checklist/mentor/q_facility_narok": "",
    "mentor_checklist/mentor/q_facility_nyeri": "",
    "mentor_checklist/mentor/q_facility_siaya": "",
    "mentor_checklist/records/assessment": "cme drills",
    "mentor_checklist/success_grp/date_004": "",
    "mentor_checklist/success_grp/story_success": "",
    "meta/instanceID": "uuid:6aae8df2-b9a1-445a-8838-bed5eb64e7c8",
    "today": "2023-08-10",
}
logging.basicConfig()
log = logging.getLogger("tests")


@pytest.mark.unit
class TestParseRowUnit(unittest.TestCase):
    def setUp(self):
        self.app = ParseRow(row_data)

    def test_get_flat_data(self):
        flat_data = self.app.get_flat_data()
        self.assertDictEqual(
            flat_data,
            {
                "mentor_name": "Dr Lex",
                "county": "Bungoma",
                "cme_completion_date": "2023-08-03",
                "date_submitted": "2023-08-10T15:01:24",
                "submission_id": "464111771",
                "success_story": "null",
            },
        )

    def test_get_facility_details(self):
        flat_data = self.app.get_facility_details()
        self.assertDictEqual(
            flat_data,
            {
                "facility_code": "15808",
                "facility_name": "Bokoli_Hospital",
            },
        )

    def test_get_cme_and_drill_particpants(self):
        cme_p, drill_p = self.app.get_cme_and_drill_particpants()
        self.assertListEqual(
            cme_p,
            ["712345678"],
        )
        self.assertListEqual(
            drill_p,
            ["789765432"],
        )

    def test_mapping(self):
        log.info(pformat(self.app.match_particpant_and_topics_to_rows()))


@pytest.mark.unit
class TestParseRowsUnit(unittest.TestCase):
    def setUp(self):
        self.app = ParseRows([row_data])

    def test_compute_cms_and_drill_topics(self):
        cme_topics, drill_topics = self.app.compute_cms_and_drill_topics()
        self.assertSetEqual(
            cme_topics,
            {
                "Hypertension_in_pregnancy",
                "Postpartum_haemorrhage_(PPH)",
                "null",
            },
        )
        self.assertSetEqual(
            drill_topics,
            {
                "Eclampsia",
                "Shoulder_dystocia_birth_of_a_non-vigorou",
                "null",
            },
        )


if __name__ == "__main__":
    unittest.main()
