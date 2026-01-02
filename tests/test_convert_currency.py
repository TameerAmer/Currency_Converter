from fastapi.testclient import TestClient
import unittest
from main import app


class TestConvertCurrency(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_empty_data(self):
        response = self.client.post("/convert", json={})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("Error", data)
        self.assertEqual(data["Error"], "No data provided")

    def test_same_currency(self):
        response = self.client.post(
            "/convert", json={"ammount": "100", "from": "USD", "to": "USD"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["Converted ammount"], 100.0)

    def test_convert_currency(self):
        response = self.client.post(
            "/convert", json={"ammount": "100", "from": "USD", "to": "EUR"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["Converted ammount"], 85.29)


if __name__ == "__main__":
    unittest.main()
