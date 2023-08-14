#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
TEST CASES
"""

import unittest
from models.user import User
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]  # Add more file paths if needed
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)
