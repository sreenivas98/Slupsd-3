import unittest
from mock import patch, MagicMock
from Text import Text

class TestDialogClass(unittest.TestCase):
    @patch("Text.Text.showDialog")
    def test_showDialog(self, mockHello):
        print("Using Mock")
        self.assertFalse(mockHello.called)
        Text().showDialog()
        self.assertTrue(mockHello.called)
        self.assertEqual(mockHello.call_count, 1)
        self.assertIsInstance(mockHello, MagicMock)
        print("Mock Test for showDialog Successful")
    
    @patch("Text.Text.hideDialog")
    def test_hideDialog(self, mockHello):
        print("Using Mock")
        self.assertFalse(mockHello.called)
        Text().hideDialog()
        self.assertTrue(mockHello.called)
        self.assertEqual(mockHello.call_count, 1)
        self.assertIsInstance(mockHello, MagicMock)
        print("Mock Test for hideDialog Successful")
      
    @patch("Text.Text.setDialog2")
    def test_setDialog2(self, mockHello):
        print("Using Mock")
        self.assertFalse(mockHello.called)
        Text().setDialog2("hello!")
        self.assertTrue(mockHello.called)
        self.assertEqual(mockHello.call_count, 1)
        self.assertIsInstance(mockHello, MagicMock)
        print("Mock Test for setDialog2(,msg) Successful")
        
    @patch("Text.Text.setDialog")
    def test_setDialog(self, mockHello):
        print("Using Mock")
        self.assertFalse(mockHello.called)
        Text().setDialog('Harry',"hello!")
        self.assertTrue(mockHello.called)
        self.assertEqual(mockHello.call_count, 1)
        self.assertIsInstance(mockHello, MagicMock)
        print("Mock Test for setDialog(name,msg) Successful")
    

if __name__ == '__main__':
    unittest.main()