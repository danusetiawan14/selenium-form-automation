from pathlib import Path

# =========================
# Project Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
SCREENSHOT_DIR = BASE_DIR / "screenshots"

INPUT_FILE = DATA_DIR / "input.xlsx"
OUTPUT_FILE = DATA_DIR / "output.xlsx"

# =========================
# Selenium Configuration
# =========================
URL = "https://demoqa.com/automation-practice-form"

WAIT_TIME = 10

APP_NAME = "Python Selenium Form Automation"

VERSION = "1.0.0"
