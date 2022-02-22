## Debian Systems based

## Upgrading pip to install new packages.
pip3 install --upgrade pip

## Checking the installed python packages
pip list

## Installing python3 virtual environment
sudo apt-get install python3-venv
pip install virtualenv

## Setting up the virtual environment and install fastapi
python3 -m venv fastapienv
. fastapienv/bin/activate
deactivate
pip3 install fastapi[all]

## Comparison flask vs fast API

ab -n 100 -c 10 http://127.0.0.1:5000/api/v1/bluetooth/settings
ab -n 100 -c 10 http://127.0.0.1:8000/api/v1/bluetooth/settings



## Install sqlalchemy
pip install sqlalchemy


## JWT - JSON Web token

JWT should be used when dealing with authorization

JWT is a great way for information to be exchanged between the server and a client.

## JSON WEB Token structure

Header:(a). Payload: (b), Signature: (c)

# JWT Header
 Algorithm for signing
 tp the specific type  of token

 {
     "alg": "HS256"
     "typ" "JWT"
 }

JWT header is encoded using Base64to create the first part of the JWT.

JWT consists of header, payload and signature.

JWT header - alg, type

JWT payload - sub, name, given_name, email, admin.

JWT signature - encoded header, encoded payload, secret


# Password encyrption

pip install "passlib[bcrypt]"

#JWT package 

pip install "python-jose[cryptography]"

# Run uvicorn on a different port number 
uvicorn  auth:app --reload --port 9000

# Connecting app to Postgresql 
 pip install psycopg2-binary


 # Connecting app to MySQL
 pip install pymysql

 # JINJA template.

 pip install aiofiles 
pip install jinja2

