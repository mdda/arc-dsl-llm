from .arc_types import *

def identity(x: Any) -> Any:
    """Returns the input unchanged"""
    return x


#def add(a: Numerical, b: Numerical) -> Numerical:
@overload
def add[T: Numerical](a: T, b: int) -> T: ...  # Order matters...
@overload
def add[T: Numerical](a: T, b: T) -> T: ...
def add(a, b):
    """Adds two numbers or tuples element-wise"""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)


#def subtract(a: Numerical, b: Numerical) -> Numerical:
def subtract[T: Numerical](a:T, b:T) -> T:
    """Subtracts two numbers or tuples element-wise"""
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
    """Multiplies two numbers or tuples element-wise"""
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

#def divide(a: Numerical, b: Numerical) -> Numerical:
def divide[T: Numerical](a: T, b: T) -> T:
    """Performs floor division of two numbers or tuples element-wise"""
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)


#def double(n: Numerical) -> Numerical:
def double[T: Numerical](n: T) -> T:
    """Multiplies a number or tuple by two"""
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

#def halve(n: Numerical) -> Numerical:
def halve[T: Numerical](n: T) -> T:
    """Performs floor division of a number or tuple by two"""
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)

def is_even(n: Integer) -> Boolean:
    """Checks if a number is even"""
    return n % 2 == 0


# was 'invert'
#def invert(n: Numerical) -> Numerical:
def negate[T: Numerical](n: T) -> T:
    """Returns the additive inverse (negation) of a number or tuple"""
    return -n if isinstance(n, int) else (-n[0], -n[1])

def is_positive(x: Integer) -> Boolean:
    """ positive """
    return x > 0


def logical_not(a: Boolean) -> Boolean:
    """Returns the logical NOT of the input"""
    return not a

# was both
def logical_and(a: Boolean, b: Boolean) -> Boolean:
    """Returns the logical AND of the inputs"""
    return a and b

# was either
def logical_or(a: Boolean, b: Boolean) -> Boolean:
    """Returns the logical OR of the inputs"""
    return a or b


def is_equal(a: Any, b: Any) -> Boolean:
    """Returns True iff 'a' and 'b' are equal"""
    return a == b

def greater_than(a: Integer, b: Integer) -> Boolean:
    """Returns True iff 'a' is greater than 'b'"""
    return a > b


def contains(value: Any, container: Container) -> Boolean:
    """Returns True iff 'value' is present in 'container'"""
    return value in container

# was combine
#def union(a: Container, b: Container) -> Container:
def union[T: Container](a: T, b: T) -> T:
    """Returns the union of two containers of the same type"""
    return type(a)((*a, *b))

def intersection(a: FrozenSet,b: FrozenSet) -> FrozenSet:
    """Returns the intersection of two containers"""
    return a & b

#def difference(a: FrozenSet, b: FrozenSet) -> FrozenSet:
def difference[T: FrozenSet](a: T, b: T) -> T:
    """Returns the set difference of two containers (elements in 'a' but not in 'b')"""
    return type(a)(e for e in a if e not in b)

# was dedupe
def remove_duplicates(tup: Tuple) -> Tuple:
    """Removes duplicate elements from a tuple, preserving order"""
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)


# was order
def sort(container: Container, compfunc: Callable) -> Tuple:
    """Sorts a container and returns the result as a tuple.  Uses the provided function for sorting"""
    return tuple(sorted(container, key=compfunc))


def repeat(item: Any, times: Integer) -> Tuple:
    """Creates a tuple containing 'item' repeated 'times'"""
    return tuple(item for i in range(times))


def size(container: Container) -> Integer:
    """Number of elements in the container"""
    return len(container)


#def maximum(container: IntegerSet) -> Integer:
def maximum(container: Container) -> Integer:
    """Returns the maximum value in a container (0 if empty)"""
    return max(container, default=0)

#def minimum(container: IntegerSet) -> Integer:
def minimum(container: Container) -> Integer:
    """Returns the minimum value in a container (0 if empty)"""
    return min(container, default=0)


def valmax(container: Container, compfunc: Callable) -> Integer:
    """ maximum by custom function """
    return compfunc(max(container, key=compfunc, default=0))

def valmin(container: Container, compfunc: Callable) -> Integer:
    """ minimum by custom function """
    return compfunc(min(container, key=compfunc, default=0))


def argmax(container: Container, compfunc: Callable) -> Any:
    """ largest item by custom order """
    return max(container, key=compfunc)

def argmin(container: Container, compfunc: Callable) -> Any:
    """ smallest item by custom order """
    return min(container, key=compfunc)


def most_common(container: Container) -> Any:
    """ most common item """
    return max(set(container), key=container.count)

def least_common(container: Container) -> Any:
    """ least common item """
    return min(set(container), key=container.count)


def increment[T: Numerical](x: T) -> T:
    """ incrementing """
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

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


def sign[T: Numerical](x: T) -> T:
    """ sign """
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (
        0 if x[0] == 0 else (1 if x[0] > 0 else -1),
        0 if x[1] == 0 else (1 if x[1] > 0 else -1)
    )



def to_vertical_vec(i: Integer) -> IntegerTuple:
    """ vector pointing vertically """
    return (i, 0)


def to_horizontal_vec(j: Integer) -> IntegerTuple:
    """ vector pointing horizontally """
    return (0, j)



def initset(value: Any) -> FrozenSet:
    """ initialize container """
    return frozenset({value})

def insert(value: Any, container: FrozenSet) -> FrozenSet:
    """ insert item into container """
    return container.union(frozenset({value}))

#def remove(value: Any, container: Container) -> Container:
def remove[T: Container](value: Any, container: T) -> T:
    """ remove item from container """
    return type(container)(e for e in container if e != value)

def get_first(container: Container) -> Any:
    """ first item of container """
    return next(iter(container))

def get_other(container: Container, value: Any) -> Any:
    """ other value in the container """
    return get_first(remove(value, container))

def get_last(container: Container) -> Any:
    """ last item of container """
    return max(enumerate(container))[1]


# was merge
#def flatten(containers: ContainerContainer) -> Container:
@overload
def flatten(x: FrozenSet[Object]) -> Object: ...
@overload
def flatten(x: Grid) -> Grid: ...        # ??
@overload
def flatten(x: Indices) -> Indices: ...  # ??
def flatten(containers):
    """Flattens a nested container into a single container"""
    return type(containers)(e for c in containers for e in c)


#def sfilter(container: Container, condition: Callable) -> Container:
def keep_if_condition[T: Container](container: T, condition: Callable) -> T:
    """Returns 'container' with only the elements that satisfy 'condition'"""
    return type(container)(e for e in container if condition(e))

# was mfilter
def keep_if_condition_and_flatten(container: Container, condition: Callable) -> FrozenSet:
    """Returns the elements of 'container' than satisfy 'condition', in a flattened form"""
    return flatten(keep_if_condition(container, condition))

def extract_first_matching(container: Container, condition: Callable) -> Any:
    """Returns the first element of 'container' that satisfies 'condition'"""
    return next(e for e in container if condition(e))


def interval(start: Integer, stop: Integer, step: Integer) -> Tuple:
    """Returns a tuple containing integers from `range(start, stop, step)`"""
    return tuple(range(start, stop, step))


def to_tuple(container: FrozenSet) -> Tuple:
    """Returns a tuple containing the contents of 'container'"""
    return tuple(container)

#def as_item_tuple[T:Union[Grid, Objects, Tuple]](a: T, b: T) -> Tuple:
def as_generic_tuple[T](a: T, b: T) -> Tuple:  # new
    """Returns the tuple (a, b)"""
    return (a, b)

def as_tuple(a: Integer, b: Integer) -> IntegerTuple:
    """Returns the integer tuple (a,b)"""
    return (a, b)

def make_cell(color: Color, location: Tuple) -> IntegerTuple:  # new
    """Returns the Cell(color, location), where 'location' is a pair of coordinates"""
    return (color, location)

# was product
def cartesian_product(a: Container, b: Container) -> FrozenSet:
    """Returns the Cartesian product of two containers as a set of tuples"""
    return frozenset((i, j) for j in b for i in a)


def pairwise(a: Tuple, b: Tuple) -> TupleTuple:
    """Returns the pairwise zipping of the two tuples 'a' and 'b'"""
    return tuple(zip(a, b))


def condition_if_else(condition: Boolean, a: Any, b: Any) -> Any:
    """if condition==True: return a; else: return b"""
    return a if condition else b


def compose( outer: Callable, inner: Callable ) -> Callable:
    """Composes two functions: `outer(inner(x))`"""
    return lambda x: outer(inner(x))


def chain( h: Callable, g: Callable, f: Callable ) -> Callable:
    """Composes three functions: `h(g(f(x)))`"""
    return lambda x: h(g(f(x)))

# was matcher
def equals( function: Callable, target: Any ) -> Callable:
    """Creates a function that checks if the result of 'function(x)' equals 'target'"""
    return lambda x: function(x) == target

# was rbind
def fix_last_argument( function: Callable, fixed_arg: Any ) -> Callable:
    """Returns a new function with the rightmost argument fixed to 'fixed_arg'"""
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed_arg)
    elif n == 3:
        return lambda x, y: function(x, y, fixed_arg)
    else:
        return lambda x, y, z: function(x, y, z, fixed_arg)

# was lbind
def fix_first_argument( function: Callable, fixed_arg: Any ) -> Callable:
    """Returns a new function with the leftmost argument fixed to 'fixed_arg'"""
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed_arg, y)
    elif n == 3:
        return lambda y, z: function(fixed_arg, y, z)
    else:
        return lambda y, z, a: function(fixed_arg, y, z, a)


def power( function: Callable, n: Integer ) -> Callable:
    """Returns a function that applies 'function' to its argument 'n' times"""
    if n == 1:
        return function
    return compose( function, power(function, n-1) )

# was fork(!)
def combine_two_function_results( outer: Callable, f1: Callable, f2: Callable ) -> Callable:
    """Combines the results of two functions ('f1' and 'f2') using 'outer'"""
    return lambda x: outer(f1(x), f2(x))

# was apply
#def apply(function: Callable, container: Container) -> Container:
def transform[T: Container](function: Callable, container: T) -> T:
    """Applies a function to each element of a container"""
    return type(container)(function(e) for e in container)

# was rapply
def apply_each_function(functions: Container, value: Any) -> Container:
    """Applies each function in a container to a single value"""
    return type(functions)(function(value) for function in functions)

# was mapply
# also : container: ContainerContainer # Changed by mdda
def transform_and_flatten(function: Callable, container: Union[ContainerContainer,ColorSet]) -> FrozenSet:
    """Applies a transform to a nested container and flattens the result"""
    return flatten(transform(function, container))

# was papply
def transform_both(function: Callable, a: Tuple, b: Tuple) -> Tuple:
    """Applies a function pairwise to elements of two tuples"""
    return tuple(function(i, j) for i, j in zip(a, b))

# was mpapply
def transform_both_and_flatten(function: Callable, a: Tuple, b: Tuple) -> Tuple:
    """Applies a function pairwise to two tuples and flattens the result"""
    return flatten(transform_both(function, a, b))

# was prapply
def apply_function_on_cartesian_product(function: Callable, a: Container, b: Container) -> FrozenSet:
    """Applies a function to all pairs in the Cartesian product of two containers"""
    return frozenset(function(i, j) for j in b for i in a)


def most_common_color(element: Element) -> Color:
    """Returns the most frequent color in a grid or object"""
    colors = [c for r in element for c in r] if isinstance(element, tuple) else [c for c, _ in element]
    return max(set(colors), key=colors.count)

def least_common_color(element: Element) -> Color:
    """Returns the least frequent color in a grid or object"""
    colors = [c for r in element for c in r] if isinstance(element, tuple) else [c for c, _ in element]
    return min(set(colors), key=colors.count)

# was height
def get_height(piece: Piece) -> Integer:
    """Returns the height of a grid or patch"""
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1

# was width
def get_width(piece: Piece) -> Integer:
    """Returns the width of a grid or patch"""
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

# was shape
def get_shape(piece: Piece) -> IntegerTuple:
    """Returns (height, width) for a grid or patch"""
    return (get_height(piece), get_width(piece))

def is_portrait(piece: Piece) -> Boolean:
    """Returns True iff height>width for a grid or patch"""
    return get_height(piece) > get_width(piece)


def color_count(element: Element, color: Color) -> Integer:
    """Returns the number of cells of 'color'"""
    if isinstance(element, tuple):
        return sum(row.count(color) for row in element)
    return sum(c == color for c, _ in element)

def color_filter(objs: Objects, color: Color) -> Objects:
    """Returns the objects filtered by 'color'"""
    return frozenset(obj for obj in objs if next(iter(obj))[0] == color)


def as_indices(grid: Grid) -> Indices:
    """Returns the indices of all cells in 'grid'"""
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def size_filter(container: Container, size: Integer) -> FrozenSet:
    """Returns the objects filtered by 'size'"""
    return frozenset(item for item in container if len(item) == size)

def of_color(grid: Grid, color: Color) -> Indices:
    """Returns the indices of all cells in 'grid' which are 'color'"""
    return frozenset((i, j) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color)


def upper_left_corner(patch: Patch) -> IntegerTuple:
    """Returns the index of the upper left corner"""
    return tuple(map(min, zip(*to_indices(patch))))

def upper_right_corner(patch: Patch) -> IntegerTuple:
    """Returns the index of the upper right corner"""
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*to_indices(patch)))))

def lower_left_corner(patch: Patch) -> IntegerTuple:
    """Returns the index of the lower left corner"""
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*to_indices(patch)))))

def lower_right_corner(patch: Patch) -> IntegerTuple:
    """Returns the index of the lower right corner"""
    return tuple(map(max, zip(*to_indices(patch))))


def crop(grid: Grid, start: IntegerTuple, dims: IntegerTuple) -> Grid:
    """ subgrid specified by start and dimension """
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])


def to_indices(patch: Patch) -> Indices:
    """Returns the indices of the cells within 'patch'"""
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for _, index in patch)
    return patch


def recolor( color: Color, patch: Patch ) -> Object:
    """Returns 'patch' with each color set to 'color'"""
    return frozenset((color, index) for index in to_indices(patch))


def shift_by_vector[T:Union[Patch,Objects]](patch: T, offset: IntegerTuple) -> T:
    """Moves 'patch' by the vector 'offset'"""
    if len(patch) == 0:
        return patch
    di, dj = offset
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((color, (i + di, j + dj)) for color, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)


#def normalize(patch: Patch) -> Patch:
def shift_to_origin[T:Patch](patch: T) -> T:
    """Moves upper left corner of 'patch' to the origin"""
    if len(patch) == 0:
        return patch
    return shift_by_vector(patch, (-uppermost(patch), -leftmost(patch)))


def direct_neighbors(loc: IntegerTuple) -> Indices:
    """Returns indices that are directly adjacent to 'loc'"""
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})


def diagonal_neighbors(loc: IntegerTuple) -> Indices:
    """Returns indices that are diagonally adjacent to 'loc'"""
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})


def neighbors(loc: IntegerTuple) -> Indices:
    """Returns indices that are either directly of diagonally adjacent to 'loc'"""
    return direct_neighbors(loc) | diagonal_neighbors(loc)


def as_objects(grid: Grid, each_object_single_color: Boolean, include_diagonal_neighbors: Boolean, discard_background: Boolean) -> Objects:
    """Converts 'grid' to a set of connected objects"""
    bg = most_common_color(grid) if discard_background else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = as_indices(grid)
    neighbor_fun = neighbors if include_diagonal_neighbors else direct_neighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        color = grid[loc[0]][loc[1]]
        if color == bg:
            continue
        obj = {(color, loc)}
        candidates = {loc}
        while len(candidates) > 0:
            neighborhood = set()
            for candidate in candidates:
                c = grid[candidate[0]][candidate[1]]
                if (color == c) if each_object_single_color else (c != bg):
                    obj.add((c, candidate))
                    occupied.add(candidate)
                    neighborhood |= {
                        (i, j) for i, j in neighbor_fun(candidate) if 0 <= i < h and 0 <= j < w
                    }
            candidates = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)


def partition(grid: Grid) -> Objects:
    """Converts 'grid' to a set of objects by color"""
    return frozenset(
        frozenset(
            (c, (i, j)) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color
        ) for color in palette(grid)
    )


def partition_only_foreground(grid: Grid) -> Objects:
    """Converts 'grid' to a set of objects by color, ignoring the background"""
    return frozenset(
        frozenset(
            (c, (i, j)) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color
        ) for color in palette(grid) - {most_common_color(grid)}
    )


def uppermost(patch: Patch) -> Integer:
    """Returns the row index of uppermost occupied cell of 'patch'"""
    return min(i for i, j in to_indices(patch))

def lowermost(patch: Patch) -> Integer:
    """Returns the row index of lowermost occupied cell of 'patch'"""
    return max(i for i, j in to_indices(patch))

def leftmost(patch: Patch) -> Integer:
    """Returns the column index of leftmost occupied cell of 'patch'"""
    return min(j for i, j in to_indices(patch))

def rightmost(patch: Patch) -> Integer:
    """Returns the column index of rightmost occupied cell of 'patch'"""
    return max(j for i, j in to_indices(patch))


def is_square(piece: Piece) -> Boolean:
    """Returns True iff the piece forms a square"""
    return len(piece) == len(piece[0]) if isinstance(piece, tuple) else get_height(piece) * get_width(piece) == len(piece) and get_height(piece) == get_width(piece)

def is_vertical_line(patch: Patch) -> Boolean:
    """Returns True iff the piece forms a vertical line"""
    return get_height(patch) == len(patch) and get_width(patch) == 1

def is_horizontal_line(patch: Patch) -> Boolean:
    """Returns True iff the piece forms a horizontal line"""
    return get_width(patch) == len(patch) and get_height(patch) == 1


def horizontal_matching(a: Patch, b: Patch) -> Boolean:
    """Returns True iff there exists a row for which both patches have cells"""
    return len(set(i for i, j in to_indices(a)) & set(i for i, j in to_indices(b))) > 0

def vertical_matching(a: Patch, b: Patch) -> Boolean:
    """Returns True iff there exists a column for which both patches have cells"""
    return len(set(j for i, j in to_indices(a)) & set(j for i, j in to_indices(b))) > 0


def manhattan_distance(a: Patch, b: Patch) -> Integer:
    """Returns the minimum manhattan distance between two patches"""
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in to_indices(a) for bi, bj in to_indices(b))

def adjacent(a: Patch, b: Patch) -> Boolean:
    """Returns True iff two patches are adjacent"""
    return manhattan_distance(a, b) == 1


def bordering(patch: Patch, grid: Grid) -> Boolean:
    """Returns True iff 'patch' is adjacent to a border of 'grid'"""
    return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1


def centerofmass(patch: Patch) -> IntegerTuple:
    """Returns the center of mass of 'patch'"""
    return tuple(map(lambda x: sum(x) // len(patch), zip(*to_indices(patch))))


def palette(element: Element) -> ColorSet:
    """Returns the set of colors occurring in object or grid"""
    if isinstance(element, tuple):
        return frozenset({c for r in element for c in r}) # Grid
    return frozenset({c for c, _ in element}) # Object

#) -> IntegerSet:   #mdda : Seems wrong
def count_colors(element: Element) -> Integer:  
    """Returns the number of colors occurring in object or grid"""
    return len(palette(element))

# was color
def get_color(obj: Object) -> Color:
    """Returns the color of object"""
    return next(iter(obj))[0]


def to_object(patch: Patch, grid: Grid) -> Object:
    """Returns the object given by extracting the locations in 'patch' from 'grid'"""
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in to_indices(patch) if 0 <= i < h and 0 <= j < w)


def as_object(grid: Grid) -> Object:
    """Returns the 'grid' converted to an object"""
    return frozenset((c, (i, j)) for i, r in enumerate(grid) for j, c in enumerate(r))


def rot90(grid: Grid) -> Grid:
    """Returns 'grid' rotated a quarter turn clockwise"""
    return tuple(row for row in zip(*grid[::-1]))

def rot180(grid: Grid) -> Grid:
    """Returns 'grid' rotated a half turn"""
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def rot270(grid: Grid) -> Grid:
    """Returns 'grid' rotated a quarter turn anticlockwise"""
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]


#def horizontal_mirror(piece: Piece) -> Piece:
def horizontal_mirror[T: Piece](piece: T) -> T:
    """Returns 'piece' mirrored along horizontal axis"""
    if isinstance(piece, tuple):
        return piece[::-1]
    d = upper_left_corner(piece)[0] + lower_right_corner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((c, (d - i, j)) for c, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

#def vertical_mirror(piece: Piece) -> Piece:
def vertical_mirror[T: Piece](piece: T) -> T:
    """Returns 'piece' mirrored along vertical axis"""
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = upper_left_corner(piece)[1] + lower_right_corner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((c, (i, d - j)) for c, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

#def diagonal_mirror(piece: Piece) -> Piece:
def diagonal_mirror[T: Piece](piece: T) -> T:
    """Returns 'piece' mirrored along diagonal"""
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = upper_left_corner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

#def counterdiagonal_mirror(piece: Piece) -> Piece:
def counterdiagonal_mirror[T: Piece](piece: T) -> T:
    """Returns 'piece' mirrored along counterdiagonal"""
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return vertical_mirror(diagonal_mirror(vertical_mirror(piece)))


# Is there a better name for this?
# changed patch: Patch :: mdda
def fill(grid: Grid, color: Color, patch: Union[Patch,Objects,Tuple]) -> Grid:
    """Returns 'grid' with 'color' filled in at the indices in 'patch'"""
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in to_indices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = color
    return tuple(tuple(row) for row in grid_filled)

# was underfill
# changed patch: Patch :: mdda
def fill_background(grid: Grid, color: Color, patch: Piece) -> Grid:
    """Returns 'grid' with 'color' filled in at the indices in 'patch' over the background parts"""
    h, w = len(grid), len(grid[0])
    bg = most_common_color(grid)
    g = list(list(r) for r in grid)
    for i, j in to_indices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = color
    return tuple(tuple(r) for r in g)


# was paint
# changed obj: Object :: mdda
def paint_onto_grid(grid: Grid, obj: Union[Object, Tuple, Indices]) -> Grid:
    """Returns 'grid' the object painted onto it"""
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for color, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = color
    return tuple(tuple(row) for row in grid_painted)

# was underpaint
# changed obj: Object :: mdda
def paint_onto_grid_background(grid: Grid, obj: Union[Object, Tuple, Indices]) -> Grid:
    """Returns 'grid' the object painted onto only its background"""
    h, w = len(grid), len(grid[0])
    bg = most_common_color(grid)
    g = list(list(r) for r in grid)
    for color, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = color
    return tuple(tuple(r) for r in g)


def horizontal_upscale(grid: Grid, factor: Integer) -> Grid:
    """Returns 'grid' upscaled horizontally by 'factor'"""
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def vertical_upscale(grid: Grid, factor: Integer) -> Grid:
    """Returns 'grid' upscaled vertically by 'factor'"""
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g

def upscale[T: Union[Element,Patch]](element: T, factor: Integer) -> T:
    """Returns object or grid upscaled overall by 'factor'"""
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

def downscale(grid: Grid, factor: Integer) -> Grid:
    """Returns 'grid' downscaled overall by 'factor'"""
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


def horizontal_concat(a: Grid, b: Grid) -> Grid:
    """Returns a grid formed by concatenating the grids 'a' and 'b' horizontally"""
    return tuple(i + j for i, j in zip(a, b))

def vertical_concat(a: Grid, b: Grid) -> Grid:
    """Returns a grid formed by concatenating the grids 'a' and 'b' vertically"""
    return a + b


def smallest_subgrid_containing(patch: Patch, grid: Grid) -> Grid:
    """ smallest subgrid containing object """
    return crop(grid, upper_left_corner(patch), get_shape(patch))


def horizontal_split(grid: Grid, n: Integer) -> Tuple:
    """Returns 'n' smaller grids formed by splitting 'grid' horizontally"""
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))

def vertical_split(grid: Grid, n: Integer) -> Tuple:
    """Returns 'n' smaller grids formed by splitting 'grid' vertically"""
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))


def cellwise(a: Grid, b: Grid, fallback: Color) -> Grid:
    """Returns the grid resulting from copying the places where 'a' and 'b' match, but having the color 'fallback' where they do not"""
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


def replace(grid: Grid, replacee: Color, replacer: Color) -> Grid:
    """Returns 'grid' where the color 'replacee' is replaced by 'replacer'"""
    return tuple(tuple(replacer if c == replacee else c for c in r) for r in grid)

def switch(grid: Grid, a: Color, b: Color) -> Grid:
    """Returns 'grid' where the colors 'a' and 'b' are switched"""
    return tuple(tuple(c if (c != a and c != b) else {a: b, b: a}[c] for c in r) for r in grid)


def center(patch: Patch) -> IntegerTuple:
    """Returns the coordinates of the center of 'patch'"""
    return (uppermost(patch) + get_height(patch) // 2, leftmost(patch) + get_width(patch) // 2)


def position(a: Patch, b: Patch) -> IntegerTuple:
    """Returns the relative position of patch 'b' to patch 'a' as (vertical, horizontal). Values are -1, 0, or 1, representing down/left, same, or up/right respectively"""
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


def color_at_location(grid: Grid, location: IntegerTuple) -> Color:
    """Returns the color found in 'grid' at 'location'"""
    i, j = location
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[location[0]][location[1]] 

# was canvas
def create_grid(color: Color, dimensions: IntegerTuple) -> Grid:
    """Creates a grid filled with the specified 'color' and 'dimensions' (height, width)"""
    return tuple(tuple(color for j in range(dimensions[1])) for i in range(dimensions[0]))

# was corners
def corner_indices(patch: Patch) -> Indices:
    """Returns the indices of the corners of a patch as a set"""
    return frozenset({upper_left_corner(patch), upper_right_corner(patch), lower_left_corner(patch), lower_right_corner(patch)})


def line_between(a: IntegerTuple, b: IntegerTuple) -> Indices:
    """Returns the indices of cells forming a line between two points. Supports horizontal, vertical, and exactly diagonal lines. Returns an empty set if the line is not one of these types"""
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


# was cover
def erase_patch(grid: Grid, patch: Patch) -> Grid:
    """Erases a patch from the grid by filling it with the most common color (background)"""
    return fill(grid, most_common_color(grid), to_indices(patch))

# was trim
def trim_border(grid: Grid) -> Grid:
    """Removes the outer border (one cell wide) from the grid"""
    return tuple(r[1:-1] for r in grid[1:-1])

# was move
def move_object(grid: Grid, obj: Object, offset: IntegerTuple) -> Grid:
    """Moves an object on the grid by the given offset (vertical, horizontal)"""
    return paint_onto_grid(erase_patch(grid, obj), shift_by_vector(obj, offset))



def top_half(grid: Grid) -> Grid:
    """Returns the top half of the grid"""
    return grid[:len(grid) // 2]

def bottom_half(grid: Grid) -> Grid:
    """Returns the bottom half of the grid"""
    return grid[len(grid) // 2 + len(grid) % 2:]

def left_half(grid: Grid) -> Grid:
    """Returns the left half of the grid"""
    return rot270(top_half(rot90(grid)))

def right_half(grid: Grid) -> Grid:
    """Returns the right half of the grid"""
    return rot270(bottom_half(rot90(grid)))


# was vfrontier
def vertical_line(location: IntegerTuple) -> Indices:
    """ vertical line through point """
    return frozenset((i, location[1]) for i in range(30))

# was hfrontier
def horizontal_line(location: IntegerTuple) -> Indices:
    """ horizontal line through point """
    return frozenset((location[0], j) for j in range(30))


# was backdrop
def bounding_box_indices(patch: Patch) -> Indices:
    """Returns the indices inside the bounding box of a patch"""
    if len(patch) == 0:
        return frozenset({})
    indices = to_indices(patch)
    si, sj = upper_left_corner(indices)
    ei, ej = lower_right_corner(patch)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))

# was delta
def bounding_box_delta(patch: Patch) -> Indices:
    """Returns the indices within the bounding box of a patch but *not* part of the patch itself"""
    if len(patch) == 0:
        return frozenset({})
    return bounding_box_indices(patch) - to_indices(patch)

# was gravitate
def move_until_touching(source: Patch, destination: Patch) -> IntegerTuple:
    """Returns the direction to move 'source' until it is adjacent to 'destination'"""
    si, sj = center(source)
    di, dj = center(destination)
    i, j = 0, 0
    if vertical_matching(source, destination):
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


def inbox(patch: Patch) -> Indices:
    """ inbox for patch (lines 1 unit inside patch bounding box) """
    ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
    bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def outbox(patch: Patch) -> Indices:
    """ outbox for patch (lines 1 unit outside patch bounding box) """
    ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
    bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def box(patch: Patch) -> Indices:
    """ outline of patch (lines along patch bounding box) """
    if len(patch) == 0:
        return patch
    ai, aj = upper_left_corner(patch)
    bi, bj = lower_right_corner(patch)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def shoot(start: IntegerTuple, direction: IntegerTuple) -> Indices:
    """Returns the indices of a line from 'start' towards 'direction'"""
    return line_between(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))


def occurrences(grid: Grid, obj: Object) -> Indices:
    """Returns the locations of occurrences of 'obj' in 'grid'"""
    occs = set()
    normed = shift_to_origin(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = get_shape(obj)
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

# was frontiers
def solid_color_strips_in_grid(grid: Grid) -> Objects:
    """Returns the set of frontiers of 'grid' (i.e. horizontal and vertical lines where each line through the grid contains a single color)"""
    h, w = len(grid), len(grid[0])
    row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    column_indices = tuple(j for j, c in enumerate(diagonal_mirror(grid)) if len(set(c)) == 1)
    hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers

# was compress
def remove_solid_color_strips_from_grid(grid: Grid) -> Grid:
    """Returns 'grid' with frontiers removed (i.e. remove horizontal and vertical lines from the grid where each line through the grid contains a single color)"""
    ri = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)                  # Find unique rows
    ci = tuple(j for j, c in enumerate(diagonal_mirror(grid)) if len(set(c)) == 1) # Find unique columns
    return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(grid) if i not in ri)


def horizontal_periodicity(obj: Object) -> Integer:
    """ horizontal periodicity """
    normalized = shift_to_origin(obj)
    w = get_width(normalized)
    for p in range(1, w):
        offsetted = shift_by_vector(normalized, (0, -p))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
        if pruned.issubset(normalized):
            return p
    return w

def vertical_periodicity(obj: Object) -> Integer:
    """ vertical periodicity """
    normalized = shift_to_origin(obj)
    h = get_height(normalized)
    for p in range(1, h):
        offsetted = shift_by_vector(normalized, (-p, 0))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
        if pruned.issubset(normalized):
            return p
    return h
