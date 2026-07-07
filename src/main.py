from src.browser import create_driver
from src.config import URL
from src.logger import logger
from src.excel import read_excel
from src.automation import process_customers

from src.ui import (
    show_startup,
    show_browser_start,
    show_summary,
)


def main():

    # ===============================
    # Load Excel
    # ===============================

    customers = read_excel()

    show_startup(customers)

    # ===============================
    # Browser
    # ===============================

    logger.info("Starting browser")

    show_browser_start()

    driver = create_driver()

    driver.get(URL)

    # ===============================
    # Automation
    # ===============================

    results = process_customers(
        driver,
        customers
    )

    # ===============================
    # Summary
    # ===============================

    show_summary(results)

    input("Press ENTER to close browser...")

    driver.quit()

    logger.info("Browser closed")


if __name__ == "__main__":
    main()