from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Dict

app = FastAPI()

# Dummy users database
USERS_DB = {
    "alice@example.com": {"password": "alice123", "data": {"name": "Alice", "role": "admin"}},
    "bob@example.com": {"password": "bob123", "data": {"name": "Bob", "role": "editor"}},
}

# OAuth2 token scheme (for simplicity we just return email as token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Login endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Return dummy token (just the email for this example)
    return {"access_token": form_data.username, "token_type": "bearer"}


# Protected endpoint: get user-specific data
@app.get("/mydata")
async def get_user_data(token: str = Depends(oauth2_scheme)):
    user = USERS_DB.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user["data"]

# Sample GeoJSON
@app.get("/geojson")
async def get_geojson(token: str= Depends(oauth2_scheme)):
    user = USERS_DB.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Example GeoJSON data
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [125.6, 10.1]},
                "properties": {"name": "Sample Point 1"}
            },
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [125.7, 10.2]},
                "properties": {"name": "Sample Point 2"}
            }
        ]
    }
    return geojson_data
