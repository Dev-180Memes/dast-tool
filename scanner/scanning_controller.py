# scanner/scanning_controller.py

from .scanner_engine import ScannerEngine
from .target_manager import TargetManager
from database.db_manager import DBManager

class ScanningController:
    def __init__(self, db_path):
        self.target_manager = TargetManager()
        self.scanner_engine = ScannerEngine()
        self.db_manager = DBManager(db_path)

    def add_target(self, url):
        self.target_manager.add_target(url)

    def start_scan(self):
        targets = self.target_manager.get_targets()
        for target in targets:
            self.scanner_engine.scan(target)
            vulnerabilities = self.scanner_engine.get_vulnerabilities()
            for vulnerability in vulnerabilities:
                name, severity, url = vulnerability
                self.db_manager.insert_scan_result(target, name, severity, "Refer to OWASP guidelines")

    def generate_report(self):
        results = self.db_manager.fetch_all_results()
        return results

    def close(self):
        self.db_manager.close()
