# scanner/scanner_engine.py

import requests

class ScannerEngine:
    def __init__(self):
        self.vulnerabilities = []

    def scan(self, target):
        self.detect_sql_injection(target)
        self.detect_xss(target)

    def detect_sql_injection(self, url):
        payloads = ["' OR '1'='1", "' OR '1'='2"]
        for payload in payloads:
            test_url = f"{url}?id={payload}"
            response = requests.get(test_url)
            if "syntax error" in response.text.lower():
                self.vulnerabilities.append(("SQL Injection", "High", test_url))

    def detect_xss(self, url):
        payload = "<script>alert('XSS')</script>"
        response = requests.get(url, params={"q": payload})
        if payload in response.text:
            self.vulnerabilities.append(("Cross-Site Scripting (XSS)", "Medium", url))

    def get_vulnerabilities(self):
        return self.vulnerabilities
