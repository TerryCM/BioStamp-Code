from enum import Enum
from typing import Optional, List


class Prefix(Enum):
    W = "w"


class WVal(Enum):
    CODE = "code"
    HEADING = "heading"
    LEFT = "left"


class Jc:
    w_val: WVal
    prefix: Prefix

    def __init__(self, w_val: WVal, prefix: Prefix) -> None:
        self.w_val = w_val
        self.prefix = prefix


class SectPR:
    prefix: Prefix

    def __init__(self, prefix: Prefix) -> None:
        self.prefix = prefix


class PPR:
    p_style: Optional[Jc]
    jc: Optional[Jc]
    prefix: Prefix
    sect_pr: Optional[SectPR]

    def __init__(self, p_style: Optional[Jc], jc: Optional[Jc], prefix: Prefix, sect_pr: Optional[SectPR]) -> None:
        self.p_style = p_style
        self.jc = jc
        self.prefix = prefix
        self.sect_pr = sect_pr


class TClass:
    prefix: Prefix
    text: Optional[str]
    cdata: Optional[str]

    def __init__(self, prefix: Prefix, text: Optional[str], cdata: Optional[str]) -> None:
        self.prefix = prefix
        self.text = text
        self.cdata = cdata


class R:
    t: TClass
    prefix: Prefix

    def __init__(self, t: TClass, prefix: Prefix) -> None:
        self.t = t
        self.prefix = prefix


class P:
    p_pr: PPR
    r: Optional[R]
    prefix: Prefix

    def __init__(self, p_pr: PPR, r: Optional[R], prefix: Prefix) -> None:
        self.p_pr = p_pr
        self.r = r
        self.prefix = prefix


class Body:
    p: List[P]
    prefix: Prefix

    def __init__(self, p: List[P], prefix: Prefix) -> None:
        self.p = p
        self.prefix = prefix


class Document:
    body: Body
    xmlns_w: str
    prefix: Prefix

    def __init__(self, body: Body, xmlns_w: str, prefix: Prefix) -> None:
        self.body = body
        self.xmlns_w = xmlns_w
        self.prefix = prefix


class Welcome5:
    document: Document

    def __init__(self, document: Document) -> None:
        self.document = document
