import logging
import os

CRITERIA_THRESHOLDS = (
    (50, True, True, True, "Platinum"),
    (25, False, True, True, "Gold"),
    (10, False, False, True, "Silver"),
    (10, False, False, False, "Bronze"),
)

users_api_url = os.environ.get("USERS_API_URL", "http://127.0.0.1:8080/")
swagger_json_path = os.environ.get("SWAGGER_JSON_PATH", "static/swagger.json")
log_level = os.environ.get("LOG_LEVEL", "INFO")

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
