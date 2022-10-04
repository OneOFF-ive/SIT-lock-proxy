import mitmproxy.http
from config import config


class Control:
    def __init__(self, conf: dict):
        self.__config = conf

    # 拦截请求
    def request(self, flow: mitmproxy.http.HTTPFlow):
        method: str = flow.request.query.get('Method')
        c_no: str = flow.request.query.get('KaHao')

        baseUrl: str = f"http://{self.__config['host']}:{self.__config['port']}"
        if method == "ShuaKaLiuCheng":
            flow.request.url = baseUrl+"/skip_reg?c_no=" + c_no
        elif method == "SaveRemoteOpenDoor":
            flow.request.url = baseUrl + "/open_door?c_no=" + c_no


addons = [
    Control(config)
]
