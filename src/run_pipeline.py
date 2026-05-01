import logging
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "pipeline.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


def run_command(step_name: str, script_path: str) -> None:
    full_script_path = PROJECT_ROOT / script_path

    logger.info("START: %s", step_name)

    result = subprocess.run(
        [sys.executable, str(full_script_path)],
        cwd=PROJECT_ROOT,
        check=False,
    )

    if result.returncode != 0:
        logger.error("FAILED: %s", step_name)
        raise RuntimeError(f"{step_name} failed with exit code {result.returncode}")

    logger.info("SUCCESS: %s", step_name)


def run_ingestion() -> None:
    run_command("API Ingestion", "src/ingest_api.py")


def run_transformation() -> None:
    run_command("Data Transformation", "src/transform.py")


def run_warehouse_load() -> None:
    run_command("Warehouse Load", "src/load_warehouse.py")


def run_validation() -> None:
    run_command("Data Quality Validation", "src/validate.py")


def run_analytics() -> None:
    run_command("Analytics Generation", "src/analytics.py")


def run_full_pipeline() -> None:
    logger.info("=" * 80)
    logger.info("PRODUCTION MARKET DATA PIPELINE STARTED")
    logger.info("Run timestamp UTC: %s", datetime.now(timezone.utc).isoformat())
    logger.info("=" * 80)

    run_ingestion()
    run_transformation()
    run_warehouse_load()
    run_validation()
    run_analytics()

    logger.info("=" * 80)
    logger.info("PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 80)


def main() -> None:
    run_full_pipeline()


if __name__ == "__main__":
    main()