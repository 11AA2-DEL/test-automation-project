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
        def get(self,path,**kwargs): #定义get方法，path是路径，kwargs是额外参数
                url = urljoin(self.base_url,path) #拼完整URL:根地址+路径
                logger.info(f"GET {url}")#记录日志：正准备请求哪个地址
                resp =  self.session.get(url, timeout = TIMEOUT, **kwargs) #发GET请求，超时时间来自配置
                logger.info(f"Response:{resp.status_code}")#记录日志：服务器返回的状态码
                return resp #返回响应结果

        def post(self,path,data,**kwargs):#path：路径，data=要发的数据，kwargs：额外的参数
                url = urljoin(self.base_url,path)#拼完整URL
                logger.info(f"POST {url}")#记日志：准备POST到哪个地址
                resp = self.session.post(url, json=data, timeout = TIMEOUT, **kwargs)#发POST请求，把data转换为JSON发给服务器
                logger.info(f"Response:{resp.status_code}")#记日志：服务器返回的状态码
                return resp#返回相应结果


