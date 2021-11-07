import requests
from  requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
#from services.Celery import app_celery

adapter = HTTPAdapter(max_retries=3)


#@app_celery.task
def req_picture():
    with requests.Session() as s:
        s.mount('https://dog.ceo/api/breeds/image/random', adapter)
        try:
            r = s.get('https://dog.ceo/api/breeds/image/random')
            if r.status_code != 200:
                return None
        except ConnectionError as ce:
            return(None)

        picture = r.text
        picture = picture.split('"')[3]
    return picture


def post_file(file):
    res = requests.post(
        'https://gttb.guane.dev/api/files', files={'file': file}
    )
    return res.json()