# reporting/report_generator.py

import os

class ReportGenerator:
    def __init__(self, report_dir):
        self.report_dir = report_dir

    def generate_text_report(self, scan_results):
        report_path = os.path.join(self.report_dir, "scan_report.txt")
        with open(report_path, "w") as report_file:
            for result in scan_results:
                target, vulnerability, severity, recommendation = result[1:]
                report_file.write(f"Target: {target}\nVulnerability: {vulnerability}\nSeverity: {severity}\nRecommendation: {recommendation}\n\n")

    def generate_html_report(self, scan_results):
        report_path = os.path.join(self.report_dir, "scan_report.html")
        with open(report_path, "w") as report_file:
            report_file.write("<html><body><h1>Scan Report</h1>")
            for result in scan_results:
                target, vulnerability, severity, recommendation = result[1:]
                report_file.write(f"<h2>Target: {target}</h2><p><strong>Vulnerability:</strong> {vulnerability}</p><p><strong>Severity:</strong> {severity}</p><p><strong>Recommendation:</strong> {recommendation}</p><hr>")
            report_file.write("</body></html>")
