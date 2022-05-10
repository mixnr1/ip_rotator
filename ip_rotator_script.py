import os
import time
import requests
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS

#https://github.com/Ge0rg3/requests-ip-rotator

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
src = 'https://api64.ipify.org'
for i in range(5):
    # Create gateway object and initialise in AWS region
    gateway = ApiGateway(src,
                        # regions=EXTRA_REGIONS,
                        regions=["eu-central-1", "eu-west-1", "eu-west-2"],
                        access_key_id=f"{aws_access_key_id}",
                        access_key_secret=f"{aws_secret_access_key}")
    gateway.start(force=True)
    # Assign gateway to session
    session=requests.Session()
    session.mount(src, gateway)
    # Send request (IP will be randomised)
    response=session.get(src)
    print("connection_status_code: ", response.status_code, " | assigned_ip_address: ", response.text)
    # Delete gateways
    gateway.shutdown()
    time.sleep(1)
