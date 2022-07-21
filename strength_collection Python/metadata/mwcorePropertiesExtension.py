from uuid import UUID


class MwcoreProperties:
    uuid: UUID
    xmlns: str

    def __init__(self, uuid: UUID, xmlns: str) -> None:
        self.uuid = uuid
        self.xmlns = xmlns


class Welcome3:
    mwcore_properties: MwcoreProperties

    def __init__(self, mwcore_properties: MwcoreProperties) -> None:
        self.mwcore_properties = mwcore_properties
