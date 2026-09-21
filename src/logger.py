import logging
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT/"logs"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

file_handler = logging.FileHandler(LOGS / "pipeline_coleta.log", encoding="utf-8")

console_handler = logging.StreamHandler()

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

