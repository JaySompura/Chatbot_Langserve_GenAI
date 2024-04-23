import requests

response  = requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"Dr. Vikram Sarabhai"}}
    )

print(response.json()["output"]["content"])
