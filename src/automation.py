from src.logger import logger
from src.screenshot import save_screenshot
from src.report import save_report
from tqdm import tqdm


def fill_form(driver, customer):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from src.config import WAIT_TIME

    wait = WebDriverWait(driver, WAIT_TIME)

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    last_name = driver.find_element(By.ID, "lastName")

    email = driver.find_element(By.ID, "userEmail")

    first_name.clear()
    first_name.send_keys(customer["first_name"])

    last_name.clear()
    last_name.send_keys(customer["last_name"])

    email.clear()
    email.send_keys(customer["email"])


def process_customers(driver, customers):

    results = []

    for customer in tqdm(
        customers,
        desc="Processing Customers",
        colour="green",
        ncols=80,
    ):

        try:

            logger.info(f"Processing {customer['first_name']}")

            fill_form(driver, customer)

            filename = (
                f"{customer['first_name']}_{customer['last_name']}.png"
            )

            save_screenshot(driver, filename)

            logger.info(f"Screenshot saved : {filename}")

            results.append({
                "first_name": customer["first_name"],
                "last_name": customer["last_name"],
                "email": customer["email"],
                "status": "Success",
                "message": "Completed"
            })

        except Exception as e:

            logger.exception(
                f"Failed processing {customer['first_name']} {customer['last_name']}"
            )

            filename = (
                f"ERROR_{customer['first_name']}_{customer['last_name']}.png"
            )

            save_screenshot(driver, filename)

            results.append({
                "first_name": customer["first_name"],
                "last_name": customer["last_name"],
                "email": customer["email"],
                "status": "Failed",
                "message": str(e)
            })

    save_report(results)

    return results