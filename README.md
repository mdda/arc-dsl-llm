# Domain Specific Language for the Abstraction and Reasoning Corpus (ARC-DSL)

The DSL was created with the aim of being expressive enough to allow programs solving arbitrary ARC tasks, and generic, i.e. consisting of only few primitives, each useful for many tasks (see [`dsl.py`](dsl.py)). As a proof of concept, solver programs for the training tasks were written (see [`solvers.py`](solvers.py)). See [`arc_dsl_writeup.pdf`](arc_dsl_writeup.pdf) for a more detailed description of the work.


## Example solver program for task 00d62c1b written in the DSL

![Task 00d62c1b](00d62c1b.png)

```python
def solve_00d62c1b(I):
    objs = objects(grid=I, univalued=T, diagonal=F, without_bg=F)
    black_objs = colorfilter(objs=objs, value=ZERO)
    borders = rbind(function=bordering, fixed=I)
    does_not_border = compose(outer=flip, inner=borders)
    enclosed = mfilter(container=black_objs, function=does_not_border)
    O = fill(grid=I, value=FOUR, patch=enclosed)
    return O
```

The function `solve_00d62c1b` takes an input grid `I` and returns the correct output grid `O`. An explanation of what the variables store and how their values were computed:

- `objs`: the set of objects extracted from the input grid `I` that are single-color only, where individual objects may only have cells that are connected directly, and cells may be of the background color (black); the result of calling the `objects` primitive on `I` with `univalued=True`, `diagonal=False` and `without_background=True`
- `black_objs`: the subset of the objects `objs` which are black; the result of filtering objects by their color, i.e. calling `colorfilter` with `objects=objs` and `color=ZERO` (black)
- `borders`: a function taking an object and returning `True` iff that object is at the border of the grid; the result of fixing the right argument of the `bordering` primitive to `I` by calling the function `rbind` on `function=bordering` and `fixed=I`
- `does_not_border`: a function that returns the inverse of the previous function, i.e. a function that returns `True` iff an object does not touch the grid border; the result of composing the `flip` primitive (which simply negates a boolean) and `borders`
- `enclosed`: a single object defined as the union of objects `black_objs` for which function `does_not_border` returns `True`, i.e. the black objects which do not touch the grid border (corresponding to the "holes" in the green objects); the result of calling `mfilter` (which combines `merge` and `filter`) with `container=black_objs` and `condition=does_not_border`
- `O`: the output grid, created by coloring all pixels of the object `enclosed` yellow; the result of calling the `fill` primitive on `I` with `color=FOUR` (yellow) and `patch=enclosed`


## Another solver example: 5521c0d9

![Task 5521c0d9](5521c0d9.png)

```python
def solve_5521c0d9(I):
    objs = objects(grid=I, univalued=T, diagonal=F, without_bgT)
    foreground = merge(containers=objs)
    empty_grid = cover(grid=I, patch=foreground)
    offset_getter = chain(h=toivec, g=invert, f=height)
    shifter = fork(outer=shift, a=identity, b=offset_getter)
    shifted = mapply(function=shifter, container=objs)
    O = paint(grid=empty_grid, obj=shifted)
    return O
```

- `objs`: the set of objects extracted from the input grid `I` that are single-color only, ignoring the background color; the result of calling the `objects` primitive on `I` with `univalued=True`, `diagonal=False` and `without_background=True`
- `foreground`: all the objects treated as a single object, the result of calling the `merge` primitive on the objects `objs`
- `empty_grid`: a new grid, where `foreground` is removed (covered), i.e. replaced with the background color (black); the result of calling the `cover` primitive with `grid=I` and `patch=foreground`
- `offset_getter`: a function that takes an object and returns a vector pointing up by as much as that object is high; the result of composing the three functions `toivec`, `invert` and `height`; the result of calling the `chain` primitive with `h=toivec`, `g=invert` and `f=height`
- `shifter`: a function that takes an object and shifts it as much upwards as it is high; the result of calling the `fork` primitive with `outer=shift`, `a=identity` and `b=offset_getter`
- `shifted`: all the objects shifted up by their heights, as a single object, obtained by appling the constructed function on the set of objects and merging the results; the result of calling the `mapply` primitive on `function=shifter` and `container=objs`
- `O` the desired output grid, obtained by painting the resulting object onto the grid `empty_grid` where the original objects were removed from; the result of calling the `paint` primitive on `grid=empty_grid` and `obj=shifted`




Changes made



invert      negate
combine     union
dedupe      remove_duplicates
order       sort

even        is_even
positive    is_positive
equality    is_equal
greater     is_greater
portrait    is_portrait
square      is_square
            is_vertical_line
            is_horizontal_line

first       get_first
last        get_last
other       get_other

both        logical_and
either      logical_or
            logical_not

hmirror     horizontal_mirror
vmirror     vertical_mirror
?dmirror     diagonal_mirror
?cmirror     counterdiagonal_mirror

            horizontal_upscale
            vertical_upscale

hconcat     horizontal_concat
vconcat     vertical_concat

hsplit      horizontal_split
vsplit      vertical_split

location    color_at_location
            line_between

subgrid     smallest_subgrid_containing
extract     extract_first_matching

            color_count
            color_filter
            size_filter

ulcorner    upper_left_corner
urcorner    upper_right_corner
llcorner    lower_left_corner
lrcorner    lower_right_corner

product     cartesian_product

sfilter     keep_if_condition
mfilter     keep_if_condition_and_merge

apply       transform
mapply      transform_and_flatten
papply      transform_both  
mpapply     transform_both_and_flatten apply_to_both_and_merge
rapply      apply_each_function
prapply     apply_function_on_cartesian_product(

            extract_first_matching
branch      condition_if_else
fork        combine_two_function_results

matcher     equals

hvec        to_horizontal_vec
vvec        to_vertical_vec

shift       shift_by_vector
normalize   shift_to_origin

            direct_neighbors
            diagonal_neighbors

vfrontier   vertical_frontier
hfrontier   horizontal_frontier

vmatching   vertical_matching
hmatching   horizontal_matching


fgpartition partition_only_foreground

mostcolor   most_common_color
leastcolor  least_common_color

manhattan   manhattan_distance
            as_generic_tuple
            make_cell

backdrop    bounding_box_indices
delta       bounding_box_delta
            
canvas      create_grid
cover       erase_patch
trim        trim_border
move        move_object

T           True
F           False

