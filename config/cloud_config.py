from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Local S3-style data lake paths
DATA_LAKE_DIR = PROJECT_ROOT / "data_lake"
RAW_ZONE = DATA_LAKE_DIR / "raw"
PROCESSED_ZONE = DATA_LAKE_DIR / "processed"

# Simulated cloud bucket name for architecture documentation
S3_BUCKET_NAME = "market-data-platform-demo-bucket"

RAW_ZONE.mkdir(parents=True, exist_ok=True)
PROCESSED_ZONE.mkdir(parents=True, exist_ok=True)