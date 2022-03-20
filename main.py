import requests

GENDER = "male"
WEIGHT_KG = 70.3
HEIGHT_CM = 182.88
AGE = 35

NUTRITION_ID = "8a95e5b3"
NUTRITION_API = "34b6671a1d89ea1acd6a22fff85e95ec"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did. ")

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
