from .dsl import *


A = ((1, 0), (0, 1), (1, 0))
B = ((2, 1), (0, 1), (2, 1))
C = ((3, 4), (5, 5))
D = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
E = ((1, 2), (4, 5))
F = ((5, 6), (8, 0))
G = ((1, 0, 0, 0, 3), (0, 1, 1, 0, 0), (0, 1, 1, 2, 0), (0, 0, 2, 2, 0), (0, 2, 0, 0, 0))
H = ((0, 0, 0, 0, 0), (0, 2, 0, 2, 0), (2, 0, 0, 2, 0), (0, 0, 0, 0, 0), (0, 0, 2, 0, 0))
I = ((0, 0, 2, 0, 0), (0, 2, 0, 2, 0), (2, 0, 0, 2, 0), (0, 2, 0, 2, 0), (0, 0, 2, 0, 0))
J = ((0, 0, 2, 0, 0), (0, 2, 0, 2, 0), (0, 0, 2, 2, 0), (0, 2, 0, 2, 0), (0, 0, 2, 0, 0))
K = ((0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0))


def test_identity():
    assert identity(1) == 1
 

def test_add():
    assert add(1, 2) == 3
    assert add(4, 6) == 10
 

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(4, 6) == -2
 

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 3) == 12
 

def test_divide():
    assert divide(4, 2) == 2
    assert divide(9, 2) == 4
 

def test_negate():
    assert negate(1) == -1
    assert negate(-4) == 4
 

def test_is_even():
    assert not is_even(1)
    assert is_even(2)
 

def test_double():
    assert double(1) == 2
 

def test_halve():
    assert halve(2) == 1
    assert halve(5) == 2
 

def test_logical_not():
    assert logical_not(False)
    assert not logical_not(True)
 

def test_is_equal():
    assert is_equal(A, A)
    assert not is_equal(A, B)
 

def test_contains():
    assert contains(1, (1, 3))
    assert not contains(2, {3, 4})
 

def test_union():
    assert union(frozenset({1, 2}), frozenset({3, 4})) == frozenset({1, 2, 3, 4})
    assert union((1, 2), (3, 4)) == (1, 2, 3, 4)
 

def test_intersection():
    assert intersection(frozenset({1, 2}), frozenset({2, 3})) == frozenset({2})
 

def test_difference():
    assert difference(frozenset({1, 2, 3}), frozenset({1, 2})) == frozenset({3})
 

def test_remove_duplicates():
    assert remove_duplicates((1, 2, 3, 3, 2, 4, 1)) == (1, 2, 3, 4)
 

def test_sort():
    assert sort(((1,), (1, 2, 3), (1, 2)), len) == ((1,), (1, 2), (1, 2, 3))
    assert sort((1, 4, -3), abs) == (1, -3, 4)
 

def test_repeat():
    assert repeat(C, 3) == (C, C, C)
 

def test_greater_than():
    assert greater_than(2, 1)
    assert not greater_than(4, 10)
 

def test_size():
    assert size((1, 2, 3)) == 3
    assert size(frozenset({2, 5})) == 2
 

def test_flatten():
    assert flatten(frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == frozenset({(1, (0, 0)), (1, (1, 1)), (1, (0, 1))})
    assert flatten(((1, 2), (3, 4, 5))) == (1, 2, 3, 4, 5)
    assert flatten(((4, 5), (7,))) == (4, 5, 7)
 

def test_maximum():
    assert maximum({1, 2, 5, 3}) == 5
    assert maximum((4, 2, 6)) == 6
 

def test_minimum():
    assert minimum({1, 2, 5, 3}) == 1
    assert minimum((4, 2, 6)) == 2
 

def test_valmax():
    assert valmax(((1,), (1, 2)), len) == 2
 

def test_valmin():
    assert valmin(((1,), (1, 2)), len) == 1
 

def test_argmax():
    assert argmax(((1,), (1, 2)), len) == (1, 2)
 

def test_argmin():
    assert argmin(((1,), (1, 2)), len) == (1,)
 

def test_most_common():
    assert most_common((1, 2, 2, 3, 3, 3)) == 3
 

def test_least_common():
    assert least_common((1, 2, 3, 4, 2, 3, 4)) == 1
 

def test_initset():
    assert initset(2) == frozenset({2})
 

def test_logical_and():
    assert not logical_and(True, False)
    assert logical_and(True, True)
    assert not logical_and(False, False)
 

def test_logical_or():
    assert logical_or(True, False)
    assert logical_or(True, True)
    assert not logical_or(False, False)
 

def test_increment():
    assert increment(1) == 2
 

def test_decrement():
    assert decrement(1) == 0
 

def test_crement():
    assert crement(1) == 2
    assert crement(-2) == -3
 

def test_sign():
    assert sign(2) == 1
    assert sign(0) == 0
    assert sign(-1) == -1
 

def test_is_positive():
    assert is_positive(1)
    assert not is_positive(-2)
 

def test_to_vertical_vec():
    assert to_vertical_vec(2) == (2, 0)
 

def test_to_horizontal_vec():
    assert to_horizontal_vec(3) == (0, 3)
 

def test_keep_if_condition():
    assert keep_if_condition((1, 2, 3), lambda x: x > 1) == (2, 3)
    assert keep_if_condition(frozenset({2, 3, 4}), lambda x: x % 2 == 0) == frozenset({2, 4})
 

def test_keep_if_condition_and_flatten():
    assert keep_if_condition_and_flatten(frozenset({frozenset({(2, (3, 3))}), frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})}), lambda x: len(x) == 1) == frozenset({(1, (0, 0)), (2, (3, 3))})
 

def test_extract_first_matching():
    assert extract_first_matching((1, 2, 3), lambda x: x > 2) == 3
    assert extract_first_matching(frozenset({2, 3, 4}), lambda x: x % 4 == 0) == 4
 

def test_to_tuple():
    assert to_tuple({1}) == (1,)
 

def test_get_first():
    assert get_first((2, 3)) == 2
 

def test_get_last():
    assert get_last((2, 3)) == 3
 

def test_insert():
    assert insert(1, frozenset({2})) == frozenset({1, 2})
 

def test_remove():
    assert remove(1, frozenset({1, 2})) == frozenset({2})
 

def test_get_other():
    assert get_other({1, 2}, 1) == 2
 

def test_interval():
    assert interval(1, 4, 1) == (1, 2, 3)
    assert interval(5, 2, -1) == (5, 4, 3)
 

def test_as_tuple():
    assert as_tuple(3, 4) == (3, 4)
 
def test_as_generic_tuple():  # mdda added  - needed instead of as_tuple(Grid, Grid), etc
    pass 
def test_make_cell():  # mdda added - needed instead of as_tuple(Color, IntegerTuple)
    pass 

def test_cartesian_product():
    assert cartesian_product({1, 2}, {2, 3}) == frozenset({(1, 2), (1, 3), (2, 2), (2, 3)})
 

def test_pairwise():
    assert pairwise((1, 2), (4, 3)) == ((1, 4), (2, 3))
 

def test_condition_if_else():
    assert condition_if_else(True, 1, 3) == 1
    assert condition_if_else(False, 4, 2) == 2
 

def test_compose():
    assert compose(lambda x: x ** 2, lambda x: x + 1)(2) == 9
    assert compose(lambda x: x + 1, lambda x: x ** 2)(2) == 5
 

def test_chain():
    assert chain(lambda x: x + 3, lambda x: x ** 2, lambda x: x + 1)(2) == 12
 

def test_equals():
    assert equals(lambda x: x + 1, 3)(2)
    assert not equals(lambda x: x - 1, 3)(2)
 

def test_fix_last_argument():
    assert fix_last_argument(lambda a, b: a + b, 2)(3) == 5
    assert fix_last_argument(lambda a, b: a == b, 2)(2)
 

def test_fix_first_argument():
    assert fix_first_argument(lambda a, b: a + b, 2)(3) == 5
    assert fix_first_argument(lambda a, b: a == b, 2)(2)
 

def test_power():
    assert power(lambda x: x + 1, 3)(4) == 7
 

def test_combine_two_function_results():
    assert combine_two_function_results(lambda x, y: x * y, lambda x: x + 1, lambda x: x + 2)(2) == 12
 

def test_transform():
    assert transform(lambda x: x ** 2, (1, 2, 3)) == (1, 4, 9)
    assert transform(lambda x: x % 2, frozenset({1, 2})) == frozenset({0, 1})
 

def test_apply_each_function():
    assert apply_each_function(frozenset({lambda x: x + 1, lambda x: x - 1}), 1) == {0, 2}
 

def test_transform_and_flatten():
    assert transform_and_flatten(lambda x: frozenset({(v + 1, (i, j)) for v, (i, j) in x}), frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == frozenset({(2, (0, 0)), (2, (1, 1)), (2, (0, 1))})
 

def test_transform_both():
    assert transform_both(lambda x, y: x + y, (1, 2), (3, 4)) == (4, 6)
 

def test_transform_both_and_flatten():
    #assert transform_both_and_flatten(lambda x, y: frozenset({(x, (i, j)) for _, (i, j) in y}), (3, 4), frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == ((3, (0, 0)), (4, (1, 1)), (4, (0, 1)))
    input_tuple: tuple[int, int] = (3, 4)
    input_data: Tuple[Tuple[Cell,], Tuple[Cell, Cell]] = (
        ((1, (0, 0)),),
        ((1, (1, 1)), (1, (0, 1))),
    )
    expected: Tuple[Cell, Cell, Cell] = (
        (3, (0, 0)),
        (4, (1, 1)),
        (4, (0, 1))
    )
    computed = transform_both_and_flatten(lambda x, y: tuple((x, (i, j))
                       for _, (i, j) in y), input_tuple, input_data)
    assert computed == expected

 

def test_apply_function_on_cartesian_product():
    assert apply_function_on_cartesian_product(lambda x, y: x + y, {1, 2}, {2, 3}) == frozenset({3, 4, 5})
 

def test_most_common_color():
    assert most_common_color(B) == 1
    assert most_common_color(C) == 5
 

def test_least_common_color():
    assert least_common_color(B) == 0
 

def test_get_height():
    assert get_height(A) == 3
    assert get_height(C) == 2
    assert get_height(frozenset({(0, 4)})) == 1
    assert get_height(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 3
 

def test_get_width():
    assert get_width(A) == 2
    assert get_width(C) == 2
    assert get_width(frozenset({(0, 4)})) == 1
    assert get_width(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 3
 

def test_get_shape():
    assert get_shape(A) == (3, 2)
    assert get_shape(C) == (2, 2)
    assert get_shape(frozenset({(0, 4)})) == (1, 1)
    assert get_shape(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == (3, 3)
 

def test_is_portrait():
    assert is_portrait(A)
    assert not is_portrait(C)
 

def test_color_count():
    assert color_count(A, 1) == 3
    assert color_count(C, 5) == 2
    assert color_count(frozenset({(1, (0, 0)), (2, (1, 0)), (2, (0, 1))}), 2) == 2
    assert color_count(frozenset({(1, (0, 0)), (2, (1, 0)), (2, (0, 1))}), 1) == 1
 

def test_color_filter():
     assert color_filter(frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})}), 2) == frozenset({frozenset({(2, (4, 1))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
 

def test_size_filter():
    assert size_filter(frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})}), 1) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))})})
 

def test_as_indices():
    assert as_indices(A) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)})
    assert as_indices(C) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1)})
 

def test_of_color():
    assert of_color(A, 0) == frozenset({(0, 1), (1, 0), (2, 1)})
    assert of_color(B, 2) == frozenset({(0, 0), (2, 0)})
    assert of_color(C, 1) == frozenset()
 

def test_upper_left_corner():
    assert upper_left_corner(frozenset({(1, 2), (0, 3), (4, 0)})) == (0, 0)
    assert upper_left_corner(frozenset({(1, 2), (0, 0), (4, 3)})) == (0, 0)
 

def test_upper_right_corner():
    assert upper_right_corner(frozenset({(1, 2), (0, 3), (4, 0)})) == (0, 3)
    assert upper_right_corner(frozenset({(1, 2), (0, 0), (4, 3)})) == (0, 3)
 

def test_lower_left_corner():
    assert lower_left_corner(frozenset({(1, 2), (0, 3), (4, 0)})) == (4, 0)
    assert lower_left_corner(frozenset({(1, 5), (0, 0), (2, 3)})) == (2, 0)
 

def test_lower_right_corner():
    assert lower_right_corner(frozenset({(1, 2), (0, 3), (4, 0)})) == (4, 3)
    assert lower_right_corner(frozenset({(1, 5), (0, 0), (2, 3)})) == (2, 5)
 

def test_crop():
    assert crop(A, (0, 0), (2, 2)) == ((1, 0), (0, 1))
    assert crop(C, (0, 1), (1, 1)) == ((4,),)
    assert crop(D, (1, 2), (2, 1)) == ((6,), (0,))
 

def test_to_indices():
    assert to_indices(frozenset({(1, (1, 1)), (1, (1, 0))})) == frozenset({(1, 1), (1, 0)})
    assert to_indices(frozenset({(1, 1), (0, 1)})) == frozenset({(1, 1), (0, 1)})
 

def test_recolor():
    assert recolor(3, frozenset({(2, (0, 0)), (1, (0, 1)), (5, (1, 0))})) == frozenset({(3, (0, 0)), (3, (0, 1)), (3, (1, 0))})
    assert recolor(2, frozenset({(2, (2, 5)), (2, (1, 1))})) == frozenset({(2, (2, 5)), (2, (1, 1))})
 

def test_shift_by_vector():
    assert shift_by_vector(frozenset({(2, (1, 1)), (4, (1, 2)), (1, (2, 3))}), (1, 2)) == frozenset({(2, (2, 3)), (4, (2, 4)), (1, (3, 5))})
    assert shift_by_vector(frozenset({(1, 3), (0, 2), (3, 4)}), (0, -1)) == frozenset({(1, 2), (0, 1), (3, 3)})
 

def test_shift_to_origin():
    assert shift_to_origin(frozenset({(2, (1, 1)), (4, (1, 2)), (1, (2, 3))})) == frozenset({(2, (0, 0)), (4, (0, 1)), (1, (1, 2))})
    assert shift_to_origin(frozenset({(1, 0), (0, 2), (3, 4)})) == frozenset({(1, 0), (0, 2), (3, 4)})
 

def test_direct_neighbors():
    assert direct_neighbors((1, 1)) == frozenset({(0, 1), (1, 0), (2, 1), (1, 2)})
    assert direct_neighbors((0, 0)) == frozenset({(0, 1), (1, 0), (-1, 0), (0, -1)})
    assert direct_neighbors((0, 1)) == frozenset({(0, 0), (1, 1), (-1, 1), (0, 2)})
    assert direct_neighbors((1, 0)) == frozenset({(0, 0), (1, 1), (1, -1), (2, 0)})
 

def test_diagonal_neighbors():
    assert diagonal_neighbors((1, 1)) == frozenset({(0, 0), (0, 2), (2, 0), (2, 2)})
    assert diagonal_neighbors((0, 0)) == frozenset({(1, 1), (-1, -1), (1, -1), (-1, 1)})
    assert diagonal_neighbors((0, 1)) == frozenset({(1, 0), (1, 2), (-1, 0), (-1, 2)})
    assert diagonal_neighbors((1, 0)) == frozenset({(0, 1), (2, -1), (2, 1), (0, -1)})
 

def test_neighbors():
    assert neighbors((1, 1)) == frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)})
    assert neighbors((0, 0)) == frozenset({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)})
 

def test_as_objects():
    assert as_objects(G, True, False, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert as_objects(G, True, True, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert as_objects(G, False, False, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert as_objects(G, False, True, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2)), (2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert as_objects(G, True, False, False) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(0, (1, 0)), (0, (2, 0)), (0, (3, 0)), (0, (4, 0)), (0, (3, 1))}), frozenset({(0, (0, 1)), (0, (0, 2)), (0, (0, 3)), (0, (1, 3)), (0, (1, 4)), (0, (2, 4)), (0, (3, 4)), (0, (4, 4)), (0, (4, 3)), (0, (4, 2))})})
 

def test_partition():
    assert partition(B) == frozenset({frozenset({(0, (1, 0))}), frozenset({(2, (0, 0)), (2, (2, 0))}), frozenset({(1, (0, 1)), (1, (1, 1)), (1, (2, 1))})})
    assert partition(G) == frozenset({frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(3, (0, 4))}), frozenset({(0, (0, 1)), (0, (0, 2)), (0, (0, 3)), (0, (1, 0)), (0, (1, 3)), (0, (1, 4)), (0, (2, 0)), (0, (2, 4)), (0, (3, 0)), (0, (3, 1)), (0, (3, 4)), (0, (4, 0)), (0, (4, 2)), (0, (4, 3)), (0, (4, 4))})})
 

def test_partition_only_foreground():
    assert partition_only_foreground(B) == frozenset({frozenset({(0, (1, 0))}), frozenset({(2, (0, 0)), (2, (2, 0))})})
    assert partition_only_foreground(G) == frozenset({frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(3, (0, 4))})})
 

def test_uppermost():
    assert uppermost(frozenset({(0, 4)})) == 0
    assert uppermost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 0
 

def test_lowermost():
    assert lowermost(frozenset({(0, 4)})) == 0
    assert lowermost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 2
 

def test_leftmost():
    assert leftmost(frozenset({(0, 4)})) == 4
    assert leftmost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 0
 

def test_rightmost():
    assert rightmost(frozenset({(0, 4)})) == 4
    assert rightmost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 2
 

def test_is_square():
    assert is_square(C)
    assert is_square(D)
    assert not is_square(A)
    assert not is_square(B)
    assert not is_square(frozenset({(1, 1), (1, 0)}))
    assert is_square(frozenset({(1, 1), (0, 0), (1, 0), (0, 1)}))
    assert not is_square(frozenset({(0, 0), (1, 0), (0, 1)}))
    assert is_square(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}))
 

def test_is_vertical_line():
    assert is_vertical_line(frozenset({(1, (1, 1)), (1, (0, 1))}))
    assert not is_vertical_line(frozenset({(1, 1), (1, 0)}))
 

def test_is_horizontal_line():
    assert is_horizontal_line(frozenset({(1, (1, 1)), (1, (1, 0))}))
    assert not is_horizontal_line(frozenset({(1, 1), (0, 1)}))
 

def test_horizontal_matching():
    assert horizontal_matching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (1, 3)), (2, (1, 4))}))
    assert not horizontal_matching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (2, 3)), (2, (2, 4))}))
 

def test_vertical_matching():
    assert vertical_matching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (3, 1)), (2, (4, 1))}))
    assert not vertical_matching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (3, 2)), (2, (4, 2))}))
 

def test_manhattan_distance():
    assert manhattan_distance(frozenset({(0, 0), (1, 1)}), frozenset({(1, 2), (2, 3)})) == 1
    assert manhattan_distance(frozenset({(1, 1)}), frozenset({(2, 3)})) == 3
 

def test_adjacent():
    assert adjacent(frozenset({(0, 0)}), frozenset({(0, 1), (1, 0)}))
    assert not adjacent(frozenset({(0, 0)}), frozenset({(1, 1)}))
 

def test_bordering():
    assert bordering(frozenset({(0, 0)}), D)
    assert bordering(frozenset({(0, 2)}), D)
    assert bordering(frozenset({(2, 0)}), D)
    assert bordering(frozenset({(2, 2)}), D)
    assert not bordering(frozenset({(1, 1)}), D)
 

def test_centerofmass():
    assert centerofmass(frozenset({(0, 0), (1, 1), (1, 2)})) == (0, 1)
    assert centerofmass(frozenset({(0, 0), (1, 1), (2, 2)})) == (1, 1)
    assert centerofmass(frozenset({(0, 0), (1, 1), (0, 1)})) == (0, 0)
 

def test_palette():
    assert palette(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))})) == frozenset({1, 2, 3})
    assert palette(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == frozenset({1})
 

def test_count_colors():
    assert count_colors(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))})) == 3
    assert count_colors(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == 1
 

def test_get_color():
    assert get_color(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == 1
    assert get_color(frozenset({(2, (3, 1))})) == 2
 

def test_to_object():
    assert to_object(frozenset({(0, 0), (0, 2)}), G) == frozenset({(1, (0, 0)), (0, (0, 2))})
    assert to_object(frozenset({(0, 4)}), G) == frozenset({(3, (0, 4))})
 

def test_as_object():
    assert as_object(A) == frozenset({(0, (0, 1)), (0, (1, 0)), (0, (2, 1)), (1, (0, 0)), (1, (1, 1)), (1, (2, 0))})
 

def test_rot90():
    assert rot90(B) == ((2, 0, 2), (1, 1, 1))
    assert rot90(C) == ((5, 3), (5, 4))
 

def test_rot180():
    assert rot180(B) == ((1, 2), (1, 0), (1, 2))
    assert rot180(C) == ((5, 5), (4, 3))
 

def test_rot270():
    assert rot270(B) == ((1, 1, 1), (2, 0, 2))
    assert rot270(C) == ((4, 5), (3, 5))
 

def test_horizontal_mirror():
    assert horizontal_mirror(B) == ((2, 1), (0, 1), (2, 1))
    assert horizontal_mirror(C) == ((5, 5), (3, 4))
    assert horizontal_mirror(frozenset({(0, 0), (1, 1)})) == frozenset({(1, 0), (0, 1)})
    assert horizontal_mirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(1, 0), (0, 1), (0, 0)})
    assert horizontal_mirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 2), (1, 1)})
 

def test_vertical_mirror():
    assert vertical_mirror(B) == ((1, 2), (1, 0), (1, 2))
    assert vertical_mirror(C) == ((4, 3), (5, 5))
    assert vertical_mirror(frozenset({(0, 0), (1, 1)})) == frozenset({(1, 0), (0, 1)})
    assert vertical_mirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(1, 0), (1, 1), (0, 1)})
    assert vertical_mirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 2), (1, 1)})
 

def test_diagonal_mirror():
    assert diagonal_mirror(B) == ((2, 0, 2), (1, 1, 1))
    assert diagonal_mirror(C) == ((3, 5), (4, 5))
    assert diagonal_mirror(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (1, 1)})
    assert diagonal_mirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(0, 1), (1, 1), (0, 0)})
    assert diagonal_mirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 1), (1, 2)})
 

def test_counterdiagonal_mirror():
    assert counterdiagonal_mirror(B) == ((1, 1, 1), (2, 0, 2))
    assert counterdiagonal_mirror(C) == ((5, 4), (5, 3))
    assert counterdiagonal_mirror(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (1, 1)})
    assert counterdiagonal_mirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(0, 0), (1, 0), (1, 1)})
    assert counterdiagonal_mirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 1), (1, 2)})
 

def test_fill():
    assert fill(B, 3, frozenset({(0, 0), (1, 1)})) == ((3, 1), (0, 3), (2, 1))
    assert fill(C, 1, frozenset({(1, 0)})) == ((3, 4), (1, 5))
 

def test_paint_onto_grid():
    assert paint_onto_grid(B, frozenset({(1, (0, 0)), (2, (1, 1))})) == ((1, 1), (0, 2), (2, 1))
    assert paint_onto_grid(C, frozenset({(6, (1, 0))})) == ((3, 4), (6, 5))
 

def test_fill_background():
    assert fill_background(C, 1, frozenset({(0, 0), (1, 0)})) == ((3, 4), (1, 5))
 

def test_paint_onto_grid_background():
    assert paint_onto_grid_background(B, frozenset({(3, (0, 0)), (3, (1, 1))})) == ((2, 1), (0, 3), (2, 1))
    assert paint_onto_grid_background(C, frozenset({(3, (1, 1))})) == ((3, 4), (5, 3))
 

def test_horizontal_upscale():
    assert horizontal_upscale(B, 1) == B
    assert horizontal_upscale(C, 1) == C
    assert horizontal_upscale(B, 2) == ((2, 2, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1))
    assert horizontal_upscale(C, 2) == ((3, 3, 4, 4), (5, 5, 5, 5))
 

def test_vertical_upscale():
    assert vertical_upscale(B, 1) == B
    assert vertical_upscale(C, 1) == C
    assert vertical_upscale(B, 2) == ((2, 1), (2, 1), (0, 1), (0, 1), (2, 1), (2, 1))
    assert vertical_upscale(C, 2) == ((3, 4), (3, 4), (5, 5), (5, 5))
 

def test_upscale():
    assert upscale(B, 1) == B
    assert upscale(C, 1) == C
    assert upscale(B, 2) == ((2, 2, 1, 1), (2, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1))
    assert upscale(C, 2) == ((3, 3, 4, 4), (3, 3, 4, 4), (5, 5, 5, 5), (5, 5, 5, 5))
    assert upscale(frozenset({(3, (0, 1)), (4, (1, 0)), (5, (1, 1))}), 2) == frozenset({(3, (0, 2)), (3, (0, 3)), (3, (1, 2)), (3, (1, 3)), (4, (2, 0)), (4, (3, 0)), (4, (2, 1)), (4, (3, 1)), (5, (2, 2)), (5, (3, 2)), (5, (2, 3)), (5, (3, 3))})
    assert upscale(frozenset({(3, (0, 0))}), 2) == frozenset({(3, (0, 0)), (3, (1, 0)), (3, (0, 1)), (3, (1, 1))})
 

def test_downscale():
    assert downscale(B, 1) == B
    assert downscale(C, 1) == C
    assert downscale(((2, 2, 1, 1), (2, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1)), 2) == B
    assert downscale(((3, 3, 4, 4), (3, 3, 4, 4), (5, 5, 5, 5), (5, 5, 5, 5)), 2) == C
 

def test_horizontal_concat():
    assert horizontal_concat(A, B) == ((1, 0, 2, 1), (0, 1, 0, 1), (1, 0, 2, 1))
    assert horizontal_concat(B, A) == ((2, 1, 1, 0), (0, 1, 0, 1), (2, 1, 1, 0))
 

def test_vertical_concat():
    assert vertical_concat(A, B) == ((1, 0), (0, 1), (1, 0), (2, 1), (0, 1), (2, 1))
    assert vertical_concat(B, A) == ((2, 1), (0, 1), (2, 1), (1, 0), (0, 1), (1, 0))
    assert vertical_concat(B, C) == ((2, 1), (0, 1), (2, 1), (3, 4), (5, 5))
 

def test_smallest_subgrid_containing():
    assert smallest_subgrid_containing(frozenset({(3, (0, 0))}), C) == ((3,),)
    assert smallest_subgrid_containing(frozenset({(5, (1, 0)), (5, (1, 1))}), C) == ((5, 5),)
    assert smallest_subgrid_containing(frozenset({(2, (0, 1)), (4, (1, 0))}), D) == ((1, 2), (4, 5))
    assert smallest_subgrid_containing(frozenset({(1, (0, 0)), (0, (2, 2))}), D) == D
 

def test_horizontal_split():
    assert horizontal_split(B, 1) == (B,)
    assert horizontal_split(B, 2) == (((2,), (0,), (2,)), ((1,), (1,), (1,)))
    assert horizontal_split(C, 1) == (C,)
    assert horizontal_split(C, 2) == (((3,), (5,)), ((4,), (5,)))
 

def test_vertical_split():
    assert vertical_split(B, 1) == (B,)
    assert vertical_split(B, 3) == (((2, 1),), ((0, 1),), ((2, 1),))
    assert vertical_split(C, 1) == (C,)
    assert vertical_split(C, 2) == (((3, 4),), ((5, 5),))
 

def test_cellwise():
    assert cellwise(A, B, 0) == ((0, 0), (0, 1), (0, 0))
    assert cellwise(C, E, 0) == ((0, 0), (0, 5))
 

def test_replace():
    assert replace(B, 2, 3) == ((3, 1), (0, 1), (3, 1))
    assert replace(C, 5, 0) == ((3, 4), (0, 0))
 

def test_switch():
    assert switch(C, 3, 4) == ((4, 3), (5, 5))
 

def test_center():
    assert center(frozenset({(1, (0, 0))})) == (0, 0)
    assert center(frozenset({(1, (0, 0)), (1, (0, 2))})) == (0, 1)
    assert center(frozenset({(1, (0, 0)), (1, (0, 2)), (1, (2, 0)), (1, (2, 2))})) == (1, 1)
 

def test_position():
    assert position(frozenset({(0, (1, 1))}), frozenset({(0, (2, 2))})) == (1, 1)
    assert position(frozenset({(0, (2, 2))}), frozenset({(0, (1, 2))})) == (-1, 0)
    assert position(frozenset({(0, (3, 3))}), frozenset({(0, (3, 4))})) == (0, 1)
 

def test_color_at_location():
    assert color_at_location(C, (0, 0)) == 3
    assert color_at_location(D, (1, 2)) == 6
 

def test_create_grid():
    assert create_grid(3, (1, 2)) == ((3, 3),)
    assert create_grid(2, (3, 1)) == ((2,), (2,), (2,))
 

def test_corner_indices():
    assert corner_indices(frozenset({(1, 2), (0, 3), (4, 0)})) == frozenset({(0, 0), (0, 3), (4, 0), (4, 3)})
    assert corner_indices(frozenset({(1, 2), (0, 0), (4, 3)})) == frozenset({(0, 0), (0, 3), (4, 0), (4, 3)})
 

def test_line_between():
    assert line_between((1, 1), (2, 2)) == frozenset({(1, 1), (2, 2)})
    assert line_between((1, 1), (1, 4)) == frozenset({(1, 1), (1, 2), (1, 3), (1, 4)})
 

def test_erase_patch():
    assert erase_patch(C, frozenset({(0, 0)})) == ((5, 4), (5, 5))
 

def test_trim_border():
    assert trim_border(D) == ((5,),)
 

def test_move_object():
    assert move_object(C, frozenset({(3, (0, 0))}), (1, 1)) == ((5, 4), (5, 3))
 

def test_top_half():
    assert top_half(C) == ((3, 4),)
    assert top_half(D) == ((1, 2, 3),)
 

def test_bottom_half():
    assert bottom_half(C) == ((5, 5),)
    assert bottom_half(D) == ((7, 8, 0),)
 

def test_left_half():
    assert left_half(C) == ((3,), (5,))
    assert left_half(D) == ((1,), (4,), (7,))
 

def test_right_half():
    assert right_half(C) == ((4,), (5,))
    assert right_half(D) == ((3,), (6,), (0,))
 

def test_vertical_line():
    assert vertical_line((3, 4)) == frozenset({(i, 4) for i in range(30)})
 

def test_horizontal_line():
    assert horizontal_line((3, 4)) == frozenset({(3, i) for i in range(30)})
 

def test_bounding_box_indices():
    assert bounding_box_indices(frozenset({(2, 3), (3, 2), (3, 3), (4, 1)})) == frozenset({(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3),})
 

def test_bounding_box_delta():
    assert bounding_box_delta(frozenset({(2, 3), (3, 2), (3, 3), (4, 1)})) == frozenset({(2, 1), (2, 2), (3, 1), (4, 2), (4, 3)})
 

def test_move_until_touching():
    assert move_until_touching(frozenset({(0, 0)}), frozenset({(0, 1)})) == (0, 0)
    assert move_until_touching(frozenset({(0, 0)}), frozenset({(0, 4)})) == (0, 3)
 

def test_inbox():
    assert inbox(frozenset({(0, 0), (2, 2)})) == frozenset({(1, 1)})
 

def test_outbox():
    assert outbox(frozenset({(1, 1)})) == frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)})
 

def test_box():
    assert box(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1)})
 

def test_shoot():
    assert shoot((0, 0), (1, 1)) == frozenset({(i, i) for i in range(43)})
 

def test_occurrences():
    assert occurrences(G, frozenset({(1, (0, 0)), (1, (0, 1))})) == frozenset({(1, 1), (2, 1)})
 

def test_solid_color_strips_in_grid():
    assert solid_color_strips_in_grid(C) == frozenset({frozenset({(5, (1, 0)), (5, (1, 1))})})
 

def test_remove_solid_color_strips_from_grid():
    assert remove_solid_color_strips_from_grid(K) == ((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0))
 

def test_horizontal_periodicity():
    assert horizontal_periodicity(frozenset({(8, (2, 1)), (8, (1, 3)), (2, (2, 4)), (8, (2, 3)), (2, (2, 2)), (2, (1, 2)), (8, (1, 1)), (8, (1, 5)), (2, (1, 4)), (8, (2, 5)), (2, (2, 0)), (2, (1, 0))})) == 2
    assert horizontal_periodicity(frozenset({(2, (2, 6)), (2, (2, 0)), (3, (2, 4)), (3, (2, 2)), (3, (2, 5)), (2, (2, 3)), (3, (2, 1))})) == 3
 

def test_vertical_periodicity():
    assert vertical_periodicity(frozenset({(2, (2, 6)), (2, (2, 0)), (3, (2, 4)), (3, (2, 2)), (3, (2, 5)), (2, (2, 3)), (3, (2, 1))})) == 1
    assert vertical_periodicity(frozenset({(1, (2, 6)), (2, (3, 5)), (2, (3, 0)), (2, (2, 2)), (2, (2, 7)), (1, (3, 4)), (2, (2, 1)), (1, (2, 3)), (2, (2, 5)), (2, (2, 4)), (1, (3, 7)), (1, (2, 0)), (2, (3, 6)), (2, (3, 2)), (2, (3, 3)), (1, (3, 1))})) == 2
