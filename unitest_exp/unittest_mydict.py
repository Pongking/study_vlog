import unittest
from my_dict import MyDict

class TestDict(unittest.TestCase):
    def setUp(self):
        self.keys=['a','b','c','d']
        self.values=['1','2','3','4']
        self.dict=MyDict()
    
    def testDict(self):
        for k,v in zip(self.keys,self.values):
            self.dict.put(k,v)
        for key,value in zip(self.keys,self.values):
            self.assertEqual(self.dict.get(key),value)
        

if __name__ =='__main__':
    unittest.main()