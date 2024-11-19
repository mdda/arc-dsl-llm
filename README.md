# Domain Specific Language for the Abstraction and Reasoning Corpus (ARC-DSL-LLM)
## Updated (from [`arc-dsl`](https://github.com/michaelhodel/arc-dsl/)) to be LLM-legible

The original DSL (released as `arc-dsl`) was created with the aim of 
being expressive enough to allow programs solving arbitrary ARC tasks, 
and generic, i.e. consisting of only few primitives, each useful for many tasks (see [`dsl.py`](dsl.py)). 
As a proof of concept, solver programs for the training tasks were written (see [`solvers.py`](solvers.py)). 
See Hodel's [`arc_dsl_writeup.pdf`](https://github.com/michaelhodel/arc-dsl/blob/main/arc_dsl_writeup.pdf) 
for a more detailed description of the original work.


## `arc-dsl-llm` and LLM-legibility

There were several kinds of changes made to the original `arc-dsl` to make it more LLM-legible (and, frankly, more human-legible).  

The following are the most significant updates made:

* Significantly updating the DSL function names to be more LLM-friendly (see below for a list)
  + A motivating example : `fork(outer,a,b)` is more 'legible' when named `combine_two_function_results(outer,f1,f2)`
* Rectifying the use of `COLOR_X` constants: 
  + Remove implicit assumptions that `COLOR_BLACK==0` or `COLOR_BLACK<COLOR_RED` (for instance)
  + Add additional `COLOR_BELOW` (defined to be numerically smaller than other colors) that allows for `sort` to behave in the way expected by several solutions
  + Remove usage of `COLOR_X` to represent small integers (i.e. non-colors).  This was frustrating.
  + Remove calculation of `COLOR_X` values by (for instance) doubling other `COLOR_Y` values (!)
* Ensuring that `python -m arc_dsl.main` runs cleanly (running the DSL tests and proving the solutions on the test examples)
  + NB: the code is up-to-date (with all 400 training-set solutions passing)
* Adding correct type-hinting so that `pyright solvers.py` executes cleanly
* Allowing the code to run as an imported module (without moving the files around - the change history is preserved)


## Example solver program for task `00d62c1b` written in the DSL

![Task 00d62c1b](00d62c1b.png)

### Taken from the current `arc-dsl` repo

```python
def solve_00d62c1b(I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = mfilter(x2, x4)
    O = fill(I, FOUR, x5)    
    return O
```

### The `arc-dsl-llm` version

As given in `solvers.py`:
```python
def solve_00d62c1b(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = fix_last_argument(bordering, I)
    x4 = compose(logical_not, x3)
    x5 = keep_if_condition_and_flatten(x2, x4)
    O = fill(I, COLOR_FOUR, x5)
```
NB: parameter name annotations can be added (as in the original Hodel repo) automatically, 
since the format of the function definition / documentation is now uniform.


## Another solver example: `5521c0d9`

![Task 5521c0d9](5521c0d9.png)

### Taken from the current `arc-dsl` repo
```python
def solve_5521c0d9(I):
    x1 = objects(I, T, F, T)
    x2 = merge(x1)
    x3 = cover(I, x2)
    x4 = chain(toivec, invert, height)
    x5 = fork(shift, identity, x4)
    x6 = mapply(x5, x1)
    O = paint(x3, x6)
    return O
```

### The `arc-dsl-llm` version

As given in `solvers.py`:
```python
def solve_5521c0d9(I):
    x1 = as_objects(I, True, False, True)
    x2 = flatten(x1)
    x3 = erase_patch(I, x2)
    x4 = chain(to_vertical_vec, negate, get_height)
    x5 = combine_two_function_results(shift_by_vector, identity, x4)
    x6 = transform_and_flatten(x5, x1)
    O = paint_onto_grid(x3, x6)
    return O
```


## Installation

There are very minimal requirements :
```bash
uv pip install tqdm
```


## DSL function name changes (`arc-dsl` &rarr; `arc-dsl-llm`)

Hopefully, it will be clear to the reader that the RHS replacements should be much more 'LLM-legible' than the original LHS.

| `arc-dsl` original | `arc-dsl-llm` new |
| ------ | ------ | 
| invert | negate |
| combine | union |
| dedupe | remove_duplicates |
| order | sort |
|  |  |
| even | is_even |
| positive | is_positive |
| equality | is_equal |
| greater | is_greater |
| portrait | is_portrait |
| square | is_square |
| vfrontier | is_vertical_line |
| hfrontier | is_horizontal_line |
|  |  |
| color | get_color |
| width | get_width |
| height | get_height |
| shape | get_shape |
|  |  |
| first | get_first |
| last | get_last |
| other | get_other |
|  |  |
| both | logical_and |
| either | logical_or |
| flip | logical_not |
|  |  |
| hmirror | horizontal_mirror |
| vmirror | vertical_mirror |
| dmirror | diagonal_mirror |
| cmirror | counterdiagonal_mirror |
|  |  |
| hupscale | horizontal_upscale |
| vupscale | vertical_upscale |
|  |  |
| hconcat | horizontal_concat |
| vconcat | vertical_concat |
|  |  |
| hsplit | horizontal_split |
| vsplit | vertical_split |
|  |  |
| location | color_at_location |
| connect | line_between |
|  |  |
| subgrid | smallest_subgrid_containing |
| extract | extract_first_matching |
|  |  |
| colorcount | color_count |
| colorfilter | color_filter |
| sizefilter | size_filter |
|  |  |
| ulcorner | upper_left_corner |
| urcorner | upper_right_corner |
| llcorner | lower_left_corner |
| lrcorner | lower_right_corner |
|  |  |
| product | cartesian_product |
|  |  |
| sfilter | keep_if_condition |
| mfilter | keep_if_condition_and_merge |
|  |  |
| apply | transform |
| mapply | transform_and_flatten |
| papply | transform_both |
| mpapply | transform_both_and_flatten |
| rapply | apply_each_function |
| prapply | apply_function_on_cartesian_product |
|  |  |
| extract | extract_first_matching |
| branch | condition_if_else |
| fork | combine_two_function_results |
|  |  |
| matcher | equals |
|  |  |
| hvec | to_horizontal_vec |
| vvec | to_vertical_vec |
|  |  |
| shift | shift_by_vector |
| normalize | shift_to_origin |
| gravitate | move_until_touching |
|  |  |
| neighbors | direct_neighbors |
| dneighbors | diagonal_neighbors |
|  |  |
| vfrontier | vertical_frontier |
| hfrontier | horizontal_frontier |
|  |  |
| vmatching | vertical_matching |
| hmatching | horizontal_matching |
|  |  |
| fgpartition | partition_only_foreground |
|  |  |
| mostcolor | most_common_color |
| leastcolor | least_common_color |
|  |  |
| manhattan | manhattan_distance |
| *new* | as_generic_tuple |
| *new* | make_cell |
|  |  |
| backdrop | bounding_box_indices |
| delta | bounding_box_delta |
|  |  |
| paint | paint_onto_grid |
| underpaint | paint_onto_grid_background |
|  |  |
| canvas | create_grid |
| cover | erase_patch |
| trim | trim_border |
| move | move_object |
|  |  |
| frontiers | solid_color_strips_in_grid |
| compress | remove_solid_color_strips_from_grid |
|  |  |
| T | True |
| F | False |



## Citing this work

The following paper includes a more detailed description of the updates made from `arc-dsl` to `arc-dsl-llm` in Appendix A:

```bibtex
@misc{andrews2024capturingsparksabstractionarc,
      title={Capturing Sparks of Abstraction for the ARC Challenge}, 
      author={Martin Andrews},
      year={2024},
      eprint={2411.11206},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.11206}, 
}
```

### Acknowledgements

Support for this research was provided by the Google AI/ML Developer Programs team,
including access to the Gemini models and GPUs on Google Cloud Platform. 
