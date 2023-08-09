import unittest
from survey import AnonymousSurvey
#unitest to survey

class TestAnonymoussurvey(unittest.TestCase):
    #setUp 是TestCase特有的函数，类似init，初始化
    def setUp(self):
        question="What language did you first learn to speak"
        self.my_survy=AnonymousSurvey(question)
        
    def test_store_single_response(self):
        self.my_survy.store_response('Chinese')
        self.assertIn('English',self.my_survy.responses)
    
    def test_store_three_response(self):
        responses=['Chinese','Japanese','English']
        for response in responses:
            self.my_survy.store_response(response)
        self.assertIn('English',self.my_survy.responses)

if __name__ == '__main__':
    unittest.main()