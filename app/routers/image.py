from fastapi import APIRouter, HTTPException, Depends
from app.schemas.image import ImageGenerationRequest, ImageGenerationResponse
from app.services.replicate import ReplicateService
from app.services.auth import verify_token

router = APIRouter(
    prefix="/images",
    tags=["Images"],
    responses={404: {"description": "Not Found"}}
)

replicate_service = ReplicateService()

@router.post("/generate", response_model=ImageGenerationResponse, summary="Generate an Image")
async def generate_image(request: ImageGenerationRequest,
                        token: str = Depends(verify_token)
                        ):
    """
    Generates an image based on the provided text prompt and model version.

    - **prompt**: The description to guide image generation.
    - **model_version**: The model version to use for generation.
    - **image_size**: The desired size of the image (default is 512x512).
    
    Returns:
        JSON Response with the generated image URL.

    Raises:
        HTTPException: If the image generation fails
        
    """

    image_url = await replicate_service.generate_image(
            
        )

    try:
        service = ReplicateService()
        image_url = await service.generate_image(prompt=request.prompt,
            model_version=request.model_version,
            image_size=request.image_size
        )
        return ImageGenerationResponse(image_url=image_url, success=True)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
