class MwcoreProperties:
    content_type: str
    content_type_friendly_name: str
    matlab_release: str
    xmlns: str

    def __init__(self, content_type: str, content_type_friendly_name: str, matlab_release: str, xmlns: str) -> None:
        self.content_type = content_type
        self.content_type_friendly_name = content_type_friendly_name
        self.matlab_release = matlab_release
        self.xmlns = xmlns


class Welcome2:
    mwcore_properties: MwcoreProperties

    def __init__(self, mwcore_properties: MwcoreProperties) -> None:
        self.mwcore_properties = mwcore_properties
