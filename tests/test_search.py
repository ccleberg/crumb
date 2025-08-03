import unittest
from unittest.mock import patch
from search import search_log

class TestSearchLog(unittest.TestCase):

    @patch('search.LOG_PATH', 'test_log_path')
    def test_search_log_with_match(self, mock_log_path):
        query = 'crumb'
        # Create a dummy log file (for testing)
        with open('test_log_path', 'w') as f:
            f.write("* Example Entry\n")
            f.write(":PROPERTIES:\n")
            f.write(":URL:       http://example.com\n")
            f.write(":TIMESTAMP: 2023-10-27 10:00:00\n")

        search_log(query)
        # Assert that the function prints the expected output
        with open('test_log_path', 'r') as f:
            output = f.read()
        self.assertIn("* Example Entry\n", output)

    @patch('search.LOG_PATH', 'test_log_path')
    def test_search_log_no_match(self, mock_log_path):
        query = 'nonexistent'
        with open('test_log_path', 'w') as f:
            f.write("* Example Entry\n")
            f.write(":PROPERTIES:\n")
            f.write(":URL:       http://example.com\n")
            f.write(":TIMESTAMP: 2023-10-27 10:00:00\n")
        search_log(query)
        with open('test_log_path', 'r') as f:
            output = f.read()
        self.assertNotIn("* Example Entry\n", output)
