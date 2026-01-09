# Automation Map Report 
This is my side hustle project. Learning the python automation skills which will later on be used for solving boring repeatitable and painful projects of my client

Core Documentations
for docxtpl 
https://docxtpl.readthedocs.io/en/latest/

for pyqt5 gui refer to this 
https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/


for fast-api studies
https://fastapi.tiangolo.com/

----

### Environment Setup

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

----
### For simple backend 
For Dummy Backend Fast API for testing auth and rest api 

```
cd fast-api-backend 
uvicorn dummy_auth_api:app --reload
python test-api.py
```