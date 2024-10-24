from fastapi import APIRouter, HTTPException
from app.services.replicate import ReplicateService
from app.schemas.auth import TokenResponse
import requests

router = APIRouter(
    prefix="/auth",
    tags=["Oauth"],
    responses={
        404: {"description": "Not Found"},
        401: {"description": "Unauthorized"},
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"}
    }
)


@router.post("/token", response_model=TokenResponse, tags=["Authenticated"])
async def get_oauth_token():
    """
    Fetch an OAuth2 token from the Replicate Service

    This endpoint uses the API key configured in the environment variables
    to fetch an access token that can be used for subsequent API requests.

    
    Returns:
        TokenResponse: The access token, its type and expiration time.
    
    Raises:
        HTTPException: If the token fetching fails

    """

    try:
        token_response = ReplicateService.fetch_oauth_token()
        return token_response
    except requests.RequestException as e:
        raise HTTPException(status_code = 400, detail=str(e))
    
    

