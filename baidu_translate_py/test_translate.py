import json
import os

from .baidu_translate import BaiduTranslateApi


def load_secrets() -> dict:
    with open(os.path.join(os.path.dirname(__file__), "../secrets.json")) as fp:
        return json.load(fp)


def test_baidu_translate():
    trans = BaiduTranslateApi(**load_secrets())
    resp = trans.common_translate(q="百度翻译测试。", dst_lang="en")
    print(resp)
