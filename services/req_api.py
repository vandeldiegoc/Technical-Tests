import json
from fastapi.encoders import jsonable_encoder
import requests
from requests import adapters
from  requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

adapter = HTTPAdapter(max_retries=3)


class MyException(Exception):
   def __init__(self, error_code, error_msg):
       self.error_code = error_code
       self.error_msg = error_msg

def req_picture():
    with requests.Session() as s:
        s.mount('https://dog.ceo/api/breeds/image/random', adapter)
        try:
            r = s.get('https://dog.ceo/api/breeds/image/random')
            if r.status_code != 200:
                return None
        except ConnectionError as ce:
            print(ce)
            return(None)

        picture = r.text
        picture = picture.split('"')[3]
    return picture

""" import httpx
from typing import Dict


async def reapi():
    pokemon_url = 'https://dog.ceo/api/breeds/image/random'

    async with httpx.AsyncClient() as client:

        resp = await client.get(pokemon_url)
        resp = resp.json()
        return resp['messege']
 """
