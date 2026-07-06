import time

from src.browser import create_driver
from src.config import URL


def main():
    driver = create_driver()

    driver.get(URL)

    time.sleep(5)

    driver.quit()


if __name__ == "__main__":
    main()