import requests
from urllib.parse import urljoin
from config import BASE_URL, TIMEOUT
from utils.logger import get_logger
logger = get_logger(__name__)
from config import BASE_URL,TIMEOUT
class ApiClient:
        def __init__(self):
                self.base_url = BASE_URL
                self.session = requests.Session()
                self.session.headers.update({"Content_Type":"application/json"})
        def get(self,path,**kwargs):
                url = urljoin(self.base_url,path)
                logger.info(f"GET {url}")
                resp =  self.session.get(url, timeout = TIMEOUT, **kwargs)
                logger.info(f"Response:{resp.status_code}")
                return resp

        def post(self,path,data,**kwargs):
                url = urljoin(self.base_url,path)
                logger.info(f"POST {url}")
                resp = self.session.post(url, json=data, timeout = TIMEOUT, **kwargs)
                logger.info(f"Response:{resp.status_code}")
                return resp


