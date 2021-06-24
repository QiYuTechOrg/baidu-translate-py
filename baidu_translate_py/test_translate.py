import json
import os

from .baidu_translate import BaiduTranslateApi
from .dt import NiuTranslateArgs
from .niu_translate import NiuTranslationApi


def load_baidu_secrets() -> dict:
    with open(os.path.join(os.path.dirname(__file__), "../baidu_secrets.json")) as fp:
        return json.load(fp)


def test_baidu_translate():
    trans = BaiduTranslateApi(**load_baidu_secrets())
    test_q = """
52001 表示请求超时，请检查按照如下步骤检查您的签名生成方法是否正确：
1. 您传入的 query 长度是否超长？建议将原文采用"\\n"分段请求；
2. 如间隔一段时间再次请求，是否可正常返回结果？如果不可以，请检查您所填写的原文或译文语种是否在支持的语种列表里。
    """
    resp = trans.common_translate(q=test_q, dst_lang="en")
    print(resp)


def load_niu_apikey() -> dict:
    with open(os.path.join(os.path.dirname(__file__), "../niu_apikey.json")) as fp:
        return json.load(fp)


def test_niu_xml_translation():
    trans = NiuTranslationApi(**load_niu_apikey())
    src_text = """
小牛翻译<p style="color: red">很不错</p>。
"""
    args = NiuTranslateArgs(src_text=src_text, src_lang="zh", dst_lang="en")
    xml_resp = trans.xml_translate(args=args)
    text_resp = trans.text_translate(args=args)
    print(xml_resp, text_resp)
