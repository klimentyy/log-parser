

import logging
import os
import unittest

from log_analyzer.parser import LogParser


class TestCase2LogParser(unittest.TestCase):
    def setUp(self):
        self.log_file_path = "tests/data/log.txt"
        self.output_file_path = "tests/test_outputs/output_report_2.txt"
        self.threshold = 1
        self.log_level = logging.INFO

    def test_log_parser(self):
        parser = LogParser(
            self.log_file_path, self.output_file_path, self.threshold, log_level=self.log_level
        )
        parser.parse()
        parser.generate_report()

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.output_file_path))

        # Check if the output file contains expected content
        with open(self.output_file_path, "r") as f:
            content = f.read()
            self.assertIn("Total log entries: 3", content)
            self.assertIn("Entries above threshold: 1", content)    