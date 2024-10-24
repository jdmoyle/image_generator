from fastapi import Depends, HTTPException
from app.services.token import token_manager

async def verify_token(token: str = Depends(token_manager.get_valid_token)):
    """
    Dependency to verify the OAuth2 token.

    Raises:
        HTTPException: If the token is invalid or expired.
    """

    if not token:
        raise HTTPException(status_code = 401, detail ="Invalid or expired token")
    