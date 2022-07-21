from enum import Enum
from typing import Optional, List


class SplitterState:
    proportion: str

    def __init__(self, proportion: str) -> None:
        self.proportion = proportion


class MetaData:
    evaluation_state: str
    layout_state: str
    output_status: str
    splitter_state: SplitterState

    def __init__(self, evaluation_state: str, layout_state: str, output_status: str, splitter_state: SplitterState) -> None:
        self.evaluation_state = evaluation_state
        self.layout_state = layout_state
        self.output_status = output_status
        self.splitter_state = splitter_state


class TypeEnum(Enum):
    ARRAY = "array"


class LineNumbers:
    element: Optional[int]
    type: TypeEnum

    def __init__(self, element: Optional[int], type: TypeEnum) -> None:
        self.element = element
        self.type = type


class TruncationInfo:
    was_truncated_mid_line: bool
    was_truncated_at_line_break: bool

    def __init__(self, was_truncated_mid_line: bool, was_truncated_at_line_break: bool) -> None:
        self.was_truncated_mid_line = was_truncated_mid_line
        self.was_truncated_at_line_break = was_truncated_at_line_break


class OutputData:
    name: Optional[str]
    value: Optional[str]
    truncation_info: Optional[TruncationInfo]
    rows: Optional[int]
    columns: Optional[int]
    text: Optional[str]
    error_type: Optional[str]

    def __init__(self, name: Optional[str], value: Optional[str], truncation_info: Optional[TruncationInfo], rows: Optional[int], columns: Optional[int], text: Optional[str], error_type: Optional[str]) -> None:
        self.name = name
        self.value = value
        self.truncation_info = truncation_info
        self.rows = rows
        self.columns = columns
        self.text = text
        self.error_type = error_type


class OutputArrayElement:
    type: str
    output_data: OutputData
    line_numbers: LineNumbers

    def __init__(self, type: str, output_data: OutputData, line_numbers: LineNumbers) -> None:
        self.type = type
        self.output_data = output_data
        self.line_numbers = line_numbers


class OutputArray:
    element: List[OutputArrayElement]
    type: TypeEnum

    def __init__(self, element: List[OutputArrayElement], type: TypeEnum) -> None:
        self.element = element
        self.type = type


class Code:
    section_break: bool
    end_of_section: bool
    region_number: int

    def __init__(self, section_break: bool, end_of_section: bool, region_number: int) -> None:
        self.section_break = section_break
        self.end_of_section = end_of_section
        self.region_number = region_number


class RegionArrayElement:
    code: Code
    start_line: int
    end_line: int
    output_indexes: LineNumbers

    def __init__(self, code: Code, start_line: int, end_line: int, output_indexes: LineNumbers) -> None:
        self.code = code
        self.start_line = start_line
        self.end_line = end_line
        self.output_indexes = output_indexes


class RegionArray:
    element: List[RegionArrayElement]
    type: TypeEnum

    def __init__(self, element: List[RegionArrayElement], type: TypeEnum) -> None:
        self.element = element
        self.type = type


class EmbeddedOutputs:
    meta_data: MetaData
    output_array: OutputArray
    region_array: RegionArray

    def __init__(self, meta_data: MetaData, output_array: OutputArray, region_array: RegionArray) -> None:
        self.meta_data = meta_data
        self.output_array = output_array
        self.region_array = region_array


class Welcome6:
    embedded_outputs: EmbeddedOutputs

    def __init__(self, embedded_outputs: EmbeddedOutputs) -> None:
        self.embedded_outputs = embedded_outputs
