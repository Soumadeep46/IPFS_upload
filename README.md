# IPFS_upload
This project demonstrates how to upload and retrieve files from IPFS using the Pinata API and Python. It leverages the Pinata API for seamless interaction with the IPFS network and uses JWT tokens for authentication.

Features
File Upload: Upload images to IPFS using the Pinata API.
Data Retrieval: Retrieve uploaded file details from Pinata.
Environment Variable Security: Securely manage sensitive information, like JWT tokens, using a .env file.
Tech Stack
Python
Requests (HTTP requests handling)
Pinata API (for IPFS integration)
dotenv (for environment variable management)
Prerequisites
Python installed (3.7 or later).
A Pinata account with API access.
Pinata JWT token.
Setup
Clone the Repository
bash
Copy code
git clone https://github.com/your_username/DecentralizedPhotoUploader.git  
cd DecentralizedPhotoUploader  
Install Required Packages
bash
Copy code
pip install -r requirements.txt  
Create a .env File
Create a .env file in the project directory and add your Pinata JWT token:

env
Copy code
PINATA_JWT_TOKEN=your_jwt_token_here  
How to Use
1. Upload Files to IPFS
Use the python_post.py script to upload files to IPFS:

bash
Copy code
python python_post.py  
Update the FILE_PATH variable in python_post.py with the path of the file you want to upload.
The script will return the IPFS hash and Pinata metadata for the uploaded file.
2. Retrieve Uploaded Data
Use the python_get.py script to retrieve details of uploaded files:

bash
Copy code
python python_get.py  
The script will return the list of pinned files associated with your Pinata account.
File Structure
plaintext
Copy code
DecentralizedPhotoUploader/  
├── python_post.py      # Script for uploading files to IPFS  
├── python_get.py       # Script for retrieving uploaded file data  
├── .env                # File to store JWT token securely  
├── requirements.txt    # Python dependencies  
└── README.md           # Project documentation  
Sample Output
Uploading a File (python_post.py)
json
Copy code
{
    "IpfsHash": "QmXexampleHash123",
    "PinSize": 1024,
    "Timestamp": "2024-11-20T12:00:00Z"
}  
Retrieving Files (python_get.py)
json
Copy code
{
    "count": 1,
    "rows": [
        {
            "ipfs_pin_hash": "QmXexampleHash123",
            "date_pinned": "2024-11-20T12:00:00Z"
        }
    ]
}  
Future Enhancements
Add support for batch uploads.
Integrate a simple frontend for user-friendly interaction.
Extend functionality to pin metadata along with files.
License
This project is licensed under the MIT License.

