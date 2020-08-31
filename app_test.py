from app import app

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/heros.json', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    
    
    
  def test_index_content(self):
    tester = app.test_client(self)
    response = tester.get('/heros.json', content_type='application/json')
    self.assertEqual(response.content_type, 'application/json')
    
    
if __name__ == '__main__':
    unittest.main()
