import requests

from .dt import NiuTranslateResult, NiuTranslateArgs

__all__ = ["NiuTranslationApi"]


class NiuTranslationApi(object):
    """
    小牛翻译
    官方网站: https://niutrans.com/
    """

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._session = requests.Session()

    def text_translate(self, args: NiuTranslateArgs) -> NiuTranslateResult:
        """
        文本翻译
        文档: https://niutrans.com/documents/develop/develop_text/free#accessMode
        :param args:
        :return:
        """
        if args.free:
            url = "https://free.niutrans.com/NiuTransServer/translation"
        else:
            url = "https://api.niutrans.com/NiuTransServer/translation"
        return self._do_translate(url, args)

    def xml_translate(self, args: NiuTranslateArgs) -> NiuTranslateResult:
        """
        XML格式翻译接口
        文档: https://niutrans.com/documents/develop/develop_XML/free#accessMode
        :param args: 翻译参数
        :return:
        """
        if args.free:
            url = "https://free.niutrans.com/NiuTransServer/translationXML"
        else:
            url = "https://api.niutrans.com/NiuTransServer/translationXML"

        return self._do_translate(url, args)

    def _do_translate(self, url: str, args: NiuTranslateArgs) -> NiuTranslateResult:
        resp = self._session.post(
            url,
            data={
                "from": args.src_lang,
                "to": args.dst_lang,
                "apikey": self._api_key,
                "src_text": args.src_text,
                "dictNo": args.dict_no,
                "memoryNo": args.memory_no,
            },
        )
        return NiuTranslateResult(**resp.json())
