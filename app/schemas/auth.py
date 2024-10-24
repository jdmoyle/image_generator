from pydantic import BaseModel, Field

class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Oauth2 access token fetched from replicate service.")
    token_type: str = Field(..., description="Oauth2 token type recieved from replicate service.")
    expires_in: int = Field("", description="Oauth2 token expiration time in seconds.")
