
import logging
from pathlib import Path
import re
import re
from typing import Counter, Optional



class LogParser:
    def __init__(self, log_file_path: str, output_file_path: Optional[str] = None, threshold: int = 0, log_level: int = logging.INFO):
        self.log_file_path = log_file_path
        self.output_file_path = output_file_path
        self.threshold = threshold

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        self.ip_counter = Counter()
        self.status_code_counter = Counter()
        self.corrupted_lines = 0

    def parse(self) -> None:
        file_path = Path(self.log_file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Log file '{self.log_file_path}' does not exist.")
        
        with file_path.open("r") as f:
            for line in f:
                ip_address = self._extract_ip(line)
                status_code = self._extract_status_code(line)
                if ip_address and status_code:
                    self.ip_counter[ip_address] += 1
                    self.status_code_counter[status_code] += 1
                else:
                    self.corrupted_lines += 1
        
    def _extract_ip(self, line: str) -> Optional[str]:
        match = re.search(r"(\d{1,3}\.){3}\d{1,3}", line)
        return match.group(0) if match else None

    def _extract_status_code(self, line: str) -> Optional[str]:
        # search for status code in the format "Http/1.1" 200
        match = re.search(r' "\s+(\d{3})\s', line)
        return match.group(1) if match else None

    def generate_report(self):
        # Placeholder for report generation logic
        pass