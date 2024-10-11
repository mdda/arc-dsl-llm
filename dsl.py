from arc_types import *


def identity(
    x: Any
) -> Any:
    """ identity function """
    return x


#def add(a: Numerical, b: Numerical) -> Numerical:
@overload
def add[T: Numerical](a: T, b: int) -> T: ...  # Order matters...
@overload
def add[T: Numerical](a: T, b: T) -> T: ...
def add(a, b):
    """ addition """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)


#def subtract(a: Numerical, b: Numerical) -> Numerical:
def subtract[T: Numerical](a:T, b:T) -> T:
    """ subtraction """
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)


#def multiply(a: Numerical, b: Numerical) -> Numerical:
@overload
def multiply[T: Numerical](a: T, b: int) -> T: ...  # Order matters...
@overload
def multiply[T: Numerical](a: T, b: T) -> T: ...
def multiply(a, b):
    """ multiplication """
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

#def divide(a: Numerical, b: Numerical) -> Numerical:
def divide[T: Numerical](a: T, b: T) -> T:
    """ floor division """
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)


#def invert(n: Numerical) -> Numerical:
def invert[T: Numerical](n: T) -> T:
    """ inversion with respect to addition """
    return -n if isinstance(n, int) else (-n[0], -n[1])


def is_even(
    n: Integer
) -> Boolean:
    """ evenness """
    return n % 2 == 0


#def double(n: Numerical) -> Numerical:
def double[T: Numerical](n: T) -> T:
    """ scaling by two """
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)


#def halve(n: Numerical) -> Numerical:
def halve[T: Numerical](n: T) -> T:
    """ scaling by one half """
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)


def flip(
    b: Boolean
) -> Boolean:
    """ logical not """
    return not b


def equality(
    a: Any,
    b: Any
) -> Boolean:
    """ equality """
    return a == b


def contains(
    value: Any,
    container: Container
) -> Boolean:
    """ element of """
    return value in container


#def combine(a: Container, b: Container) -> Container:
def combine[T: Container](a: T, b: T) -> T:
    """ union """
    return type(a)((*a, *b))


def intersection(
    a: FrozenSet,
    b: FrozenSet
) -> FrozenSet:
    """ returns the intersection of two containers """
    return a & b


#def difference(a: FrozenSet, b: FrozenSet) -> FrozenSet:
def difference[T: FrozenSet](a: T, b: T) -> T:
    """ set difference """
    return type(a)(e for e in a if e not in b)


def dedupe(
    tup: Tuple
) -> Tuple:
    """ remove duplicates """
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)


def order(
    container: Container,
    compfunc: Callable
) -> Tuple:
    """ order container by custom key """
    return tuple(sorted(container, key=compfunc))


def repeat(
    item: Any,
    num: Integer
) -> Tuple:
    """ repetition of item within vector """
    return tuple(item for i in range(num))


def is_greater(
    a: Integer,
    b: Integer
) -> Boolean:
    """ greater """
    return a > b


def size(
    container: Container
) -> Integer:
    """ cardinality """
    return len(container)


#def merge(containers: ContainerContainer) -> Container:
@overload
def merge(x: FrozenSet[Object]) -> Object: ...
@overload
def merge(x: Grid) -> Grid: ...        # ??
@overload
def merge(x: Indices) -> Indices: ...  # ??
def merge(containers):
    """ merging """
    return type(containers)(e for c in containers for e in c)


#def maximum(container: IntegerSet) -> Integer:
def maximum(container: Container) -> Integer:
    """ maximum """
    return max(container, default=0)

#def minimum(container: IntegerSet) -> Integer:
def minimum(container: Container) -> Integer:
    """ minimum """
    return min(container, default=0)


def valmax(
    container: Container,
    compfunc: Callable
) -> Integer:
    """ maximum by custom function """
    return compfunc(max(container, key=compfunc, default=0))


def valmin(
    container: Container,
    compfunc: Callable
) -> Integer:
    """ minimum by custom function """
    return compfunc(min(container, key=compfunc, default=0))


def argmax(
    container: Container,
    compfunc: Callable
) -> Any:
    """ largest item by custom order """
    return max(container, key=compfunc)


def argmin(
    container: Container,
    compfunc: Callable
) -> Any:
    """ smallest item by custom order """
    return min(container, key=compfunc)


def most_common(
    container: Container
) -> Any:
    """ most common item """
    return max(set(container), key=container.count)


def least_common(
    container: Container
) -> Any:
    """ least common item """
    return min(set(container), key=container.count)


def initset(
    value: Any
) -> FrozenSet:
    """ initialize container """
    return frozenset({value})


def both(
    a: Boolean,
    b: Boolean
) -> Boolean:
    """ logical and """
    return a and b


def either(
    a: Boolean,
    b: Boolean
) -> Boolean:
    """ logical or """
    return a or b


#def increment(x: Numerical) -> Numerical:
#@overload 
#def increment(x: Integer) -> Integer: ...
#@overload 
#def increment(x: IntegerTuple) -> IntegerTuple: ...
#def increment(x):
def increment[T: Numerical](x: T) -> T:
    """ incrementing """
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)


#def decrement(x: Numerical) -> Numerical:
#@overload 
#def decrement(x: Integer) -> Integer: ...
#@overload 
#def decrement(x: IntegerTuple) -> IntegerTuple: ...
#def decrement(x):
#def decrement(x: Numerical) -> Numerical:
def decrement[T: Numerical](x: T) -> T:
    """ decrementing """
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)


def crement[T: Numerical](x: T) -> T:
    """ incrementing positive and decrementing negative """
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (
        0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),
        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )


#def sign(x: Numerical) -> Numerical:
@overload
def sign(x: Integer) -> Integer: ...
@overload
def sign(x: IntegerTuple) -> IntegerTuple: ...
def sign(x):
    """ sign """
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (
        0 if x[0] == 0 else (1 if x[0] > 0 else -1),
        0 if x[1] == 0 else (1 if x[1] > 0 else -1)
    )


def is_positive(
    x: Integer
) -> Boolean:
    """ positive """
    return x > 0


def to_vertical_vec(
    i: Integer
) -> IntegerTuple:
    """ vector pointing vertically """
    return (i, 0)


def to_horizontal_vec(
    j: Integer
) -> IntegerTuple:
    """ vector pointing horizontally """
    return (0, j)


#def sfilter(container: Container, condition: Callable) -> Container:
def keep_if_condition[T: Container](container: T, condition: Callable) -> T:
    """ keep elements in container that satisfy condition """
    return type(container)(e for e in container if condition(e))


def mfilter(
    container: Container,
    function: Callable
) -> FrozenSet:
    """ filter and merge """
    return merge(keep_if_condition(container, function))


def extract_first_matching(
    container: Container,
    condition: Callable
) -> Any:
    """ first element of container that satisfies condition """
    return next(e for e in container if condition(e))


def to_tuple(
    container: FrozenSet
) -> Tuple:
    """ conversion to tuple """
    return tuple(container)


def first(
    container: Container
) -> Any:
    """ first item of container """
    return next(iter(container))


def last(
    container: Container
) -> Any:
    """ last item of container """
    return max(enumerate(container))[1]


def insert(
    value: Any,
    container: FrozenSet
) -> FrozenSet:
    """ insert item into container """
    return container.union(frozenset({value}))


#def remove(value: Any, container: Container) -> Container:
def remove[T: Container](value: Any, container: T) -> T:
    """ remove item from container """
    return type(container)(e for e in container if e != value)


def other(
    container: Container,
    value: Any
) -> Any:
    """ other value in the container """
    return first(remove(value, container))


def interval(
    start: Integer,
    stop: Integer,
    step: Integer
) -> Tuple:
    """ range """
    return tuple(range(start, stop, step))

#def as_item_tuple[T:Union[Grid, Objects, Tuple]](a: T, b: T) -> Tuple:
def as_generic_tuple[T](a: T, b: T) -> Tuple:  # Tuple[T]
    """ constructs a tuple of two items """
    return (a, b)

def as_tuple(a: Integer, b: Integer) -> IntegerTuple:
    """ constructs a tuple """
    return (a, b)

def make_cell(a: Color, b: Tuple) -> IntegerTuple:
    """ constructs a cell """
    return (a, b)


def cartesian_product(
    a: Container,
    b: Container
) -> FrozenSet:
    """ cartesian product """
    return frozenset((i, j) for j in b for i in a)


def pair(
    a: Tuple,
    b: Tuple
) -> TupleTuple:
    """ zipping of two tuples """
    return tuple(zip(a, b))


def branch(
    condition: Boolean,
    a: Any,
    b: Any
) -> Any:
    """ if else branching """
    return a if condition else b


def compose(
    outer: Callable,
    inner: Callable
) -> Callable:
    """ function composition """
    return lambda x: outer(inner(x))


def chain(
    h: Callable,
    g: Callable,
    f: Callable,
) -> Callable:
    """ function composition with three functions """
    return lambda x: h(g(f(x)))


def matcher(
    function: Callable,
    target: Any
) -> Callable:
    """ construction of equality function """
    return lambda x: function(x) == target


def rbind(
    function: Callable,
    fixed: Any
) -> Callable:
    """ fix the rightmost argument """
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)


def lbind(
    function: Callable,
    fixed: Any
) -> Callable:
    """ fix the leftmost argument """
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)


def power(
    function: Callable,
    n: Integer
) -> Callable:
    """ power of function """
    if n == 1:
        return function
    return compose(function, power(function, n - 1))


def fork(
    outer: Callable,
    a: Callable,
    b: Callable
) -> Callable:
    """ creates a wrapper function """
    return lambda x: outer(a(x), b(x))


#def apply(function: Callable, container: Container) -> Container:
def apply[T: Container](function: Callable, container: T) -> T:
    """ apply function to each item in container """
    return type(container)(function(e) for e in container)


def rapply(functions: Container, value: Any) -> Container:
    """ apply each function in container to value """
    return type(functions)(function(value) for function in functions)


def apply_and_merge(
    function: Callable,
    #container: ContainerContainer
    container: Union[ContainerContainer,ColorSet]  # mdda
) -> FrozenSet:
    """ apply and merge """
    return merge(apply(function, container))


def papply(
    function: Callable,
    a: Tuple,
    b: Tuple
) -> Tuple:
    """ apply function on two vectors """
    return tuple(function(i, j) for i, j in zip(a, b))


def mpapply(
    function: Callable,
    a: Tuple,
    b: Tuple
) -> Tuple:
    """ apply function on two vectors and merge """
    return merge(papply(function, a, b))


def prapply(
    function,
    a: Container,
    b: Container
) -> FrozenSet:
    """ apply function on cartesian product """
    return frozenset(function(i, j) for j in b for i in a)


def most_common_color(
    element: Element
) -> Color:
    """ most common color """
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def least_common_color(
    element: Element
) -> Color:
    """ least common color """
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)


def height(
    piece: Piece
) -> Integer:
    """ height of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1


def width(
    piece: Piece
) -> Integer:
    """ width of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1


def shape(
    piece: Piece
) -> IntegerTuple:
    """ height and width of grid or patch """
    return (height(piece), width(piece))


def is_portrait(
    piece: Piece
) -> Boolean:
    """ whether height is greater than width """
    return height(piece) > width(piece)


def color_count(
    element: Element,
    color: Color
) -> Integer:
    """ number of cells with color """
    if isinstance(element, tuple):
        return sum(row.count(color) for row in element)
    return sum(c == color for c, _ in element)


def color_filter(
    objs: Objects,
    color: Color
) -> Objects:
    """ filter objects by color """
    return frozenset(obj for obj in objs if next(iter(obj))[0] == color)


def size_filter(
    container: Container,
    n: Integer
) -> FrozenSet:
    """ filter items by size """
    return frozenset(item for item in container if len(item) == n)


def as_indices(
    grid: Grid
) -> Indices:
    """ indices of all grid cells """
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))


def of_color(
    grid: Grid,
    color: Color
) -> Indices:
    """ indices of all grid cells with value """
    return frozenset((i, j) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color)


def upper_left_corner(
    patch: Patch
) -> IntegerTuple:
    """ index of upper left corner """
    return tuple(map(min, zip(*to_indices(patch))))


def upper_right_corner(
    patch: Patch
) -> IntegerTuple:
    """ index of upper right corner """
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*to_indices(patch)))))


def lower_left_corner(
    patch: Patch
) -> IntegerTuple:
    """ index of lower left corner """
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*to_indices(patch)))))


def lower_right_corner(
    patch: Patch
) -> IntegerTuple:
    """ index of lower right corner """
    return tuple(map(max, zip(*to_indices(patch))))


def crop(
    grid: Grid,
    start: IntegerTuple,
    dims: IntegerTuple
) -> Grid:
    """ subgrid specified by start and dimension """
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])


def to_indices(
    patch: Patch
) -> Indices:
    """ indices of object cells """
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for _, index in patch)
    return patch


def recolor(
    color: Color,
    patch: Patch
) -> Object:
    """ recolor patch """
    return frozenset((color, index) for index in to_indices(patch))


def shift_by_vector[T:Union[Patch,Objects]](patch: T, directions: IntegerTuple) -> T:
    """ shift patch by vector """
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((color, (i + di, j + dj)) for color, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)


#def normalize(patch: Patch) -> Patch:
def normalize[T:Patch](patch: T) -> T:
    """ moves upper left corner to origin """
    if len(patch) == 0:
        return patch
    return shift_by_vector(patch, (-uppermost(patch), -leftmost(patch)))


def direct_neighbors(
    loc: IntegerTuple
) -> Indices:
    """ directly adjacent indices """
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})


def diagonal_neighbors(
    loc: IntegerTuple
) -> Indices:
    """ diagonally adjacent indices """
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})


def neighbors(
    loc: IntegerTuple
) -> Indices:
    """ adjacent indices """
    return direct_neighbors(loc) | diagonal_neighbors(loc)


def as_objects(
    grid: Grid,
    univalued: Boolean,
    diagonal: Boolean,
    without_bg: Boolean
) -> Objects:
    """ objects occurring on the grid """
    bg = most_common_color(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = as_indices(grid)
    diagfun = neighbors if diagonal else direct_neighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)


def partition(
    grid: Grid
) -> Objects:
    """ each cell with the same value part of the same object """
    return frozenset(
        frozenset(
            (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid)
    )


def partition_only_foreground(
    grid: Grid
) -> Objects:
    """ objects, each segregated by color ignoring the background """
    return frozenset(
        frozenset(
            (c, (i, j)) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color
        ) for color in palette(grid) - {most_common_color(grid)}
    )


def uppermost(
    patch: Patch
) -> Integer:
    """ row index of uppermost occupied cell """
    return min(i for i, j in to_indices(patch))


def lowermost(
    patch: Patch
) -> Integer:
    """ row index of lowermost occupied cell """
    return max(i for i, j in to_indices(patch))


def leftmost(
    patch: Patch
) -> Integer:
    """ column index of leftmost occupied cell """
    return min(j for i, j in to_indices(patch))


def rightmost(
    patch: Patch
) -> Integer:
    """ column index of rightmost occupied cell """
    return max(j for i, j in to_indices(patch))


def square(
    piece: Piece
) -> Boolean:
    """ whether the piece forms a square """
    return len(piece) == len(piece[0]) if isinstance(piece, tuple) else height(piece) * width(piece) == len(piece) and height(piece) == width(piece)


def is_vertical_line(
    patch: Patch
) -> Boolean:
    """ whether the piece forms a vertical line """
    return height(patch) == len(patch) and width(patch) == 1


def is_horizontal_line(
    patch: Patch
) -> Boolean:
    """ whether the piece forms a horizontal line """
    return width(patch) == len(patch) and height(patch) == 1


def hmatching(
    a: Patch,
    b: Patch
) -> Boolean:
    """ whether there exists a row for which both patches have cells """
    return len(set(i for i, j in to_indices(a)) & set(i for i, j in to_indices(b))) > 0


def vmatching(
    a: Patch,
    b: Patch
) -> Boolean:
    """ whether there exists a column for which both patches have cells """
    return len(set(j for i, j in to_indices(a)) & set(j for i, j in to_indices(b))) > 0


def manhattan(
    a: Patch,
    b: Patch
) -> Integer:
    """ closest manhattan distance between two patches """
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in to_indices(a) for bi, bj in to_indices(b))


def adjacent(
    a: Patch,
    b: Patch
) -> Boolean:
    """ whether two patches are adjacent """
    return manhattan(a, b) == 1


def bordering(
    patch: Patch,
    grid: Grid
) -> Boolean:
    """ whether a patch is adjacent to a grid border """
    return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1


def centerofmass(
    patch: Patch
) -> IntegerTuple:
    """ center of mass """
    return tuple(map(lambda x: sum(x) // len(patch), zip(*to_indices(patch))))


def palette(
    element: Element
) -> ColorSet:
    """ colors occurring in object or grid """
    if isinstance(element, tuple):
        return frozenset({c for r in element for c in r}) # Grid
    return frozenset({c for c, _ in element}) # Object


def count_colors(
    element: Element
#) -> IntegerSet:   #mdda : Seems wrong
) -> Integer:  
    """ number of colors occurring in object or grid """
    return len(palette(element))


def color(
    obj: Object
) -> Color:
    """ color of object """
    return next(iter(obj))[0]


def to_object(
    patch: Patch,
    grid: Grid
) -> Object:
    """ object from patch and grid """
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in to_indices(patch) if 0 <= i < h and 0 <= j < w)


def as_object(
    grid: Grid
) -> Object:
    """ conversion of grid to object """
    return frozenset((c, (i, j)) for i, r in enumerate(grid) for j, c in enumerate(r))


def rot90(
    grid: Grid
) -> Grid:
    """ quarter clockwise rotation """
    return tuple(row for row in zip(*grid[::-1]))


def rot180(
    grid: Grid
) -> Grid:
    """ half rotation """
    return tuple(tuple(row[::-1]) for row in grid[::-1])


def rot270(
    grid: Grid
) -> Grid:
    """ quarter anticlockwise rotation """
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

#def horizontal_mirror(piece: Piece) -> Piece:
def horizontal_mirror[T: Piece](piece: T) -> T:
    """ mirroring along horizontal """
    if isinstance(piece, tuple):
        return piece[::-1]
    d = upper_left_corner(piece)[0] + lower_right_corner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((c, (d - i, j)) for c, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)


#def vertical_mirror(piece: Piece) -> Piece:
def vertical_mirror[T: Piece](piece: T) -> T:
    """ mirroring along vertical """
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = upper_left_corner(piece)[1] + lower_right_corner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((c, (i, d - j)) for c, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)


#def diagonal_mirror(piece: Piece) -> Piece:
def diagonal_mirror[T: Piece](piece: T) -> T:
    """ mirroring along diagonal """
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = upper_left_corner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)


#def counterdiagonal_mirror(piece: Piece) -> Piece:
def counterdiagonal_mirror[T: Piece](piece: T) -> T:
    """ mirroring along counterdiagonal """
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return vertical_mirror(diagonal_mirror(vertical_mirror(piece)))


def fill(
    grid: Grid,
    color: Color,
    #patch: Patch
    patch: Union[Patch,Objects,Tuple]  # mdda
) -> Grid:
    """ fill value at indices """
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in to_indices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = color
    return tuple(tuple(row) for row in grid_filled)


def paint(
    grid: Grid,
    #obj: Object
    obj: Union[Object, Tuple, Indices]  # mdda
) -> Grid:
    """ paint object to grid """
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for color, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = color
    return tuple(tuple(row) for row in grid_painted)


def underfill(
    grid: Grid,
    color: Color,
    #patch: Patch
    patch: Piece # mdda
) -> Grid:
    """ fill value at indices that are background """
    h, w = len(grid), len(grid[0])
    bg = most_common_color(grid)
    g = list(list(r) for r in grid)
    for i, j in to_indices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = color
    return tuple(tuple(r) for r in g)


def underpaint(
    grid: Grid,
    #obj: Object
    obj: Union[Object, Tuple, Indices]  # mdda
) -> Grid:
    """ paint object to grid where there is background """
    h, w = len(grid), len(grid[0])
    bg = most_common_color(grid)
    g = list(list(r) for r in grid)
    for color, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = color
    return tuple(tuple(r) for r in g)


def horizontal_upscale(
    grid: Grid,
    factor: Integer
) -> Grid:
    """ upscale grid horizontally """
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g


def vertical_upscale(
    grid: Grid,
    factor: Integer
) -> Grid:
    """ upscale grid vertically """
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g


def upscale[T: Union[Element,Patch]](element: T, factor: Integer) -> T:
    """ upscale object or grid """
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            upscaled_row = tuple()
            for value in row:
                upscaled_row = upscaled_row + tuple(value for num in range(factor))
            g = g + tuple(upscaled_row for num in range(factor))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        di_inv, dj_inv = upper_left_corner(element)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = shift_by_vector(element, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return shift_by_vector(frozenset(o), (di_inv, dj_inv))


def downscale(
    grid: Grid,
    factor: Integer
) -> Grid:
    """ downscale grid """
    h, w = len(grid), len(grid[0])
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg


def horizontal_concat(
    a: Grid,
    b: Grid
) -> Grid:
    """ concatenate two grids horizontally """
    return tuple(i + j for i, j in zip(a, b))


def vertical_concat(
    a: Grid,
    b: Grid
) -> Grid:
    """ concatenate two grids vertically """
    return a + b


def subgrid(
    patch: Patch,
    grid: Grid
) -> Grid:
    """ smallest subgrid containing object """
    return crop(grid, upper_left_corner(patch), shape(patch))


def horizontal_split(
    grid: Grid,
    n: Integer
) -> Tuple:
    """ split grid horizontally """
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))


def vertical_split(
    grid: Grid,
    n: Integer
) -> Tuple:
    """ split grid vertically """
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))


def cellwise(
    a: Grid,
    b: Grid,
    fallback: Color
) -> Grid:
    """ cellwise match of two grids """
    h, w = len(a), len(a[0])
    resulting_grid = tuple()
    for i in range(h):
        row = tuple()
        for j in range(w):
            a_color = a[i][j]
            color = a_color if a_color == b[i][j] else fallback
            row = row + (color,)
        resulting_grid = resulting_grid + (row, )
    return resulting_grid


def replace(
    grid: Grid,
    replacee: Color,
    replacer: Color
) -> Grid:
    """ color substitution """
    return tuple(tuple(replacer if c == replacee else c for c in r) for r in grid)


def switch(
    grid: Grid,
    a: Color,
    b: Color
) -> Grid:
    """ color switching """
    return tuple(tuple(c if (c != a and c != b) else {a: b, b: a}[c] for c in r) for r in grid)


def center(
    patch: Patch
) -> IntegerTuple:
    """ center of the patch """
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)


def position(
    a: Patch,
    b: Patch
) -> IntegerTuple:
    """ relative position between two patches """
    ia, ja = center(to_indices(a))
    ib, jb = center(to_indices(b))
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    elif ja == jb:
        return (1 if ia < ib else -1, 0)
    elif ia < ib:
        return (1, 1 if ja < jb else -1)
    elif ia > ib:
        return (-1, 1 if ja < jb else -1)


def color_at_location(
    grid: Grid,
    loc: IntegerTuple
) -> Color:
    """ color at location """
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 


def canvas(
    color: Color,
    dimensions: IntegerTuple
) -> Grid:
    """ grid construction """
    return tuple(tuple(color for j in range(dimensions[1])) for i in range(dimensions[0]))


def corners(
    patch: Patch
) -> Indices:
    """ indices of corners """
    return frozenset({upper_left_corner(patch), upper_right_corner(patch), lower_left_corner(patch), lower_right_corner(patch)})


def connect(
    a: IntegerTuple,
    b: IntegerTuple
) -> Indices:
    """ line between two points """
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()


def cover(
    grid: Grid,
    patch: Patch
) -> Grid:
    """ remove object from grid """
    return fill(grid, most_common_color(grid), to_indices(patch))


def trim(
    grid: Grid
) -> Grid:
    """ trim border of grid """
    return tuple(r[1:-1] for r in grid[1:-1])


def move(
    grid: Grid,
    obj: Object,
    offset: IntegerTuple
) -> Grid:
    """ move object on grid """
    return paint(cover(grid, obj), shift_by_vector(obj, offset))


def top_half(
    grid: Grid
) -> Grid:
    """ upper half of grid """
    return grid[:len(grid) // 2]


def bottom_half(
    grid: Grid
) -> Grid:
    """ lower half of grid """
    return grid[len(grid) // 2 + len(grid) % 2:]


def left_half(
    grid: Grid
) -> Grid:
    """ left half of grid """
    return rot270(top_half(rot90(grid)))


def right_half(
    grid: Grid
) -> Grid:
    """ right half of grid """
    return rot270(bottom_half(rot90(grid)))


def vfrontier(
    location: IntegerTuple
) -> Indices:
    """ vertical frontier """
    return frozenset((i, location[1]) for i in range(30))


def hfrontier(
    location: IntegerTuple
) -> Indices:
    """ horizontal frontier """
    return frozenset((location[0], j) for j in range(30))


def backdrop(
    patch: Patch
) -> Indices:
    """ indices in bounding box of patch """
    if len(patch) == 0:
        return frozenset({})
    indices = to_indices(patch)
    si, sj = upper_left_corner(indices)
    ei, ej = lower_right_corner(patch)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))


def delta(
    patch: Patch
) -> Indices:
    """ indices in bounding box but not part of patch """
    if len(patch) == 0:
        return frozenset({})
    return backdrop(patch) - to_indices(patch)


def gravitate(
    source: Patch,
    destination: Patch
) -> IntegerTuple:
    """ direction to move source until adjacent to destination """
    si, sj = center(source)
    di, dj = center(destination)
    i, j = 0, 0
    if vmatching(source, destination):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = i, j
    c = 0
    while not adjacent(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = shift_by_vector(source, (i, j))
    return (gi - i, gj - j)


def inbox(
    patch: Patch
) -> Indices:
    """ inbox for patch """
    ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
    bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def outbox(
    patch: Patch
) -> Indices:
    """ outbox for patch """
    ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
    bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def box(
    patch: Patch
) -> Indices:
    """ outline of patch """
    if len(patch) == 0:
        return patch
    ai, aj = upper_left_corner(patch)
    bi, bj = lower_right_corner(patch)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def shoot(
    start: IntegerTuple,
    direction: IntegerTuple
) -> Indices:
    """ line from starting point and direction """
    return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))


def occurrences(
    grid: Grid,
    obj: Object
) -> Indices:
    """ locations of occurrences of object in grid """
    occs = set()
    normed = normalize(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = shape(obj)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = True
            for v, (a, b) in shift_by_vector(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and grid[a][b] == v):
                    occurs = False
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)


def frontiers( grid: Grid ) -> Objects:
    """ set of frontiers """
    h, w = len(grid), len(grid[0])
    row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    column_indices = tuple(j for j, c in enumerate(diagonal_mirror(grid)) if len(set(c)) == 1)
    hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers


def compress(
    grid: Grid
) -> Grid:
    """ removes frontiers from grid """
    ri = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    ci = tuple(j for j, c in enumerate(diagonal_mirror(grid)) if len(set(c)) == 1)
    return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(grid) if i not in ri)


def horizontal_periodicity(
    obj: Object
) -> Integer:
    """ horizontal periodicity """
    normalized = normalize(obj)
    w = width(normalized)
    for p in range(1, w):
        offsetted = shift_by_vector(normalized, (0, -p))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
        if pruned.issubset(normalized):
            return p
    return w


def vertical_periodicity(
    obj: Object
) -> Integer:
    """ vertical periodicity """
    normalized = normalize(obj)
    h = height(normalized)
    for p in range(1, h):
        offsetted = shift_by_vector(normalized, (-p, 0))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
        if pruned.issubset(normalized):
            return p
    return h
