from typing import (
    List,
    Union,
    Tuple,
    Any,
    Container,
    Callable,
    FrozenSet,
    Iterable,
    NewType,
    overload,
)

Boolean = bool
Integer = int
IntegerSet = FrozenSet[Integer]
IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IntegerTuple]
Color = NewType('Color', int)
ColorSet = FrozenSet[Color]
#Grid = Tuple[Tuple[Integer]]
#Cell = Tuple[Integer, IntegerTuple]
Grid = Tuple[Tuple[Color]]
Cell = Tuple[Color, IntegerTuple]
Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IntegerTuple]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
Element = Union[Object, Grid]
Piece = Union[Grid, Patch]
TupleTuple = Tuple[Tuple]
ContainerContainer = Container[Container]

