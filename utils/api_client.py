"""封装HTTP请求客户端，统一管理GET/POST、Token、日志"""
import requests
from urllib.parse import urljoin
from utils.logger import get_logger
from utils.config_loader import CONFIG

logger = get_logger(__name__)

class ApiClient:
        def __init__(self):
                self.base_url = CONFIG["base_url"]
                self.session = requests.Session()
                self.session.headers.update({"Content-Type":"application/json"})

        def set_token(self, token):
                self.session.headers.update({"Authorization": f"Bearer {token}"})

        def get(self,path,**kwargs): #定义get方法，path是路径，kwargs是额外参数
                url = urljoin(self.base_url,path) #拼完整URL:根地址+路径
                logger.info(f"GET {url}")#记录日志：正准备请求哪个地址
                resp =  self.session.get(url, timeout = CONFIG["timeout"], **kwargs) #发GET请求，超时时间来自配置
                logger.info(f"Response:{resp.status_code}")#记录日志：服务器返回的状态码
                return resp #返回响应结果

        def post(self,path,data,**kwargs):#path：路径，data=要发的数据，kwargs：额外的参数
                url = urljoin(self.base_url,path)#拼完整URL
                logger.info(f"POST {url}")#记日志：准备POST到哪个地址
                resp = self.session.post(url, json=data, timeout = CONFIG["timeout"], **kwargs)#发POST请求，把data转换为JSON发给服务器
                logger.info(f"Response:{resp.status_code}")#记日志：服务器返回的状态码
                return resp#返回相应结果


