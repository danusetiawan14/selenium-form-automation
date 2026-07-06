import logging

from src.config import LOG_DIR

# Membuat folder logs jika belum ada
LOG_DIR.mkdir(exist_ok=True)

# Konfigurasi logging
logging.basicConfig(
    filename=LOG_DIR / "automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)