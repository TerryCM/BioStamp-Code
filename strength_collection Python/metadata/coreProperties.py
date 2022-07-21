from datetime import datetime


class Created:
    xsi_type: str
    prefix: str
    text: datetime

    def __init__(self, xsi_type: str, prefix: str, text: datetime) -> None:
        self.xsi_type = xsi_type
        self.prefix = prefix
        self.text = text


class CoreProperties:
    created: Created
    modified: Created
    xmlns_cp: str
    xmlns_dc: str
    xmlns_dcmitype: str
    xmlns_dcterms: str
    xmlns_xsi: str
    prefix: str

    def __init__(self, created: Created, modified: Created, xmlns_cp: str, xmlns_dc: str, xmlns_dcmitype: str, xmlns_dcterms: str, xmlns_xsi: str, prefix: str) -> None:
        self.created = created
        self.modified = modified
        self.xmlns_cp = xmlns_cp
        self.xmlns_dc = xmlns_dc
        self.xmlns_dcmitype = xmlns_dcmitype
        self.xmlns_dcterms = xmlns_dcterms
        self.xmlns_xsi = xmlns_xsi
        self.prefix = prefix


class Welcome3:
    core_properties: CoreProperties

    def __init__(self, core_properties: CoreProperties) -> None:
        self.core_properties = core_properties
