import pytest
import unittest
from apps import init_app




@pytest.mark.unit
class TestPingEnpoint(unittest.TestCase):
    def setUp(self):
        self.app = init_app(db=None)

    def test_ping_endpoint(self):
        with self.app.test_client() as client:
            response = client.get("/api/v1/ping")
            self.assertEqual(200, response.status_code)
            self.assertTrue(response.json["isAlive"])




