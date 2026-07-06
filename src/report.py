from openpyxl import Workbook

from src.config import OUTPUT_FILE


def save_report(results):
    """
    Menyimpan hasil automation ke output.xlsx
    """

    wb = Workbook()

    ws = wb.active

    ws.title = "Automation Report"

    # Header
    ws.append([
        "First Name",
        "Last Name",
        "Email",
        "Status",
        "Message"
    ])

    # Data
    for row in results:
        ws.append([
            row["first_name"],
            row["last_name"],
            row["email"],
            row["status"],
            row["message"]
        ])

    wb.save(OUTPUT_FILE)