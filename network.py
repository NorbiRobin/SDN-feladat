import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DNA_CENTER_URL = "https://dna-center.example.com"
SERVICE_TICKET = "IDE_JÖN_A_TOKEN"

def get_network_devices():
    url = f"{DNA_CENTER_URL}/dna/intent/api/v1/network-device"
    headers = {
        "X-Auth-Token": SERVICE_TICKET,
        "Content-Type": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        verify=False
    )

    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    devices = get_network_devices()

    for device in devices:
        platform_id = device.get("platformId")
        management_ip = device.get("managementIpAddress")

        print(f"Platform ID: {platform_id}, Management IP: {management_ip}")