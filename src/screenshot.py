from src.config import SCREENSHOT_DIR


def save_screenshot(driver, filename):
    """
    Menyimpan screenshot browser.
    """

    SCREENSHOT_DIR.mkdir(exist_ok=True)

    filepath = SCREENSHOT_DIR / filename

    driver.save_screenshot(str(filepath))

    return filepath