import hashlib
import secrets

import requests

from .dt import BaiduTranslateResult

__all__ = ["BaiduTranslateApi"]


class BaiduTranslateApi(object):
    """
    百度翻译API
    """

    def __init__(self, app_id: str, secret: str):
        """
        登录百度开发平台之后
        从这个页面获取: https://fanyi-api.baidu.com/api/trans/product/desktop

        :param app_id: 应用名称
        :param secret: 密钥
        """
        self._app_id = app_id
        self._secret = secret
        self._session = requests.Session()

    def common_translate(
        self, q: str, dst_lang: str, src_lang: str = "auto"
    ) -> BaiduTranslateResult:
        """
        通用翻译文档: https://fanyi-api.baidu.com/doc/21

        如果您遇到: INVALID_CLIENT_IP 请把您的 IP 地址加入到 IP 地址白名单中

        :param q: 翻译的内容 [6000个字节以内，一般为 2000 个汉字]
        :param dst_lang: 目标语言
        :param src_lang: 源语言
        :except ValidationError
        :return:
        """
        url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
        salt = secrets.token_urlsafe(16)

        resp = self._session.post(
            url,
            data={
                "q": q,
                "from": src_lang,
                "to": dst_lang,
                "appid": self._app_id,
                "salt": salt,
                "sign": self._compute_sign(q, salt=salt),
            },
        )
        return BaiduTranslateResult(**resp.json())

    def _compute_sign(self, q: str, salt: str) -> str:
        """
        签名生成方法

        签名是为了保证调用安全，使用 MD5 算法生成的一段字符串，生成的签名长度为 32 位，签名中的英文字符均为小写格式。
        生成方法：

        Step1. 将请求参数中的 APPID(appid)， 翻译 query(q，注意为UTF-8编码)，随机数(salt)，以及平台分配的密钥(可在管理控制台查看) 按照 appid+q+salt+密钥的顺序拼接得到字符串 1。
        Step2. 对字符串 1 做 md5 ，得到 32 位小写的 sign。

        注：
        1. 待翻译文本（q）需为 UTF-8 编码；
        2. 在生成签名拼接 appid+q+salt+密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode；
        3.如遇到报 54001 签名错误，请检查您的签名生成方法是否正确，在对 sign 进行拼接和加密时，q 不需要做 URL encode，很多开发者遇到签名报错均是由于拼接 sign 前就做了 URL encode；
        4.在生成签名后，发送 HTTP 请求时，如果将 query 拼接在 url 上，需要对 query 做 URL encode。

        :return: str
        """
        data = f"{self._app_id}{q}{salt}{self._secret}"
        md5 = hashlib.md5(data.encode("utf-8"))
        digest = md5.hexdigest()
        return digest.lower()
