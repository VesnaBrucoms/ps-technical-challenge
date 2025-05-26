import logging
import os

from ps_challenge.models.threshold import Threshold


CRITERIA_THRESHOLDS = (
    Threshold(50, 1, True, True, True, "Platinum"),
    Threshold(25, 0.8, False, True, True, "Gold"),
    Threshold(10, 0.75, False, False, True, "Silver"),
    Threshold(10, 0, False, False, False, "Bronze"),
)

users_api_url = os.environ.get("USERS_API_URL", "http://127.0.0.1:8080/")
swagger_json_path = os.environ.get("SWAGGER_JSON_PATH", "static/swagger.json")
log_level = os.environ.get("LOG_LEVEL", "INFO")

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
