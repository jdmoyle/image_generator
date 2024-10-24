import requests
import time
from app.config import config
from app.schemas.auth import TokenResponse

class TokenManager:
    def __init__(self):
        self.token = None
        self.expiry_time = 0

    def fetch_oauth_token(self) -> TokenResponse:
        headers = {
        "Authorization": f"Bearer {config.REPLICATE_API_KEY}",
        "Content-Type": "application/json"
        }

        response = requests.post(config.REPLICATE_API_URL, headers=headers)
        response.raise_for_status() # Raise an error for bad responses

        token_response = TokenResponse(**response.json())
        self.token = token_response.access_token
        # Set expiry time (assuming expires_in is in seconds)
        self.expiry_time = time.time() + token_response.expires_in
        return token_response

    def get_valid_token(self) -> str:
        # Check if token is still valid
        if self.token is None or time.time() >= self.expiry_time:
            self.fetch_oauth_token() # Fetch a new token if expired
        return self.token

# Create a single instance of TokenManager
token_manager = TokenManager()