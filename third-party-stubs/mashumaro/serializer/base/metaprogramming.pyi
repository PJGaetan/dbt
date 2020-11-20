from mashumaro.meta.helpers import *
from mashumaro.serializer.base.helpers import *
from base64 import decodebytes as decodebytes, encodebytes as encodebytes
from mashumaro.exceptions import InvalidFieldValue as InvalidFieldValue, MissingField as MissingField, UnserializableDataError as UnserializableDataError, UnserializableField as UnserializableField
from mashumaro.meta.patch import patch_fromisoformat as patch_fromisoformat
from mashumaro.types import SerializableType as SerializableType, SerializationStrategy as SerializationStrategy
from typing import Any

NoneType: Any
INITIAL_MODULES: Any

class CodeBuilder:
    cls: Any = ...
    lines: Any = ...
    modules: Any = ...
    globals: Any = ...
    def __init__(self, cls: Any) -> None: ...
    def reset(self) -> None: ...
    @property
    def namespace(self): ...
    @property
    def annotations(self): ...
    @property
    def fields(self): ...
    @property
    def defaults(self): ...
    def add_line(self, line: Any) -> None: ...
    def indent(self) -> None: ...
    def compile(self) -> None: ...
    def add_from_dict(self) -> None: ...
    def add_to_dict(self) -> None: ...
    def add_pack_union(self, fname: Any, ftype: Any, parent: Any, variant_types: Any, value_name: Any): ...
    def add_unpack_union(self, fname: Any, ftype: Any, parent: Any, variant_types: Any, value_name: Any): ...