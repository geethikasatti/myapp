import unittest
import json
from app import app

class BackendTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        resp = self.client.get("/")
        data = json.loads(resp.data)
        self.assertEqual(data["message"], "Hello from Backend!")

    def test_add_numbers(self):
        resp = self.client.post("/add", json={"a": 2, "b": 3})
        data = json.loads(resp.data)
        self.assertEqual(data["result"], 5)

if __name__ == "__main__":
    unittest.main()
