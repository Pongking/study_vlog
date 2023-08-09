import unittest
from name_function import get_formatted_name
#unittest to function
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name('pc','lee')
        self.assertEqual(formatted_name,'Pc Lee')

if __name__=='__main__':
    unittest.main()