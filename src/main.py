show_banner()

from src.browser import create_driver
from src.config import URL
from src.logger import logger
from src.excel import read_excel
from src.automation import process_customers
from src.banner import show_banner


def main():

    logger.info("Starting browser")

    driver = create_driver()

    driver.get(URL)

    customers = read_excel()

    logger.info(f"Found {len(customers)} customer(s)")

    process_customers(driver, customers)

    input("Press ENTER to close browser...")

    driver.quit()

    logger.info("Browser closed")


if __name__ == "__main__":
    main()