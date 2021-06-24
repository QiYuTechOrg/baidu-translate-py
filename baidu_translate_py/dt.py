from typing import List, Optional

from pydantic import BaseModel, Field

__all__ = ["BaiduTranslateResult", "BaiduTranslateItem"]


class BaiduTranslateItem(BaseModel):
    src: str = Field(..., title="源文本")
    dst: str = Field(..., title="翻译之后的文本")


class BaiduTranslateResult(BaseModel):
    from_: str = Field(..., title="源语言", alias="from")
    to: str = Field(..., title="目标语言")
    trans_result: Optional[List[BaiduTranslateItem]] = Field(None, title="翻译结果")
