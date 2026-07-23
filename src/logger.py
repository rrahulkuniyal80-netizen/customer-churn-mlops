import logging
import os
from datetime import datetime

Log_dir = 'logs'
os.makedirs(Log_dir, exist_ok=True)

Log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

Log_path = os.path.join(Log_dir, Log_file)
logging.basicConfig(
    filename=Log_path,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)