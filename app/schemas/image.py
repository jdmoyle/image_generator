from pydantic import BaseModel, Field

class ImageGenerationRequest(BaseModel):
    prompt: str = Field(..., description="The text prompt to guide image generation.")
    model_version: str = Field(..., description="The version of the model to be used.")
    image_size: str = Field("512x512", description="The desired size of the generated image (e.g., 512x512).")

class ImageGenerationResponse(BaseModel):
    image_url: str = Field(..., description="The URL of the generated image.")
    success: bool = Field(..., description="Indicates if the image generation was successful.")
    message: str = Field("", description="Additional message or error details.")
