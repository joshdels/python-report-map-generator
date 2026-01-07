from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

# ------------------------------------------------------------------
# Dummy users database
# ------------------------------------------------------------------
USERS_DB = {
    "alice@example.com": {
        "password": "alice123",
        "data": {"name": "Alice", "role": "admin"}
    },
    "bob@example.com": {
        "password": "bob123",
        "data": {"name": "Bob", "role": "editor"}
    },
}

# ------------------------------------------------------------------
# In-memory GeoJSON store (DEV ONLY)
# ------------------------------------------------------------------
FEATURE_STORE = {
    "type": "FeatureCollection",
    "features": []
}

# OAuth2 token scheme (token = email for demo)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ------------------------------------------------------------------
# AUTH
# ------------------------------------------------------------------
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {
        "access_token": form_data.username,
        "token_type": "bearer"
    }


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = USERS_DB.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user


# ------------------------------------------------------------------
# USER DATA
# ------------------------------------------------------------------
@app.get("/mydata")
async def get_user_data(user: dict = Depends(get_current_user)):
    return user["data"]


# ------------------------------------------------------------------
# GET GEOJSON (QGIS reads from here)
# ------------------------------------------------------------------
@app.get("/geojson")
async def get_geojson(user: dict = Depends(get_current_user)):
    return FEATURE_STORE


# ------------------------------------------------------------------
# UPLOAD COORDINATES → SERVER BUILDS FEATURES
# ------------------------------------------------------------------
class PointIn(BaseModel):
    lat: float
    lng: float
    name: Optional[str] = None


class PointsPayload(BaseModel):
    points: List[PointIn]


@app.post("/upload/coordinates")
async def upload_coordinates(
    payload: PointsPayload,
    user: dict = Depends(get_current_user)
):
    new_features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [p.lng, p.lat]
            },
            "properties": {
                "name": p.name,
                "uploaded_by": user["data"]["name"]
            }
        }
        for p in payload.points
    ]

    FEATURE_STORE["features"].extend(new_features)

    return {
        "status": "ok",
        "added": len(new_features),
        "total": len(FEATURE_STORE["features"])
    }


# ------------------------------------------------------------------
# UPLOAD GEOJSON DIRECTLY (BEST FOR QGIS)
# ------------------------------------------------------------------
@app.post("/upload/geojson")
async def upload_geojson(
    geojson: Dict,
    user: dict = Depends(get_current_user)
):
    if geojson.get("type") != "FeatureCollection":
        raise HTTPException(status_code=400, detail="Invalid GeoJSON")

    new_features = geojson.get("features", [])

    FEATURE_STORE["features"].extend(new_features)

    return {
        "status": "ok",
        "added": len(new_features),
        "total": len(FEATURE_STORE["features"])
    }
