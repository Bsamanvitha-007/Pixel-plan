import os
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

# Create folders if not exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("generated", exist_ok=True)

app = FastAPI()

# Enable CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount generated folder
app.mount("/generated", StaticFiles(directory="generated"), name="generated")


def apply_style(image_path, style):
    image = cv2.imread(image_path)

    if style == "scandinavian":
        # Bright and soft
        styled = cv2.convertScaleAbs(image, alpha=1.2, beta=30)

    elif style == "modern":
        # High contrast
        styled = cv2.convertScaleAbs(image, alpha=1.5, beta=10)

    elif style == "vintage":
        # Sepia effect
        sepia_filter = np.array(
            [[0.272, 0.534, 0.131],
             [0.349, 0.686, 0.168],
             [0.393, 0.769, 0.189]]
        )
        styled = cv2.transform(image, sepia_filter)
        styled = np.clip(styled, 0, 255).astype(np.uint8)

    else:
        styled = image

    return styled


@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    style: str = Query(...)
):
    try:
        # Save uploaded image
        upload_path = f"uploads/{file.filename}"
        with open(upload_path, "wb") as buffer:
            buffer.write(await file.read())

        # Apply style
        styled_image = apply_style(upload_path, style)

        # Save generated image
        output_path = f"generated/styled_{file.filename}"
        cv2.imwrite(output_path, styled_image)

        return {
            "message": "Image styled successfully",
            "image_url": f"http://127.0.0.1:8000/{output_path}"
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
