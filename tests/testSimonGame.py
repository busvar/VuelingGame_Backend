import unittest, requests, json

class TestGameGeneration(unittest.TestCase):
 
    def testConnection(self):
        req = requests.get("http://127.0.0.1:5000/Simon/generateGame")
        self.assertEqual(req.status_code, 200)

    def testValidValued(self):
        req = requests.get("http://127.0.0.1:5000/Simon/generateGame")
        dict = json.loads(req.content)
        valid = True
        for item in dict['sequence']:
            if item < 0 or item > 3:
                valid = False
                break
        self.assertTrue(valid)
 
if __name__ == "__main__":
    unittest.main()