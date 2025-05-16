# DESAFIO 01 - SEMEQ

## INSTALL

<h1 align="center">
  API Proxy Portal Stream - Documentation
</h1>

<h2 align="center">
  Information
</h2>

<p align="center">
    This documentation has been created to explain about the endpoints.
</p>


- **Python**
- **FastAPI**
- **httpx**
- **pydantic**
- **Uvicorn**
- **python-dotenv**
---

### Install

You need to create a file with the extension **.env** in the root of the project to store the external url so as not to be exposed.

```env
URL_BASE="https:..."
````


```bash
git clone git@github.com:HelterXavier/portalstream_api.git

python -m venv venv

venv\Scripts\Activate

pip install -r requirements.txt

pip install uvicorn

pip freeze > requirements.txt

uvicorn app.main:app --reload
```



### URL base

**URL:**  *http://127.0.0.1:8000/*

<hr style="border: none; height:  1px; background-color: gray;">

## POST

| `POST - http://127.0.0.1:8000/token`

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

<hr style="border: none; height:  1px; background-color: gray;">
<br>

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

<hr style="border: none; height:  1px; background-color: gray;">


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
    },
    {
      "id": 20397,
      "name": "PED PORTAL",
      "corporation": 54
    },
    {
      "id": 10441,
      "name": "PORTAL DAS ROSAS",
      "corporation": 54
    },
    {
      "id": 20439,
      "name": "SEMEQ MOBILE",
      "corporation": 54
    },
    {
      "id": 20363,
      "name": "SMQ SAINT LOUIS STL",
      "corporation": 54
    },
    {
      "id": 20446,
      "name": "TEST 20250416",
      "corporation": 708
    },
    {
      "id": 20449,
      "name": "TEST ALTEON",
      "corporation": 708
    },
    {
      "id": 20450,
      "name": "TESTE 20250501",
      "corporation": 708
    },
    {
      "id": 20442,
      "name": "TESTE-DO-BOREL",
      "corporation": 54
    },
    {
      "id": 20431,
      "name": "TESTE MIGRACAO",
      "corporation": 54
    },
    {
      "id": 20443,
      "name": "TESTE-ÓLEO",
      "corporation": 706
    },
    {
      "id": 20447,
      "name": "TEST GABRIEL",
      "corporation": 708
    },
    {
      "id": 20448,
      "name": "TEST VITINHO",
      "corporation": 708
    },
    {
      "id": 20398,
      "name": "TREINAMENTO",
      "corporation": 54
    }
  ],
  "notification": []
}
```

<hr style="border: none; height:  1px; background-color: gray;">


| `GET - http://127.0.0.1:8000/implantation/mobile/tree?site=ID`

**Send Params**
- Access Token: Bearer Access

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


| `GET - http://127.0.0.1:8000/implantation/mobile/info?site=ID`

**Send Params**
- Access Token: Bearer Access

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

<hr style="border: none; height:  1px; background-color: gray;">

| `GET - http://127.0.0.1:8000/implatation/mobile/info`

**Send Params**
- Access Token: Bearer Access

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
        },
```


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
