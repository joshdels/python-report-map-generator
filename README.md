### Getting started

Documentations


Start the python environments
```
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv .venv  
source .venv/bin/activate
```
for checking
```
which python3
```

For project dependecies
```
pip -m venv .venv
pip install -r requirements.txt
source .venv/scripts/activate
```

For Dummy Backend Fast API for testing auth and rest api 
```
cd fast-api-backend 
uvicorn dummy_auth_api:app --reload
python test-api.py
```