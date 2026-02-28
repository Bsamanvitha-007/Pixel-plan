from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# =========================
# DESIGN SCHEMAS
# =========================

class DesignCreate(BaseModel):
    style: str


class DesignResponse(BaseModel):
    id: int
    style: str
    original_image: str
    generated_image: str
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# IMAGE ANALYSIS RESPONSE
# =========================

class AnalysisResponse(BaseModel):
    brightness: float
    room_type: str


# =========================
# UPLOAD RESPONSE
# =========================

class UploadResponse(BaseModel):
    message: str
    analysis: AnalysisResponse
    generated_image: strS