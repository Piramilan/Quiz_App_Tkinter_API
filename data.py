import requests


parameter = {
    "amount":50,
    "type":"boolean"
}

resopnse = requests.get(url="https://opentdb.com/api.php?",params=parameter)
resopnse.raise_for_status()
question_data = resopnse.json()['results']
