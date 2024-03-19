import requests
from .variable_handler import get_whmcs_variables

whmcs_variables = get_whmcs_variables()


def request():
    api_url = "https://www.example.com/includes/api.php"
    payload = whmcs_variables["payload"]
    response = requests.post(api_url, data=payload)
    return response.json()
