import requests
import os
from datetime import datetime
APP_ID=os.environ["NT_APP_ID"]
API_KEY=os.environ["NT_API_KEY"]
GENDER="female"
WEIGHT_KG=50.5
HEIGHT_CM=155.64
AGE=19

excercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_input=input("Tell me which exercises you did")
sheet_endpoint=os.environ["SHEET_ENDPOINT"]
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
Nutri_params={
    "query":"ran 3 miles",
     "gender":GENDER,
     "weight_kg":WEIGHT_KG,
     "height_cm":HEIGHT_CM,
     "age":AGE
}

response=requests.post(url=excercise_endpoint,json=Nutri_params,headers=headers)
result=response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for excercise in result["exercises"]:
    sheet_params={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":excercise["name"].title(),
            "duration":excercise["duration_min"],
            "calories":excercise["nf_calories"]
        }
    }

bearer_headers={
    "Authorization":f"Bearer {os.environ['TOKEN']}"
}
sheet_response=requests.post(url=sheet_endpoint,json=sheet_params,headers=bearer_headers)
print(sheet_response.text)
