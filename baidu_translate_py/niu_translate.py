import requests

from .dt import NiuTranslateResult

__all__ = ["NiuTranslationApi"]


class NiuTranslationApi(object):
    """
    小牛翻译
    官方网站: https://niutrans.com/
    """

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._session = requests.Session()

    def xml_translate(
        self,
        src_text: str,
        src_lang: str,
        dst_lang: str,
        dict_no: str = "",
        memory_no: str = "",
        free: bool = True,
    ) -> NiuTranslateResult:
        """
        XML格式翻译接口

        文档: https://niutrans.com/documents/develop/develop_XML/free#accessMode

        :param src_text: 待翻译字符串 该字段必须为UTF-8编码
        :param src_lang: 源语言：待翻译文本语种参数
        :param dst_lang: 目标语言：翻译目标语种参数
        :param dict_no: 设置术语词典子库ID，缺省值为空
        :param memory_no: 设置翻译记忆子库ID，缺省值为空
        :param free: 是否使用免费接口
        :return:
        """
        if free:
            url = "https://free.niutrans.com/NiuTransServer/translationXML"
        else:
            url = "https://api.niutrans.com/NiuTransServer/translationXML"

        resp = self._session.post(
            url,
            data={
                "from": src_lang,
                "to": dst_lang,
                "apikey": self._api_key,
                "src_text": src_text,
                "dictNo": dict_no,
                "memoryNo": memory_no,
            },
        )
        return NiuTranslateResult(**resp.json())
