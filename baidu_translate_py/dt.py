from typing import List, Optional

from pydantic import BaseModel, Field

__all__ = [
    "BaiduTranslateResult",
    "BaiduTranslateItem",
    "NiuTranslateResult",
    "NiuTranslateArgs",
]


class BaiduTranslateItem(BaseModel):
    src: str = Field(..., title="源文本")
    dst: str = Field(..., title="翻译之后的文本")


class BaiduTranslateResult(BaseModel):
    from_: str = Field(..., title="源语言", alias="from")
    to: str = Field(..., title="目标语言")
    trans_result: Optional[List[BaiduTranslateItem]] = Field(None, title="翻译结果")


class NiuTranslateResult(BaseModel):
    from_: str = Field(..., title="源语言", alias="from")
    to: str = Field(..., title="目标语言")
    tgt_text: str = Field(..., title="翻译结果")


class NiuTranslateArgs(BaseModel):
    src_text: str = Field(..., title="目标文本")
    src_lang: str = Field(..., title="源语言")
    dst_lang: str = Field(..., title="目标语言")
    dict_no: str = Field("", title="")
    memory_no: str = Field("", title="")
    free: bool = Field(True, title="使用免费接口")
