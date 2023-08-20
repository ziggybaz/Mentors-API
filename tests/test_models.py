import unittest
import pytest

from models import MentorCheck


@pytest.mark.unit
class TestMentorCheckModelUnit(unittest.TestCase):
    def test_mentor_chek_model_init(self):
        row = MentorCheck(
            cme_completion_date="23/08/23",
            cme_unique_id=1,
            county="Bungoma",
            date_submitted="23/08/23",
            drill_unique_id=1,
            essential_cme_topic=False,
            essential_drill_topic=True,
            facility_code="24252",
            facility_name="Bokoli_Hospital",
            id_number_cme=1123,
            id_number_drill=2332,
            mentor_name="Dr Tom",
            submission_id=1111,
            success_story="null",
        )

        self.assertEqual(row.county, "Bungoma")
        self.assertEqual(row.mentor_name, "Dr Tom")
        self.assertEqual(row.id_number_cme, 1123)
        self.assertEqual(row.submission_id, 1111)
        self.assertEqual(row.date_submitted, "23/08/23")
        self.assertEqual(row.cme_completion_date, "23/08/23")
