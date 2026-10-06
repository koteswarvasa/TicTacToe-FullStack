from pydantic import BaseModel, EmailStr


class PlayerCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_nm: str | None = None
    last_nm: str | None = None


class PlayerResponse(BaseModel):
    player_id: int
    username: str
    email: str
    first_nm: str | None
    last_nm: str | None
    is_active: bool

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    player_id: int
    username: str
    first_nm: str | None
    last_nm: str | None
    message: str