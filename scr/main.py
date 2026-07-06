from browser import create_driver
from config import URL
import time


driver = create_driver()

driver.get(URL)

time.sleep(5)

driver.quit()
