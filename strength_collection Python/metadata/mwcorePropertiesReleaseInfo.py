class MathWorksVersionInfo:
    version: str
    release: str
    description: str
    date: str
    checksum: int

    def __init__(self, version: str, release: str, description: str, date: str, checksum: int) -> None:
        self.version = version
        self.release = release
        self.description = description
        self.date = date
        self.checksum = checksum


class Welcome6:
    math_works_version_info: MathWorksVersionInfo

    def __init__(self, math_works_version_info: MathWorksVersionInfo) -> None:
        self.math_works_version_info = math_works_version_info
