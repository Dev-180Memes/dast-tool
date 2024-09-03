# main.py

from scanner.scanning_controller import ScanningController
from reporting.report_generator import ReportGenerator
from config.settings import DATABASE_PATH, SCAN_RESULTS_PATH


def main():
    controller = ScanningController(DATABASE_PATH)

    # Add targets to scan
    controller.add_target("http://example.com")
    controller.add_target("http://testphp.vulnweb.com")

    # Start the scan
    controller.start_scan()

    # Generate reports
    results = controller.generate_report()
    report_generator = ReportGenerator(SCAN_RESULTS_PATH)
    report_generator.generate_text_report(results)
    report_generator.generate_html_report(results)

    # Cleanup
    controller.close()


if __name__ == "__main__":
    main()
