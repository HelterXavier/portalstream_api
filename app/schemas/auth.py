from pydantic import BaseModel


class Credential(BaseModel):
    username: str
    password: str


class AuthToken(BaseModel):
    refresh: str
    access: str


class RefreshToken(BaseModel):
    refresh: str


class AccessToken(BaseModel):
    access: str


class VerifyToken(BaseModel):
    token: str
