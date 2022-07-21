from typing import List


class Relationship:
    id: str
    target: str
    type: str

    def __init__(self, id: str, target: str, type: str) -> None:
        self.id = id
        self.target = target
        self.type = type


class Relationships:
    relationship: List[Relationship]
    xmlns: str

    def __init__(self, relationship: List[Relationship], xmlns: str) -> None:
        self.relationship = relationship
        self.xmlns = xmlns


class Welcome10:
    relationships: Relationships

    def __init__(self, relationships: Relationships) -> None:
        self.relationships = relationships
