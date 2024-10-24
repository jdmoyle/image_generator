import httpx
import requests
from app.config import settings
from app.schemas.auth import TokenResponse

REPLICATE_BASE_URL = "https://api.replicate.com/v1"

class ReplicateService:
    """
    Service for interacting with the Replicate Image Generation API.
    """
    def __init__(self):
        self.api_key = settings.REPLICATE_API_KEY
        self.headers = {
            "Authorization": f"Token {self.api_key}",
            "Content-Type": "application/json"
        }

    async def generate_image(self, prompt: str, model_version: str, image_size: str) -> str:
        """
        Sends a request to the Replicate API to generate an image based on a prompt.
        
        :param prompt: The text prompt for the image.
        :param model_version: The specific model version to be used.
        :param image_size: Desired dimensions for the output image.
        :return: The URL of the generated image.
        :raises Exception: If there is an error in generating the image.
        """
        async with httpx.AsyncClient() as client:
            payload = {
                "version": settings.REPLICATE_MODEL_NAME,
                "input": {
                    "prompt": prompt,
                    "image_size": image_size
                }
            }
            response = await client.post(f"{REPLICATE_BASE_URL}/predictions", json=payload, headers=self.headers)
            
            if response.status_code == 201:
                prediction = response.json()
                return prediction.get("output", {}).get("image", "")
            else:
                raise Exception(f"Failed to generate image: {response.text}")
