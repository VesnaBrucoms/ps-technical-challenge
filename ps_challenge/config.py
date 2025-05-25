import os

users_api_url = os.environ.get("USERS_API_URL", "http://127.0.0.1:8080/")
swagger_json_path = os.environ.get("SWAGGER_JSON_PATH", "static/swagger.json")
log_level = os.environ.get("LOG_LEVEL", "INFO")
