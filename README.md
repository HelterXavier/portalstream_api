# DESAFIO 01 - SEMEQ

<h1 align="center">
  API Proxy Portal Stream - Documentation
</h1>

<p align="center">
    This documentation was created to explain the endpoint created for the SEMEQ challenge
</p>


## Install Project


```bash

# API
git clone git@github.com:HelterXavier/portalstream_api.git

python -m venv venv

venv\Scripts\Activate

pip install -r requirements.txt

pip install uvicorn

pip freeze > requirements.txt
```


```bash
# FRONT END REACT JS
git clone git@github.com:HelterXavier/front_end_portalstream.git

Install Node.js -> https://nodejs.org/pt

npm install

npm run dev
```

### File .env with URL_BASE at the root
```env
URL_BASE="https:..."
```

## Run Project
```bash
uvicorn app.main:app --reload
```

## URL base
**URL BASE:**  *http://127.0.0.1:8000/*

<hr style="border: none; height:  1px; background-color: gray;">


## Libraries installed in the project

Below are the libraries used in API construction, installed with `pip`:
```bash
pip install fastapi uvicorn httpx python-dotenv pydantic
```

- **FASTAPI** ➡️ Framework to create APIs RESTful with Python. Create routes and endpoints;
- **HTTPX** ➡️ Make external HTTP requests to another API;
Need to create a file with the extension **.env** in the root of the project to store the external url so as not to be exposed;
- **PYDANTIC** ➡️ To create models (SCHEMAS) that validate the data received and sent from the API;
- **UVICORN** ➡️ Run local server FASTAPI: *uvicorn app.main:app --reload*;
- **PYTHON-DOTENV** ➡️ Loads environment variables. Used to avoid exposing information such as passwords, user, urls etc.


## AUTH TOKEN

`POST - http://127.0.0.1:8000/token`

**Request Body Example:**

```json
{
    "username": "username",
    "password": "username"
}
```

**Response:**

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMzc5MDM2NSwiaWF0IjoxNzAzNzAzOTY1LCJqdGkiOiI1NzEzNzE0N2UxZjI0MzY1ODM2OTdmMWUxNWFlZTNmOSIsInVzZXJfaWQiOjIxMn0JalnbPJf-7U9QpbLJfi2a4LwwLRVP0OKhSp_RtdgyY",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNzA0MjY1LCJpYXQiOjE3MDM3MDM5NjUsImp0aSI6IjdmOTZjZDExMzc4MDQzZDY5ZmRkZDgxYjliMjRmNDFhIiwidXNlcl9pZCI6MjEyfQnXPYekgNFsRSUdMrw3giB7pF21-KA5iOsTIHkxP5NLM"
}
```
## Print Insomnia

<img src="docs/token.png" width="900"/>

<hr style="border: none; height:  1px; background-color: gray;">
<br>

## VERIFY TOKEN

| `POST - http://127.0.0.1:8000/token/verify`

**Request Body Example:**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NDIwNTA2LCJpYXQiOjE3NDc0MTkzMDYsImp0aSI6ImU5MjQ2ZmUwNmY1MTRjYWRhZjMyN2NiODc5ZWQzOTgyIiwidXNlcl9pZCI6NTE5fQ.rx-my_Zmb3fZlYYDRQK3cfadXCgKuDxFr1A6NYRFGSo"
}
```

**Response:**

```json
CODE 200
{}
```

## Print Insomnia
<img src="docs/verify_token.png" width="900"/>

<hr style="border: none; height:  1px; background-color: gray;">


## REFRESH TOKEN

| `POST - http://127.0.0.1:8000/token/refresh`

**Request Body Example:**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NzY3ODUwNiwiaWF0IjoxNzQ3NDE5MzA2LCJqdGkiOiI5OTU1ZmQ4ODA2Yzg0MzI1OTQ1NGJhZGIxNWZjNTIzNCIsInVzZXJfaWQiOjUxOX0.2DF0m4QxQnmRRmj3PZ2vq8X60Hk2m3jNobegp-FAt9Y"
}
```



**Response:**

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NDIwNjQ2LCJpYXQiOjE3NDc0MTkzMDYsImp0aSI6IjNjMmQxN2I3MjA5MjRhZGE5ZWZjOTg4M2UxMjQwZjk4IiwidXNlcl9pZCI6NTE5fQ.QKd938HZbPmNbXiGerRI97ZnQeSED_2cTo4ZvFYBtag"
}
```

## Print Insomnia

<img src="docs/refresh_token.png" width="900"/>

<hr style="border: none; height:  1px; background-color: gray;">


## GET

| `GET - http://127.0.0.1:8000/usercorp`

**Send Params**
- Access Token: Bearer Access

**Response:**

```json
{
  "user": {
    "id": 519,
    "username": "dev_intern",
    "first_name": "Internship",
    "last_name": "Challenge",
    "email": "pedro.martins@semeq.com"
  },
  "corporation": [
    {
      "id": 54,
      "name": "SEMEQ"
    },
    {
      "id": 706,
      "name": "TESTE - ÓLEO"
    },
    {
      "id": 708,
      "name": "VALIDATION - OIL"
    }
  ],
  "sites": [
    {
      "id": 20432,
      "name": "AMBEV GU MIGRACAO",
      "corporation": 54
    },
    {
      "id": 20433,
      "name": "GERDAU JACKSON",
      "corporation": 54
    },...
  ],
  "notification": []
}
```

## Print Insomnia
<img src="docs/get_usercorp.png" width="900"/>

<hr style="border: none; height:  1px; background-color: gray;">


| `GET - http://127.0.0.1:8000/implantation/mobile/tree?site=ID`

**Send Params**
- Access Token: Bearer Access
- Sites -> ID

**Response:**

```json
  {
	"id": 10441,
	"name": "PORTAL DAS ROSAS",
	"revision": 28,
	"tree": [
		{
			"id": 2016775,
			"asset_type": 17,
			"group": "motor",
			"status": true,
			"name": "TESTE",
			"tag": null,
			"level": 3,
			"order": 1,
			"parent": 2016771,
			"site": 10441
		},
		{
			"id": 2015883,
			"asset_type": 17,
			"group": "motor",
			"status": true,
			"name": "TESTE-5",
			"tag": null,
			"level": 3,
			"order": 5,
			"parent": 2015878,
			"site": 10441
		},
  ]}
```
## Print Insomnia
<img src="docs/implantition_tree.png" width="900"/>

| `GET - http://127.0.0.1:8000/implantation/mobile/info?site=ID`

**Send Params**
- Access Token: Bearer Access
- Sites -> ID

**Response:**

```json
  {
  "asset_info": [
    {
      "devices": [
        {
          "device_id": 14138,
          "serial_number": "042",
          "device_type_id": 1,
          "directions": [
            "X",
            "Y",
            "Z"
          ],
          "services": [
            1,
            2
          ]
        },
        {
          "device_id": 14139,
          "serial_number": "043",
          "device_type_id": 1,
          "directions": [
            "X",
            "Y",
            "Z"
          ],
          "services": [
            1,
            2
          ]
        }...
```

## Print Insomnia
<img src="docs/implantition_info_site.png" width="900"/>



<hr style="border: none; height:  1px; background-color: gray;">

| `GET - http://127.0.0.1:8000/implatation/mobile/static`

**Send Params**
- Access Token: Bearer Access

**Response:**

```json

{
  "asset_group": [
    {
      "id": "motor",
      "desc": "MOTOR"
    },
    {
      "id": "gearbox",
      "desc": "GEARBOX"
    },
    {
      "id": "compressor",
      "desc": "COMPRESSOR"
    }...
```

## Print Insomnia
<img src="docs/implantation_static.png" width="900"/>

<hr style="border: none; height:  1px; background-color: gray;">

| `GET - http://127.0.0.1:8000/implatation/mobile/static/get_lubricants`

**Send Params**
- Access Token: Bearer Access

**Response:**

```json

{
  "asset_group": [
    {
      "id": "motor",
      "desc": "MOTOR"
    },
    {
      "id": "gearbox",
      "desc": "GEARBOX"
    },
    {
      "id": "compressor",
      "desc": "COMPRESSOR"
    },
    {
      "id": "pillow block",
      "desc": "PILLOW BLOCK"
    },
    {
      "id": "fan",
      "desc": "FAN"
    },...
```

## Print Insomnia
<img src="docs/implantation_get_lubricants.png" width="900"/>
