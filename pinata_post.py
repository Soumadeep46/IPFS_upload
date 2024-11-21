import requests
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_pinata(filepath, jwt_token):
    url ="https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers={'Authorization': f'Bearer {jwt_token}'}

    with open(filepath,'rb') as file:
        response= requests.post(url,files={'file':file}, headers=headers)
        return response.json()
    
PINATA_JWT_TOKEN = os.getenv('PINATA_JWT_TOKEN')



FILE_PATH= 'GOT.jpg'

print(upload_to_pinata(FILE_PATH,PINATA_JWT_TOKEN))