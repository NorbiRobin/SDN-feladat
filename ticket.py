import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DNA_CENTER_URL = "https://dna-center.example.com"
USERNAME = "cisco"
PASSWORD = "cisco123"

def get_service_ticket():
    url = f"{DNA_CENTER_URL}/dna/system/api/v1/auth/token"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers=headers,
        verify=False
    )

    response.raise_for_status()
    token = response.json()["Token"]
    return token


if __name__ == "__main__":
    ticket = get_service_ticket()
    print("Service ticket (token):")
    print(ticket)