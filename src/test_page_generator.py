import unittest
from page_generator import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        text = """# title of text
body
end of text"""
        expected = '# title of text'
        self.assertEqual(extract_title(text), expected)

    def test_extract_title_no_header(self):
        text = """## title of text
body
end of text"""
        self.assertRaises(Exception, extract_title, text)

    def test_extract_title_two_headers(self):
        text = """# title of text
# extra header
body
end of text"""
        self.assertRaises(Exception, extract_title, text)

if __name__ == "__main__":
    unittest.main()