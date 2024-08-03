from wagtail.rich_text import get_text_for_indexing
import unittest

class TestGetTextForIndexing(unittest.TestCase):

    def test_html_with_cyrillic(self):
        html = "<div>ПЪ</div>"
        expected = "ПЪ"
        result = get_text_for_indexing(html)
        self.assertEqual(result, expected)
        
    def test_html_with_monetary_symbols(self):
        html = "<div>$€¥¢₹</div>"
        expected = "$€¥¢₹"
        result = get_text_for_indexing(html)
        self.assertEqual(result, expected)
    
    def test_html_with_extended_latin(self):
        html = "<div>ÇꜲĒ</div>"
        expected = "ÇꜲĒ"
        result = get_text_for_indexing(html)
        self.assertEqual(result, expected)
        
        
if __name__ == '__main__':
    unittest.main()
