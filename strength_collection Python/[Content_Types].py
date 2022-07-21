from typing import List


class Default:
    content_type: str
    extension: str

    def __init__(self, content_type: str, extension: str) -> None:
        self.content_type = content_type
        self.extension = extension


class Override:
    content_type: str
    part_name: str

    def __init__(self, content_type: str, part_name: str) -> None:
        self.content_type = content_type
        self.part_name = part_name


class Types:
    default: List[Default]
    override: List[Override]
    xmlns: str

    def __init__(self, default: List[Default], override: List[Override], xmlns: str) -> None:
        self.default = default
        self.override = override
        self.xmlns = xmlns


class Welcome4:
    types: Types

    def __init__(self, types: Types) -> None:
        self.types = types
