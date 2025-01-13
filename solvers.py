from .dsl import *
from .constants import *


def solve_67a3c6ac(I):
    O = vertical_mirror(I)
    return O


def solve_68b16354(I):
    O = horizontal_mirror(I)
    return O


def solve_74dd1130(I):
    O = diagonal_mirror(I)
    return O


def solve_3c9b0459(I):
    O = rot180(I)
    return O


def solve_6150a2bd(I):
    O = rot180(I)
    return O


def solve_9172f3a0(I):
    O = upscale(I, 3)
    return O


def solve_9dfd6313(I):
    O = diagonal_mirror(I)
    return O


def solve_a416b8f3(I):
    O = horizontal_concat(I, I)
    return O


def solve_b1948b0a(I):
    O = replace(I, COLOR_SIX, COLOR_TWO)
    return O


def solve_c59eb873(I):
    O = upscale(I, 2)
    return O


def solve_c8f0f002(I):
    O = replace(I, COLOR_SEVEN, COLOR_FIVE)
    return O


def solve_d10ecb37(I):
    O = crop(I, ORIGIN, TWO_BY_TWO)
    return O


def solve_d511f180(I):
    O = switch(I, COLOR_FIVE, COLOR_EIGHT)
    return O


def solve_ed36ccf7(I):
    O = rot270(I)
    return O


def solve_4c4377d9(I):
    x1 = horizontal_mirror(I)
    O = vertical_concat(x1, I)
    return O


def solve_6d0aefbc(I):
    x1 = vertical_mirror(I)
    O = horizontal_concat(I, x1)
    return O


def solve_6fa7a44f(I):
    x1 = horizontal_mirror(I)
    O = vertical_concat(I, x1)
    return O


def solve_5614dbcf(I):
    x1 = replace(I, COLOR_FIVE, COLOR_ZERO)
    O = downscale(x1, 3)
    return O


def solve_5bd6f4ac(I):
    x1 = to_horizontal_vec(6)
    O = crop(I, x1, THREE_BY_THREE)
    return O


def solve_5582e5ca(I):
    x1 = most_common_color(I)
    O = create_grid(x1, THREE_BY_THREE)
    return O


def solve_8be77c9e(I):
    x1 = horizontal_mirror(I)
    O = vertical_concat(I, x1)
    return O


def solve_c9e6f938(I):
    x1 = vertical_mirror(I)
    O = horizontal_concat(I, x1)
    return O


def solve_2dee498d(I):
    x1 = horizontal_split(I, 3)
    O = get_first(x1)
    return O


def solve_1cf80156(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_32597951(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = bounding_box_delta(x1)
    O = fill(I, COLOR_THREE, x2)
    return O


def solve_25ff71a9(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    O = move_object(I, x2, DOWN)
    return O


def solve_0b148d64(I):
    x1 = partition(I)
    x2 = argmin(x1, size)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_1f85a75f(I):
    x1 = as_objects(I, True, True, True)
    x2 = argmax(x1, size)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_23b5c85d(I):
    x1 = as_objects(I, True, True, True)
    x2 = argmin(x1, size)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_9ecd008a(I):
    x1 = vertical_mirror(I)
    x2 = of_color(I, COLOR_ZERO)
    O = smallest_subgrid_containing(x2, x1)
    return O


def solve_ac0a08a4(I):
    x1 = color_count(I, COLOR_ZERO)
    x2 = subtract(9, x1)
    O = upscale(I, x2)
    return O


def solve_be94b721(I):
    x1 = as_objects(I, True, False, True)
    x2 = argmax(x1, size)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_c909285e(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    O = smallest_subgrid_containing(x2, I)
    return O


def solve_f25ffba3(I):
    x1 = bottom_half(I)
    x2 = horizontal_mirror(x1)
    O = vertical_concat(x2, x1)
    return O


def solve_c1d99e64(I):
    x1 = solid_color_strips_in_grid(I)
    x2 = flatten(x1)
    O = fill(I, COLOR_TWO, x2)
    return O


def solve_b91ae062(I):
    x1 = count_colors(I)
    x2 = decrement(x1)
    O = upscale(I, x2)
    return O


def solve_3aa6fb7a(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform_and_flatten(corner_indices, x1)
    O = fill_background(I, COLOR_ONE, x2)
    return O


def solve_7b7f7511(I):
    x1 = is_portrait(I)
    x2 = condition_if_else(x1, top_half, left_half)
    O = x2(I)
    return O


def solve_4258a5f9(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = transform_and_flatten(neighbors, x1)
    O = fill(I, COLOR_ONE, x2)
    return O


def solve_2dc579da(I):
    x1 = vertical_split(I, 2)
    x2 = fix_last_argument(horizontal_split, 2)
    x3 = transform_and_flatten(x2, x1)
    O = argmax(x3, count_colors)
    return O


def solve_28bf18c6(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    O = horizontal_concat(x3, x3)
    return O


def solve_3af2c5a8(I):
    x1 = vertical_mirror(I)
    x2 = horizontal_concat(I, x1)
    x3 = horizontal_mirror(x2)
    O = vertical_concat(x2, x3)
    return O


def solve_44f52bb0(I):
    x1 = vertical_mirror(I)
    x2 = is_equal(x1, I)
    x3 = condition_if_else(x2, COLOR_ONE, COLOR_SEVEN)
    O = create_grid(x3, UNITY)
    return O


def solve_62c24649(I):
    x1 = vertical_mirror(I)
    x2 = horizontal_concat(I, x1)
    x3 = horizontal_mirror(x2)
    O = vertical_concat(x2, x3)
    return O


def solve_67e8384a(I):
    x1 = vertical_mirror(I)
    x2 = horizontal_concat(I, x1)
    x3 = horizontal_mirror(x2)
    O = vertical_concat(x2, x3)
    return O


def solve_7468f01a(I):
    x1 = as_objects(I, False, True, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    O = vertical_mirror(x3)
    return O


def solve_662c240a(I):
    x1 = vertical_split(I, 3)
    x2 = combine_two_function_results(is_equal, diagonal_mirror, identity)
    x3 = compose(logical_not, x2)
    O = extract_first_matching(x1, x3)
    return O


def solve_42a50994(I):
    x1 = as_objects(I, True, True, True)
    x2 = size_filter(x1, 1)
    x3 = flatten(x2)
    O = erase_patch(I, x3)
    return O


def solve_56ff96f3(I):
    x1 = partition_only_foreground(I)
    x2 = combine_two_function_results(recolor, get_color, bounding_box_indices)
    x3 = transform_and_flatten(x2, x1)
    O = paint_onto_grid(I, x3)
    return O


def solve_50cb2852(I):
    x1 = as_objects(I, True, False, True)
    x2 = compose(bounding_box_indices, inbox)
    x3 = transform_and_flatten(x2, x1)
    O = fill(I, COLOR_EIGHT, x3)
    return O


def solve_4347f46a(I):
    x1 = as_objects(I, True, False, True)
    x2 = combine_two_function_results(difference, to_indices, box)
    x3 = transform_and_flatten(x2, x1)
    O = fill(I, COLOR_ZERO, x3)
    return O


def solve_46f33fce(I):
    x1 = rot180(I)
    x2 = downscale(x1, 2)
    x3 = rot180(x2)
    O = upscale(x3, 4)
    return O


def solve_a740d043(I):
    x1 = as_objects(I, True, True, True)
    x2 = flatten(x1)
    x3 = smallest_subgrid_containing(x2, I)
    O = replace(x3, COLOR_ONE, COLOR_ZERO)
    return O


def solve_a79310a0(I):
    x1 = as_objects(I, True, False, True)
    x2 = get_first(x1)
    x3 = move_object(I, x2, DOWN)
    O = replace(x3, COLOR_EIGHT, COLOR_TWO)
    return O


def solve_aabf363d(I):
    x1 = least_common_color(I)
    x2 = replace(I, x1, COLOR_ZERO)
    x3 = least_common_color(x2)
    O = replace(x2, x3, x1)
    return O


def solve_ae4f1146(I):
    x1 = as_objects(I, False, False, True)
    x2 = fix_last_argument(color_count, COLOR_ONE)
    x3 = argmax(x1, x2)
    O = smallest_subgrid_containing(x3, I)
    return O


def solve_b27ca6d3(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 2)
    x3 = transform_and_flatten(outbox, x2)
    O = fill(I, COLOR_THREE, x3)
    return O


def solve_ce22a75a(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform(outbox, x1)
    x3 = transform_and_flatten(bounding_box_indices, x2)
    O = fill(I, COLOR_ONE, x3)
    return O


def solve_dc1df850(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_TWO)
    x3 = transform_and_flatten(outbox, x2)
    O = fill(I, COLOR_ONE, x3)
    return O


def solve_f25fbde4(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    O = upscale(x3, 2)
    return O


def solve_44d8ac46(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform(bounding_box_delta, x1)
    x3 = keep_if_condition_and_flatten(x2, is_square)
    O = fill(I, COLOR_TWO, x3)
    return O


def solve_1e0a9b12(I):
    x1 = rot270(I)
    x1r = replace(x1, COLOR_ZERO, COLOR_BELOW) # mdda new
    x2 = fix_last_argument(sort, identity)  # mdda : This relies on BLACK being < other colors - FIXED
    #x3 = transform(x2, x1)
    x3 = transform(x2, x1r)
    x3r = replace(x3, COLOR_BELOW, COLOR_ZERO) # mdda new
    #O = rot90(x3)
    O = rot90(x3r)
    return O


def solve_0d3d703e(I):
    x1 = switch(I, COLOR_THREE, COLOR_FOUR)
    x2 = switch(x1, COLOR_EIGHT, COLOR_NINE)
    x3 = switch(x2, COLOR_TWO, COLOR_SIX)
    O = switch(x3, COLOR_ONE, COLOR_FIVE)
    return O


def solve_3618c87e(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = flatten(x2)
    O = move_object(I, x3, TWO_BY_ZERO)
    return O


def solve_1c786137(I):
    x1 = as_objects(I, True, False, False)
    x2 = argmax(x1, get_height)
    x3 = smallest_subgrid_containing(x2, I)
    O = trim_border(x3)
    return O


def solve_8efcae92(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ONE)
    x3 = compose(size, bounding_box_delta)
    x4 = argmax(x2, x3)
    O = smallest_subgrid_containing(x4, I)
    return O


def solve_445eab21(I):
    x1 = as_objects(I, True, False, True)
    x2 = combine_two_function_results(multiply, get_height, get_width)
    x3 = argmax(x1, x2)
    x4 = get_color(x3)
    O = create_grid(x4, TWO_BY_TWO)
    return O


def solve_6f8cd79b(I):
    x1 = as_indices(I)
    x2 = transform(initset, x1)
    x3 = fix_last_argument(bordering, I)
    x4 = keep_if_condition_and_flatten(x2, x3)
    O = fill(I, COLOR_EIGHT, x4)
    return O


def solve_2013d3e2(I):
    x1 = as_objects(I, False, True, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = left_half(x3)
    O = top_half(x4)
    return O


def solve_41e4d17e(I):
    x1 = as_objects(I, True, False, True)
    x2 = combine_two_function_results(union, vertical_line, horizontal_line)
    x3 = compose(x2, center)
    x4 = transform_and_flatten(x3, x1)
    O = fill_background(I, COLOR_SIX, x4)
    return O


def solve_9565186b(I):
    x1 = get_shape(I)
    x2 = as_objects(I, True, False, False)
    x3 = argmax(x2, size)
    x4 = create_grid(COLOR_FIVE, x1)
    O = paint_onto_grid(x4, x3)
    return O


def solve_aedd82e4(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_TWO)
    x3 = size_filter(x2, 1)
    x4 = flatten(x3)
    O = fill(I, COLOR_ONE, x4)
    return O


def solve_bb43febb(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_FIVE)
    x3 = compose(bounding_box_indices, inbox)
    x4 = transform_and_flatten(x3, x2)
    O = fill(I, COLOR_TWO, x4)
    return O


def solve_e98196ab(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = as_objects(x1, True, False, True)
    x4 = flatten(x3)
    O = paint_onto_grid(x2, x4)
    return O


def solve_f76d97a5(I):
    x1 = palette(I)
    x2 = get_first(x1)
    x3 = get_last(x1)
    x4 = switch(I, x2, x3)
    O = replace(x4, COLOR_FIVE, COLOR_ZERO)
    return O


def solve_ce9e57f2(I):
    x1 = as_objects(I, True, False, True)
    x2 = combine_two_function_results(line_between, upper_left_corner, centerofmass)
    x3 = transform_and_flatten(x2, x1)
    x4 = fill(I, COLOR_EIGHT, x3)
    O = switch(x4, COLOR_EIGHT, COLOR_TWO)
    return O


def solve_22eb0ac0(I):
    x1 = partition_only_foreground(I)
    x2 = combine_two_function_results(recolor, get_color, bounding_box_indices)
    x3 = transform(x2, x1)
    x4 = keep_if_condition_and_flatten(x3, is_horizontal_line)
    O = paint_onto_grid(I, x4)
    return O


def solve_9f236235(I):
    x1 = remove_solid_color_strips_from_grid(I)
    x2 = as_objects(I, True, False, False)
    x3 = vertical_mirror(x1)
    x4 = valmin(x2, get_width)
    O = downscale(x3, x4)
    return O


def solve_a699fb00(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = shift_by_vector(x1, RIGHT)
    x3 = shift_by_vector(x1, LEFT)
    x4 = intersection(x2, x3)
    O = fill(I, COLOR_TWO, x4)
    return O


def solve_46442a0e(I):
    x1 = rot90(I)
    x2 = rot180(I)
    x3 = rot270(I)
    x4 = horizontal_concat(I, x1)
    x5 = horizontal_concat(x3, x2)
    O = vertical_concat(x4, x5)
    return O


def solve_7fe24cdd(I):
    x1 = rot90(I)
    x2 = rot180(I)
    x3 = rot270(I)
    x4 = horizontal_concat(I, x1)
    x5 = horizontal_concat(x3, x2)
    O = vertical_concat(x4, x5)
    return O


def solve_0ca9ddb6(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = of_color(I, COLOR_TWO)
    x3 = transform_and_flatten(direct_neighbors, x1)
    x4 = transform_and_flatten(diagonal_neighbors, x2)
    x5 = fill(I, COLOR_SEVEN, x3)
    O = fill(x5, COLOR_FOUR, x4)
    return O


def solve_543a7ed5(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_SIX)
    x3 = transform_and_flatten(outbox, x2)
    x4 = fill(I, COLOR_THREE, x3)
    x5 = transform_and_flatten(bounding_box_delta, x2)
    O = fill(x4, COLOR_FOUR, x5)
    return O


def solve_0520fde7(I):
    x1 = vertical_mirror(I)
    x2 = left_half(x1)
    x3 = right_half(x1)
    x4 = vertical_mirror(x3)
    x5 = cellwise(x2, x4, COLOR_ZERO)
    O = replace(x5, COLOR_ONE, COLOR_TWO)
    return O


def solve_dae9d2b5(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = of_color(x1, COLOR_FOUR)
    x4 = of_color(x2, COLOR_THREE)
    x5 = union(x3, x4)
    O = fill(x1, COLOR_SIX, x5)
    return O


def solve_8d5021e8(I):
    x1 = vertical_mirror(I)
    x2 = horizontal_concat(x1, I)
    x3 = horizontal_mirror(x2)
    x4 = vertical_concat(x2, x3)
    x5 = vertical_concat(x4, x2)
    O = horizontal_mirror(x5)
    return O


def solve_928ad970(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = smallest_subgrid_containing(x1, I)
    x3 = trim_border(x2)
    x4 = least_common_color(x3)
    x5 = inbox(x1)
    O = fill(I, x4, x5)
    return O


def solve_b60334d2(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = replace(I, COLOR_FIVE, COLOR_ZERO)
    x3 = transform_and_flatten(direct_neighbors, x1)
    x4 = transform_and_flatten(diagonal_neighbors, x1)
    x5 = fill(x2, COLOR_ONE, x3)
    O = fill(x5, COLOR_FIVE, x4)
    return O


def solve_b94a9452(I):
    x1 = as_objects(I, False, False, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = least_common_color(x3)
    x5 = most_common_color(x3)
    O = switch(x3, x4, x5)
    return O


def solve_d037b0a7(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_last_argument(shoot, DOWN)
    x3 = compose(x2, center)
    x4 = combine_two_function_results(recolor, get_color, x3)
    x5 = transform_and_flatten(x4, x1)
    O = paint_onto_grid(I, x5)
    return O


def solve_d0f5fe59(I):
    x1 = as_objects(I, True, False, True)
    x2 = size(x1)
    x3 = as_tuple(x2, x2)
    x4 = create_grid(COLOR_ZERO, x3)
    x5 = shoot(ORIGIN, UNITY)
    O = fill(x4, COLOR_EIGHT, x5)
    return O


def solve_e3497940(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = vertical_mirror(x2)
    x4 = as_objects(x3, True, False, True)
    x5 = flatten(x4)
    O = paint_onto_grid(x1, x5)
    return O


def solve_e9afcf9a(I):
    x1 = as_tuple(2, 1)
    x2 = crop(I, ORIGIN, x1)
    x3 = horizontal_mirror(x2)
    x4 = horizontal_concat(x2, x3)
    x5 = horizontal_concat(x4, x4)
    O = horizontal_concat(x5, x4)
    return O


def solve_48d8fb45(I):
    x1 = as_objects(I, True, True, True)
    x2 = equals(size, 1)
    x3 = extract_first_matching(x1, x2)
    x4 = fix_first_argument(adjacent, x3)
    x5 = extract_first_matching(x1, x4)
    O = smallest_subgrid_containing(x5, I)
    return O


def solve_d406998b(I):
    x1 = vertical_mirror(I)
    x2 = of_color(x1, COLOR_FIVE)
    x3 = compose(is_even, get_last)
    x4 = keep_if_condition(x2, x3)
    x5 = fill(x1, COLOR_THREE, x4)
    O = vertical_mirror(x5)
    return O


def solve_5117e062(I):
    x1 = as_objects(I, False, True, True)
    x2 = equals(count_colors, 2)
    x3 = extract_first_matching(x1, x2)
    x4 = smallest_subgrid_containing(x3, I)
    x5 = most_common_color(x3)
    O = replace(x4, COLOR_EIGHT, x5)
    return O


def solve_3906de3d(I):
    x1 = rot270(I)
    x2 = fix_last_argument(sort, identity)
    x3 = switch(x1, COLOR_ONE, COLOR_TWO)
    x4 = transform(x2, x3)
    x5 = switch(x4, COLOR_ONE, COLOR_TWO)
    O = counterdiagonal_mirror(x5)
    return O


def solve_00d62c1b(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = fix_last_argument(bordering, I)
    x4 = compose(logical_not, x3)
    x5 = keep_if_condition_and_flatten(x2, x4)
    O = fill(I, COLOR_FOUR, x5)
    return O


def solve_7b6016b9(I):
    x1 = as_objects(I, True, False, False)
    x2 = fix_last_argument(bordering, I)
    x3 = compose(logical_not, x2)
    x4 = keep_if_condition_and_flatten(x1, x3)
    x5 = fill(I, COLOR_TWO, x4)
    O = replace(x5, COLOR_ZERO, COLOR_THREE)
    return O


def solve_67385a82(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_THREE)
    x3 = size_filter(x2, 1)
    x4 = difference(x2, x3)
    x5 = flatten(x4)
    O = fill(I, COLOR_EIGHT, x5)
    return O


def solve_a5313dff(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = fix_last_argument(bordering, I)
    x4 = compose(logical_not, x3)
    x5 = keep_if_condition_and_flatten(x2, x4)
    O = fill(I, COLOR_ONE, x5)
    return O


def solve_ea32f347(I):
    x1 = as_objects(I, True, False, True)
    x2 = replace(I, COLOR_FIVE, COLOR_FOUR)
    x3 = argmin(x1, size)
    x4 = argmax(x1, size)
    x5 = fill(x2, COLOR_ONE, x4)
    O = fill(x5, COLOR_TWO, x3)
    return O


def solve_d631b094(I):
    x1 = palette(I)
    x2 = get_other(x1, COLOR_ZERO)
    x3 = of_color(I, x2)
    x4 = size(x3)
    x5 = as_tuple(1, x4)
    O = create_grid(x2, x5)
    return O


def solve_10fcaaa3(I):
    x1 = least_common_color(I)
    x2 = horizontal_concat(I, I)
    x3 = vertical_concat(x2, x2)
    x4 = of_color(x3, x1)
    x5 = transform_and_flatten(diagonal_neighbors, x4)
    O = fill_background(x3, COLOR_EIGHT, x5)
    return O


def solve_007bbfb7(I):
    x1 = horizontal_upscale(I, 3)
    x2 = vertical_upscale(x1, 3)
    x3 = horizontal_concat(I, I)
    x4 = horizontal_concat(x3, I)
    x5 = vertical_concat(x4, x4)
    x6 = vertical_concat(x5, x4)
    O = cellwise(x2, x6, COLOR_ZERO)
    return O


def solve_496994bd(I):
    x1 = get_width(I)
    x2 = get_height(I)
    x3 = halve(x2)
    x4 = as_tuple(x3, x1)
    x5 = crop(I, ORIGIN, x4)
    x6 = horizontal_mirror(x5)
    O = vertical_concat(x5, x6)
    return O


def solve_1f876c06(I):
    x1 = partition_only_foreground(I)
    x2 = compose(get_last, get_first)
    x3 = power(get_last, 2)
    x4 = combine_two_function_results(line_between, x2, x3)
    x5 = combine_two_function_results(recolor, get_color, x4)
    x6 = transform_and_flatten(x5, x1)
    O = paint_onto_grid(I, x6)
    return O


def solve_05f2a901(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_TWO)
    x3 = get_first(x2)
    x4 = color_filter(x1, COLOR_EIGHT)
    x5 = get_first(x4)
    x6 = move_until_touching(x3, x5)
    O = move_object(I, x3, x6)
    return O


def solve_39a8645d(I):
    x1 = as_objects(I, True, True, True)
    x2 = to_tuple(x1)
    x3 = transform(get_color, x2)
    x4 = most_common(x3)
    x5 = equals(get_color, x4)
    x6 = extract_first_matching(x1, x5)
    O = smallest_subgrid_containing(x6, I)
    return O


def solve_1b2d62fb(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = of_color(x1, COLOR_ZERO)
    x4 = of_color(x2, COLOR_ZERO)
    x5 = intersection(x3, x4)
    x6 = replace(x1, COLOR_NINE, COLOR_ZERO)
    O = fill(x6, COLOR_EIGHT, x5)
    return O


def solve_90c28cc7(I):
    x1 = as_objects(I, False, False, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = remove_duplicates(x3)
    x5 = rot90(x4)
    x6 = remove_duplicates(x5)
    O = rot270(x6)
    return O


def solve_b6afb2da(I):
    x1 = as_objects(I, True, False, False)
    x2 = replace(I, COLOR_FIVE, COLOR_TWO)
    x3 = color_filter(x1, COLOR_FIVE)
    x4 = transform_and_flatten(box, x3)
    x5 = fill(x2, COLOR_FOUR, x4)
    x6 = transform_and_flatten(corner_indices, x3)
    O = fill(x5, COLOR_ONE, x6)
    return O


def solve_b9b7f026(I):
    x1 = as_objects(I, True, False, False)
    x2 = argmin(x1, size)
    x3 = fix_last_argument(adjacent, x2)
    x4 = remove(x2, x1)
    x5 = extract_first_matching(x4, x3)
    x6 = get_color(x5)
    O = create_grid(x6, UNITY)
    return O


def solve_ba97ae07(I):
    x1 = as_objects(I, True, False, True)
    x2 = to_tuple(x1)
    x3 = transform(get_color, x2)
    x4 = most_common(x3)
    x5 = of_color(I, x4)
    x6 = bounding_box_indices(x5)
    O = fill(I, x4, x6)
    return O


def solve_c9f8e694(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = of_color(I, COLOR_ZERO)
    x4 = as_tuple(x1, 1)
    x5 = crop(I, ORIGIN, x4)
    x6 = horizontal_upscale(x5, x2)
    O = fill(x6, COLOR_ZERO, x3)
    return O


def solve_d23f8c26(I):
    x1 = as_indices(I)
    x2 = get_width(I)
    x3 = halve(x2)
    x4 = equals(get_last, x3)
    x5 = compose(logical_not, x4)
    x6 = keep_if_condition(x1, x5)
    O = fill(I, COLOR_ZERO, x6)
    return O


def solve_d5d6de2d(I):
    x1 = as_objects(I, True, False, True)
    x2 = keep_if_condition(x1, is_square)
    x3 = difference(x1, x2)
    x4 = compose(bounding_box_indices, inbox)
    x5 = transform_and_flatten(x4, x3)
    x6 = replace(I, COLOR_TWO, COLOR_ZERO)
    O = fill(x6, COLOR_THREE, x5)
    return O


def solve_dbc1a6ce(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = cartesian_product(x1, x1)
    x3 = combine_two_function_results(line_between, get_first, get_last)
    x4 = transform(x3, x2)
    x5 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x6 = keep_if_condition_and_flatten(x4, x5)
    O = fill_background(I, COLOR_EIGHT, x6)
    return O


def solve_ded97339(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = cartesian_product(x1, x1)
    x3 = combine_two_function_results(line_between, get_first, get_last)
    x4 = transform(x3, x2)
    x5 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x6 = keep_if_condition_and_flatten(x4, x5)
    O = fill_background(I, COLOR_EIGHT, x6)
    return O


def solve_ea786f4a(I):
    x1 = get_width(I)
    x2 = shoot(ORIGIN, UNITY)
    x3 = decrement(x1)
    x4 = to_horizontal_vec(x3)
    x5 = shoot(x4, DOWN_LEFT)
    x6 = union(x2, x5)
    O = fill(I, COLOR_ZERO, x6)
    return O


def solve_08ed6ac7(I):
    x1 = as_objects(I, True, False, True)
    x2 = to_tuple(x1)
    x3 = sort(x1, get_height)
    x4 = size(x2)
    # 
    #x5 = interval(x4, 0, -1)  # mdda : This seems to be over colors... NAUGHTY
    #x6 = transform_both_and_flatten(recolor, x5, x3)
    #
    # mdda : Figure out how to do a tuple of COLORs
    x5a = as_generic_tuple(COLOR_FOUR, COLOR_THREE)
    x5b = as_generic_tuple(COLOR_TWO, COLOR_ONE)
    x5c = union(x5a, x5b)
    x6 = transform_both_and_flatten(recolor, x5c, x3)
    #  as_generic_tuple
    #  combine
    #
    #  BAD IDEA!
    #
    #m4 = fix_last_argument(is_equal, 4)
    #m3 = fix_last_argument(is_equal, 3)
    #m2 = fix_last_argument(is_equal, 2)
    #m1 = fix_last_argument(is_equal, 1)
    #c4 = fix_first_argument(recolor, COLOR_FOUR)
    #c3 = fix_first_argument(recolor, COLOR_THREE)
    #c2 = fix_first_argument(recolor, COLOR_TWO)
    #c1 = fix_first_argument(recolor, COLOR_ONE)
    #f4 = condition_if_else(m4, c4, identity)
    #f3 = condition_if_else(m3, c3, identity)
    #f2 = condition_if_else(m2, c2, identity)
    #f1 = condition_if_else(m1, c1, identity)
    ##ch1 = chain(f2, f3, f4)    
    ##ch2 = compose(f1, ch1)    
    #r4 = transform_both(f4, x5, x3)
    #r3 = transform_both(f3, x5, r4)
    #r2 = transform_both(f2, x5, r3)
    #r1 = transform_both(f1, x5, r2)
    #x6 = flatten(r1)
    #
    O = paint_onto_grid(I, x6)
    return O


def solve_40853293(I):
    x1 = partition(I)
    x2 = combine_two_function_results(recolor, get_color, bounding_box_indices)
    x3 = transform(x2, x1)
    x4 = keep_if_condition_and_flatten(x3, is_horizontal_line)
    x5 = keep_if_condition_and_flatten(x3, is_vertical_line)
    x6 = paint_onto_grid(I, x4)
    O = paint_onto_grid(x6, x5)
    return O


def solve_5521c0d9(I):
    x1 = as_objects(I, True, False, True)
    x2 = flatten(x1)
    x3 = erase_patch(I, x2)
    x4 = chain(to_vertical_vec, negate, get_height)
    x5 = combine_two_function_results(shift_by_vector, identity, x4)
    x6 = transform_and_flatten(x5, x1)
    O = paint_onto_grid(x3, x6)
    return O


def solve_f8ff0b80(I):
    x1 = as_objects(I, True, True, True)
    x2 = sort(x1, size)
    x3 = transform(get_color, x2)
    x4 = fix_last_argument(create_grid, UNITY)
    x5 = transform(x4, x3)
    x6 = flatten(x5)
    O = horizontal_mirror(x6)
    return O


def solve_85c4e7cd(I):
    x1 = as_objects(I, True, False, False)
    x2 = compose(negate, size)
    x3 = sort(x1, size)
    x4 = sort(x1, x2)
    x5 = transform(get_color, x4)
    x6 = transform_both_and_flatten(recolor, x5, x3)
    O = paint_onto_grid(I, x6)
    return O


def solve_d2abd087(I):
    x1 = as_objects(I, True, False, True)
    x2 = equals(size, 6)
    x3 = compose(logical_not, x2)
    x4 = keep_if_condition_and_flatten(x1, x2)
    x5 = keep_if_condition_and_flatten(x1, x3)
    x6 = fill(I, COLOR_TWO, x4)
    O = fill(x6, COLOR_ONE, x5)
    return O


def solve_017c7c7b(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = is_equal(x1, x2)
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x5 = condition_if_else(x3, x2, x4)
    x6 = vertical_concat(I, x5)
    O = replace(x6, COLOR_ONE, COLOR_TWO)
    return O


def solve_363442ee(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = crop(I, ORIGIN, THREE_BY_THREE)
    x3 = as_object(x2)
    x4 = fix_first_argument(shift_by_vector, x3)
    x5 = compose(x4, decrement)
    x6 = transform_and_flatten(x5, x1)
    O = paint_onto_grid(I, x6)
    return O


def solve_5168d44c(I):
    x1 = of_color(I, COLOR_THREE)
    x2 = get_height(x1)
    x3 = is_equal(x2, 1)
    x4 = condition_if_else(x3, ZERO_BY_TWO, TWO_BY_ZERO)
    x5 = of_color(I, COLOR_TWO)
    x6 = recolor(COLOR_TWO, x5)
    O = move_object(I, x6, x4)
    return O


def solve_e9614598(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = combine_two_function_results(add, get_first, get_last)
    x3 = x2(x1)
    x4 = halve(x3)
    x5 = direct_neighbors(x4)
    x6 = insert(x4, x5)
    O = fill(I, COLOR_THREE, x6)
    return O


def solve_d9fac9be(I):
    x1 = palette(I)
    x2 = as_objects(I, True, False, True)
    x3 = argmax(x2, size)
    x4 = get_color(x3)
    x5 = remove(COLOR_ZERO, x1)
    x6 = get_other(x5, x4)
    O = create_grid(x6, UNITY)
    return O


def solve_e50d258f(I):
    x1 = get_width(I)
    x2 = as_tuple(9, x1)
    x3 = create_grid(COLOR_ZERO, x2)
    x4 = vertical_concat(I, x3)
    x5 = as_objects(x4, False, False, True)
    x6 = fix_last_argument(color_count, COLOR_TWO)
    x7 = argmax(x5, x6)
    O = smallest_subgrid_containing(x7, I)
    return O


def solve_810b9b61(I):
    x1 = as_objects(I, True, True, True)
    x2 = transform(to_indices, x1)
    x3 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x4 = keep_if_condition(x2, x3)
    x5 = difference(x2, x4)
    x6 = combine_two_function_results(is_equal, identity, box)
    x7 = keep_if_condition_and_flatten(x5, x6)
    O = fill(I, COLOR_THREE, x7)
    return O


def solve_54d82841(I):
    x1 = get_height(I)
    x2 = as_objects(I, True, False, True)
    x3 = compose(get_last, center)
    x4 = transform(x3, x2)
    x5 = decrement(x1)
    x6 = fix_first_argument(as_tuple, x5)
    x7 = transform(x6, x4)
    O = fill(I, COLOR_FOUR, x7)
    return O


def solve_60b61512(I):
    x1 = as_objects(I, True, True, True)
    x2 = transform_and_flatten(bounding_box_delta, x1)
    O = fill(I, COLOR_SEVEN, x2)
    return O


def solve_25d8a9c8(I):
    x1 = as_indices(I)
    x2 = as_objects(I, True, False, False)
    x3 = size_filter(x2, 3)
    x4 = keep_if_condition_and_flatten(x3, is_horizontal_line)
    x5 = to_indices(x4)
    x6 = difference(x1, x5)
    x7 = fill(I, COLOR_FIVE, x5)
    O = fill(x7, COLOR_ZERO, x6)
    return O


def solve_239be575(I):
    x1 = as_objects(I, False, True, True)
    x2 = fix_first_argument(contains, COLOR_TWO)
    x3 = compose(x2, palette)
    x4 = keep_if_condition(x1, x3)
    x5 = size(x4)
    x6 = greater_than(x5, 1)
    x7 = condition_if_else(x6, COLOR_ZERO, COLOR_EIGHT)
    O = create_grid(x7, UNITY)
    return O


def solve_67a423a3(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = color_filter(x2, x1)
    x4 = flatten(x3)
    x5 = bounding_box_delta(x4)
    x6 = get_first(x5)
    x7 = neighbors(x6)
    O = fill(I, COLOR_FOUR, x7)
    return O


def solve_5c0a986e(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_ONE)
    x3 = lower_right_corner(x1)
    x4 = upper_left_corner(x2)
    x5 = shoot(x3, UNITY)
    x6 = shoot(x4, NEG_UNITY)
    x7 = fill(I, COLOR_TWO, x5)
    O = fill(x7, COLOR_ONE, x6)
    return O


def solve_6430c8c4(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = as_tuple(4, 4)
    x4 = of_color(x1, COLOR_ZERO)
    x5 = of_color(x2, COLOR_ZERO)
    x6 = intersection(x4, x5)
    x7 = create_grid(COLOR_ZERO, x3)
    O = fill(x7, COLOR_THREE, x6)
    return O


def solve_94f9d214(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = of_color(x1, COLOR_ZERO)
    x4 = of_color(x2, COLOR_ZERO)
    x5 = as_tuple(4, 4)
    x6 = create_grid(COLOR_ZERO, x5)
    x7 = intersection(x3, x4)
    O = fill(x6, COLOR_TWO, x7)
    return O


def solve_a1570a43(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_THREE)
    x3 = recolor(COLOR_TWO, x1)
    x4 = upper_left_corner(x2)
    x5 = upper_left_corner(x1)
    x6 = subtract(x4, x5)
    x7 = increment(x6)
    O = move_object(I, x3, x7)
    return O


def solve_ce4f8723(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = of_color(x1, COLOR_ZERO)
    x4 = of_color(x2, COLOR_ZERO)
    x5 = intersection(x3, x4)
    x6 = as_tuple(4, 4)
    x7 = create_grid(COLOR_THREE, x6)
    O = fill(x7, COLOR_ZERO, x5)
    return O


def solve_d13f3404(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_last_argument(shoot, UNITY)
    x3 = compose(x2, center)
    x4 = combine_two_function_results(recolor, get_color, x3)
    x5 = transform_and_flatten(x4, x1)
    x6 = as_tuple(6, 6)
    x7 = create_grid(COLOR_ZERO, x6)
    O = paint_onto_grid(x7, x5)
    return O


def solve_dc433765(I):
    x1 = of_color(I, COLOR_THREE)
    x2 = of_color(I, COLOR_FOUR)
    x3 = get_first(x1)
    x4 = get_first(x2)
    x5 = subtract(x4, x3)
    x6 = sign(x5)
    x7 = recolor(COLOR_THREE, x1)
    O = move_object(I, x7, x6)
    return O


def solve_f2829549(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = of_color(x1, COLOR_ZERO)
    x4 = of_color(x2, COLOR_ZERO)
    x5 = intersection(x3, x4)
    x6 = get_shape(x1)
    x7 = create_grid(COLOR_ZERO, x6)
    O = fill(x7, COLOR_THREE, x5)
    return O


def solve_fafffa47(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = get_shape(x2)
    x4 = of_color(x1, COLOR_ZERO)
    x5 = of_color(x2, COLOR_ZERO)
    x6 = intersection(x4, x5)
    x7 = create_grid(COLOR_ZERO, x3)
    O = fill(x7, COLOR_TWO, x6)
    return O


def solve_fcb5c309(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = color_filter(x2, x1)
    x4 = difference(x2, x3)
    x5 = argmax(x4, size)
    x6 = get_color(x5)
    x7 = smallest_subgrid_containing(x5, I)
    O = replace(x7, x6, x1)
    return O


def solve_ff805c23(I):
    x1 = horizontal_mirror(I)
    x2 = vertical_mirror(I)
    x3 = of_color(I, COLOR_ONE)
    x4 = smallest_subgrid_containing(x3, x1)
    x5 = smallest_subgrid_containing(x3, x2)
    x6 = palette(x4)
    x7 = contains(COLOR_ONE, x6)
    O = condition_if_else(x7, x5, x4)
    return O


def solve_e76a88a6(I):
    x1 = as_objects(I, False, False, True)
    x2 = argmax(x1, count_colors)
    x3 = shift_to_origin(x2)
    x4 = remove(x2, x1)
    x5 = transform(upper_left_corner, x4)
    x6 = fix_first_argument(shift_by_vector, x3)
    x7 = transform_and_flatten(x6, x5)
    O = paint_onto_grid(I, x7)
    return O


def solve_7c008303(I):
    x1 = of_color(I, COLOR_THREE)
    x2 = smallest_subgrid_containing(x1, I)
    x3 = of_color(x2, COLOR_ZERO)
    x4 = replace(I, COLOR_THREE, COLOR_ZERO)
    x5 = replace(x4, COLOR_EIGHT, COLOR_ZERO)
    x6 = remove_solid_color_strips_from_grid(x5)
    x7 = upscale(x6, 3)
    O = fill(x7, COLOR_ZERO, x3)
    return O


def solve_7f4411dc(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = fix_last_argument(difference, x2)
    x4 = fix_last_argument(greater_than, 2)
    x5 = chain(x4, size, x3)
    x6 = compose(x5, direct_neighbors)
    x7 = keep_if_condition(x2, x6)
    O = fill(I, COLOR_ZERO, x7)
    return O


def solve_b230c067(I):
    x1 = as_objects(I, True, True, True)
    x2 = to_tuple(x1)
    x3 = transform(shift_to_origin, x2)
    x4 = least_common(x3)
    x5 = equals(shift_to_origin, x4)
    x6 = extract_first_matching(x1, x5)
    x7 = replace(I, COLOR_EIGHT, COLOR_ONE)
    O = fill(x7, COLOR_TWO, x6)
    return O


def solve_e8593010(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = size_filter(x1, 2)
    x4 = flatten(x2)
    x5 = fill(I, COLOR_THREE, x4)
    x6 = flatten(x3)
    x7 = fill(x5, COLOR_TWO, x6)
    O = replace(x7, COLOR_ZERO, COLOR_ONE)
    return O


def solve_6d75e8bb(I):
    x1 = as_objects(I, True, False, True)
    x2 = get_first(x1)
    x3 = upper_left_corner(x2)
    x4 = smallest_subgrid_containing(x2, I)
    x5 = replace(x4, COLOR_ZERO, COLOR_TWO)
    x6 = as_object(x5)
    x7 = shift_by_vector(x6, x3)
    O = paint_onto_grid(I, x7)
    return O


def solve_3f7978a0(I):
    x1 = partition_only_foreground(I)
    x2 = equals(get_color, COLOR_FIVE)
    x3 = extract_first_matching(x1, x2)
    x4 = upper_left_corner(x3)
    x5 = subtract(x4, DOWN)
    x6 = get_shape(x3)
    x7 = add(x6, TWO_BY_ZERO)
    O = crop(I, x5, x7)
    return O


def solve_1190e5a7(I):
    x1 = most_common_color(I)
    x2 = solid_color_strips_in_grid(I)
    x3 = keep_if_condition(x2, is_vertical_line)
    x4 = difference(x2, x3)
    x5 = as_generic_tuple(x4, x3)  
    x6 = transform(size, x5)
    x7 = increment(x6)
    O = create_grid(x1, x7)
    return O


def solve_6e02f1e3(I):
    x1 = count_colors(I)
    x2 = create_grid(COLOR_ZERO, THREE_BY_THREE)
    x3 = is_equal(x1, 3)
    x4 = is_equal(x1, 2)
    x5 = condition_if_else(x3, TWO_BY_ZERO, ORIGIN)
    x6 = condition_if_else(x4, TWO_BY_TWO, ZERO_BY_TWO)
    x7 = line_between(x5, x6)
    O = fill(x2, COLOR_FIVE, x7)
    return O


def solve_a61f2674(I):
    x1 = as_objects(I, True, False, True)
    x2 = argmax(x1, size)
    x3 = argmin(x1, size)
    x4 = replace(I, COLOR_FIVE, COLOR_ZERO)
    x5 = recolor(COLOR_ONE, x2)
    x6 = recolor(COLOR_TWO, x3)
    x7 = union(x5, x6)
    O = paint_onto_grid(x4, x7)
    return O


def solve_fcc82909(I):
    x1 = as_objects(I, False, True, True)
    x2 = fix_last_argument(add, DOWN)
    x3 = compose(x2, lower_left_corner)
    x4 = compose(to_vertical_vec, count_colors)
    x5 = combine_two_function_results(add, lower_right_corner, x4)
    x6 = combine_two_function_results(as_tuple, x3, x5)
    x7 = compose(box, x6)
    x8 = transform_and_flatten(x7, x1)
    O = fill(I, COLOR_THREE, x8)
    return O


def solve_72ca375d(I):
    x1 = as_objects(I, True, True, True)
    x2 = to_tuple(x1)
    x3 = fix_last_argument(smallest_subgrid_containing, I)
    x4 = transform(x3, x2)
    x5 = transform(vertical_mirror, x4)
    x6 = transform_both(is_equal, x4, x5)
    x7 = pairwise(x4, x6)
    x8 = extract_first_matching(x7, get_last)
    O = get_first(x8)
    return O


def solve_253bf280(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = apply_function_on_cartesian_product(line_between, x1, x1)
    x3 = fix_last_argument(greater_than, 1)
    x4 = compose(x3, size)
    x5 = keep_if_condition(x2, x4)
    x6 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x7 = keep_if_condition_and_flatten(x5, x6)
    x8 = fill(I, COLOR_THREE, x7)
    O = fill(x8, COLOR_EIGHT, x1)
    return O


def solve_694f12f3(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_FOUR)
    x3 = compose(bounding_box_indices, inbox)
    x4 = argmin(x2, size)
    x5 = argmax(x2, size)
    x6 = x3(x4)
    x7 = x3(x5)
    x8 = fill(I, COLOR_ONE, x6)
    O = fill(x8, COLOR_TWO, x7)
    return O


def solve_1f642eb9(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = difference(x1, x2)
    x4 = get_first(x3)
    x5 = fix_last_argument(move_until_touching, x4)
    x6 = compose(crement, x5)
    x7 = combine_two_function_results(shift_by_vector, identity, x6)
    x8 = transform_and_flatten(x7, x2)
    O = paint_onto_grid(I, x8)
    return O


def solve_31aa019c(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = get_first(x2)
    x4 = neighbors(x3)
    x5 = as_tuple(10, 10)
    x6 = create_grid(COLOR_ZERO, x5)
    x7 = initset(x3)
    x8 = fill(x6, x1, x7)
    O = fill(x8, COLOR_TWO, x4)
    return O


def solve_27a28665(I):
    x1 = as_objects(I, True, False, False)
    x2 = valmax(x1, size)
    x3 = is_equal(x2, 1)
    x4 = is_equal(x2, 4)
    x5 = is_equal(x2, 5)
    x6 = condition_if_else(x3, COLOR_TWO, COLOR_ONE)
    x7 = condition_if_else(x4, COLOR_THREE, x6)
    x8 = condition_if_else(x5, COLOR_SIX, x7)
    O = create_grid(x8, UNITY)
    return O


def solve_7ddcd7ec(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = difference(x1, x2)
    x4 = get_first(x3)
    x5 = get_color(x4)
    x6 = fix_first_argument(position, x4)
    x7 = combine_two_function_results(shoot, center, x6)
    x8 = transform_and_flatten(x7, x2)
    O = fill(I, x5, x8)
    return O


def solve_3bd67248(I):
    x1 = get_height(I)
    x2 = decrement(x1)
    x3 = decrement(x2)
    x4 = as_tuple(x3, 1)
    x5 = as_tuple(x2, 1)
    x6 = shoot(x4, UP_RIGHT)
    x7 = shoot(x5, RIGHT)
    x8 = fill(I, COLOR_TWO, x6)
    O = fill(x8, COLOR_FOUR, x7)
    return O


def solve_73251a56(I):
    Ipost = replace(I, COLOR_ZERO, COLOR_BELOW)  # mdda added
    x1 = diagonal_mirror(Ipost)
    x2 = transform_both(pairwise, Ipost, x1)
    x3 = fix_first_argument(transform, maximum)  # mdda : Assumes that BLACK < other colors - FIXED
    x4 = transform(x3, x2)
    x5 = most_common_color(x4)
    #x6 = replace(x4, COLOR_ZERO, x5)
    x6 = replace(x4, COLOR_BELOW, x5)   # mdda added
    x7 = color_at_location(x6, ORIGIN)
    x8 = shoot(ORIGIN, UNITY)
    O = fill(x6, x7, x8)
    return O


def solve_25d487eb(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = of_color(I, x1)
    x4 = center(x3)
    x5 = flatten(x2)
    x6 = center(x5)
    x7 = subtract(x6, x4)
    x8 = shoot(x4, x7)
    O = fill_background(I, x1, x8)
    return O


def solve_8f2ea7aa(I):
    x1 = as_objects(I, True, False, True)
    x2 = flatten(x1)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = upscale(x3, 3)
    x5 = horizontal_concat(x3, x3)
    x6 = horizontal_concat(x5, x3)
    x7 = vertical_concat(x6, x6)
    x8 = vertical_concat(x7, x6)
    O = cellwise(x4, x8, COLOR_ZERO)
    return O


def solve_b8825c91(I):
    #x1 = replace(I, COLOR_FOUR, COLOR_ZERO)  # mdda : Assumes that COLOR_BLACK < all other colors - FIXED
    x1 = replace(I, COLOR_FOUR, COLOR_BELOW)  # mdda fixed
    x2 = diagonal_mirror(x1)
    x3 = transform_both(pairwise, x1, x2)
    x4 = fix_first_argument(transform, maximum)  
    x5 = transform(x4, x3)
    x6 = counterdiagonal_mirror(x5)
    x7 = transform_both(pairwise, x5, x6)
    x8 = transform(x4, x7)
    O = counterdiagonal_mirror(x8)
    return O


def solve_cce03e0d(I):
    x1 = upscale(I, 3)
    x2 = horizontal_concat(I, I)
    x3 = horizontal_concat(x2, I)
    x4 = vertical_concat(x3, x3)
    x5 = vertical_concat(x4, x3)
    x6 = of_color(x1, COLOR_ZERO)
    x7 = of_color(x1, COLOR_ONE)
    x8 = union(x6, x7)
    O = fill(x5, COLOR_ZERO, x8)
    return O


def solve_d364b489(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = shift_by_vector(x1, DOWN)
    x3 = fill(I, COLOR_EIGHT, x2)
    x4 = shift_by_vector(x1, UP)
    x5 = fill(x3, COLOR_TWO, x4)
    x6 = shift_by_vector(x1, RIGHT)
    x7 = fill(x5, COLOR_SIX, x6)
    x8 = shift_by_vector(x1, LEFT)
    O = fill(x7, COLOR_SEVEN, x8)
    return O


def solve_a5f85a15(I):
    x1 = as_objects(I, True, True, True)
    x2 = interval(1, 9, 1)
    x3 = transform(double, x2)
    x4 = transform(decrement, x3)
    x5 = transform_both(as_tuple, x4, x4)
    x6 = transform(upper_left_corner, x1)
    x7 = fix_first_argument(shift_by_vector, x5)
    x8 = transform_and_flatten(x7, x6)
    O = fill(I, COLOR_FOUR, x8)
    return O


def solve_3ac3eb23(I):
    x1 = as_objects(I, True, False, True)
    x2 = chain(diagonal_neighbors, get_last, get_first)
    x3 = combine_two_function_results(recolor, get_color, x2)
    x4 = transform_and_flatten(x3, x1)
    x5 = paint_onto_grid(I, x4)
    x6 = vertical_split(x5, 3)
    x7 = get_first(x6)
    x8 = vertical_concat(x7, x7)
    O = vertical_concat(x7, x8)
    return O


def solve_444801d8(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_ONE)
    x3 = fix_last_argument(to_object, I)
    x4 = chain(least_common_color, x3, bounding_box_delta)
    x5 = fix_last_argument(shift_by_vector, UP)
    x6 = compose(x5, bounding_box_indices)
    x7 = combine_two_function_results(recolor, x4, x6)
    x8 = transform_and_flatten(x7, x2)
    O = paint_onto_grid_background(I, x8)
    return O


def solve_22168020(I):
    x1 = palette(I)
    x2 = remove(COLOR_ZERO, x1)
    x3 = fix_first_argument(of_color, I)
    x4 = fix_first_argument(apply_function_on_cartesian_product, line_between)
    x5 = combine_two_function_results(x4, x3, x3)
    x6 = compose(flatten, x5)
    x7 = combine_two_function_results(recolor, identity, x6)
    x8 = transform_and_flatten(x7, x2)
    O = paint_onto_grid(I, x8)
    return O


def solve_6e82a1ae(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_first_argument(size_filter, x1)
    x3 = compose(flatten, x2)
    x4 = x3(2)
    x5 = x3(3)
    x6 = x3(4)
    x7 = fill(I, COLOR_THREE, x4)
    x8 = fill(x7, COLOR_TWO, x5)
    O = fill(x8, COLOR_ONE, x6)
    return O


def solve_b2862040(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_NINE)
    x3 = color_filter(x1, COLOR_ONE)
    x4 = fix_last_argument(bordering, I)
    x5 = compose(logical_not, x4)
    x6 = keep_if_condition_and_flatten(x2, x5)
    x7 = fix_last_argument(adjacent, x6)
    x8 = keep_if_condition_and_flatten(x3, x7)
    O = fill(I, COLOR_EIGHT, x8)
    return O


def solve_868de0fa(I):
    x1 = as_objects(I, True, False, False)
    x2 = keep_if_condition(x1, is_square)
    x3 = compose(is_even, get_height)
    x4 = keep_if_condition(x2, x3)
    x5 = difference(x2, x4)
    x6 = flatten(x4)
    x7 = flatten(x5)
    x8 = fill(I, COLOR_TWO, x6)
    O = fill(x8, COLOR_SEVEN, x7)
    return O


def solve_681b3aeb(I):
    x1 = rot270(I)
    x2 = as_objects(x1, True, False, True)
    x3 = argmax(x2, size)
    x4 = argmin(x2, size)
    x5 = get_color(x4)
    x6 = create_grid(x5, THREE_BY_THREE)
    x7 = shift_to_origin(x3)
    x8 = paint_onto_grid(x6, x7)
    O = rot90(x8)
    return O


def solve_8e5a5113(I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = rot90(x1)
    x3 = rot180(x1)
    x4 = as_generic_tuple(x2, x3)
    x5 = as_tuple(4, 8)
    x6 = transform(to_horizontal_vec, x5)
    x7 = transform(as_object, x4)
    x8 = transform_both_and_flatten(shift_by_vector, x7, x6)
    O = paint_onto_grid(I, x8)
    return O


def solve_025d127b(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform(get_color, x1)
    x3 = flatten(x1)
    x4 = fix_first_argument(color_filter, x1)
    x5 = fix_last_argument(argmax, rightmost)
    x6 = compose(x5, x4)
    x7 = transform_and_flatten(x6, x2)
    x8 = difference(x3, x7)
    O = move_object(I, x8, RIGHT)
    return O


def solve_2281f1f4(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = cartesian_product(x1, x1)
    x3 = power(get_first, 2)
    x4 = power(get_last, 2)
    x5 = combine_two_function_results(as_tuple, x3, x4)
    x6 = transform(x5, x2)
    x7 = upper_right_corner(x1)
    x8 = remove(x7, x6)
    O = fill_background(I, COLOR_TWO, x8)
    return O


def solve_cf98881b(I):
    x1 = horizontal_split(I, 3)
    x2 = get_first(x1)
    x3 = remove(x2, x1)
    x4 = get_first(x3)
    x5 = get_last(x3)
    x6 = of_color(x4, COLOR_NINE)
    x7 = of_color(x2, COLOR_FOUR)
    x8 = fill(x5, COLOR_NINE, x6)
    O = fill(x8, COLOR_FOUR, x7)
    return O


def solve_d4f3cd78(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = bounding_box_delta(x1)
    x3 = fill(I, COLOR_EIGHT, x2)
    x4 = box(x1)
    x5 = difference(x4, x1)
    x6 = position(x4, x5)
    x7 = get_first(x5)
    x8 = shoot(x7, x6)
    O = fill(x3, COLOR_EIGHT, x8)
    return O


def solve_bda2d7a6(I):
    x1 = partition(I)
    x2 = sort(x1, size)
    x3 = transform(get_color, x2)
    x4 = get_last(x2)
    x5 = remove(x4, x2)
    x6 = repeat(x4, 1)
    x7 = union(x6, x5)
    x8 = transform_both_and_flatten(recolor, x3, x7)
    O = paint_onto_grid(I, x8)
    return O


def solve_137eaa0f(I):
    x1 = as_objects(I, False, True, True)
    x2 = equals(get_first, COLOR_FIVE)
    x3 = fix_last_argument(keep_if_condition, x2)
    x4 = chain(negate, center, x3)
    x5 = combine_two_function_results(shift_by_vector, identity, x4)
    x6 = create_grid(COLOR_ZERO, THREE_BY_THREE)
    x7 = transform_and_flatten(x5, x1)
    x8 = shift_by_vector(x7, UNITY)
    O = paint_onto_grid(x6, x8)
    return O


def solve_6455b5f5(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = argmax(x1, size)
    x4 = valmin(x1, size)
    x5 = size_filter(x2, x4)
    x6 = recolor(COLOR_ONE, x3)
    x7 = flatten(x5)
    x8 = paint_onto_grid(I, x6)
    O = fill(x8, COLOR_EIGHT, x7)
    return O


def solve_b8cdaf2b(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = shift_by_vector(x2, UP)
    x4 = upper_left_corner(x3)
    x5 = upper_right_corner(x3)
    x6 = shoot(x4, NEG_UNITY)
    x7 = shoot(x5, UP_RIGHT)
    x8 = union(x6, x7)
    O = fill_background(I, x1, x8)
    return O


def solve_bd4472b8(I):
    x1 = get_width(I)
    x2 = as_tuple(2, x1)
    x3 = crop(I, ORIGIN, x2)
    x4 = top_half(x3)
    x5 = diagonal_mirror(x4)
    x6 = horizontal_upscale(x5, x1)
    x7 = repeat(x6, 2)
    x8 = flatten(x7)
    O = vertical_concat(x3, x8)
    return O


def solve_4be741c5(I):
    x1 = is_portrait(I)
    x2 = condition_if_else(x1, diagonal_mirror, identity)
    x3 = condition_if_else(x1, get_height, get_width)
    x4 = x3(I)
    x5 = as_tuple(1, x4)
    x6 = x2(I)
    x7 = crop(x6, ORIGIN, x5)
    x8 = transform(remove_duplicates, x7)
    O = x2(x8)
    return O


def solve_bbc9ae5d(I):
    x1 = get_width(I)
    x2 = palette(I)
    x3 = halve(x1)
    x4 = vertical_upscale(I, x3)
    x5 = fix_last_argument(shoot, UNITY)
    x6 = get_other(x2, COLOR_ZERO)
    x7 = of_color(x4, x6)
    x8 = transform_and_flatten(x5, x7)
    O = fill(x4, x6, x8)
    return O


def solve_d90796e8(I):
    x1 = as_objects(I, False, False, True)
    x2 = size_filter(x1, 2)
    x3 = fix_first_argument(contains, COLOR_TWO)
    x4 = compose(x3, palette)
    x5 = keep_if_condition_and_flatten(x2, x4)
    x6 = erase_patch(I, x5)
    x7 = equals(get_first, COLOR_THREE)
    x8 = keep_if_condition(x5, x7)
    O = fill(x6, COLOR_EIGHT, x8)
    return O


def solve_2c608aff(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = argmax(x2, size)
    x4 = to_indices(x3)
    x5 = of_color(I, x1)
    x6 = apply_function_on_cartesian_product(line_between, x4, x5)
    x7 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x8 = keep_if_condition_and_flatten(x6, x7)
    O = fill_background(I, x1, x8)
    return O


def solve_f8b3ba0a(I):
    x1 = remove_solid_color_strips_from_grid(I)
    x2 = as_tuple(3, 1)
    x3 = palette(x1)
    x4 = fix_first_argument(color_count, x1)
    x5 = compose(negate, x4)
    x6 = sort(x3, x5)
    x7 = fix_last_argument(create_grid, UNITY)
    x8 = transform(x7, x6)
    x9 = flatten(x8)
    O = crop(x9, DOWN, x2)
    return O


def solve_80af3007(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = upscale(x3, 3)
    x5 = horizontal_concat(x3, x3)
    x6 = horizontal_concat(x5, x3)
    x7 = vertical_concat(x6, x6)
    x8 = vertical_concat(x7, x6)
    x9 = cellwise(x4, x8, COLOR_ZERO)
    O = downscale(x9, 3)
    return O


def solve_83302e8f(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = keep_if_condition(x2, is_square)
    x4 = difference(x2, x3)
    x5 = flatten(x3)
    x6 = recolor(COLOR_THREE, x5)
    x7 = flatten(x4)
    x8 = recolor(COLOR_FOUR, x7)
    x9 = paint_onto_grid(I, x6)
    O = paint_onto_grid(x9, x8)
    return O


def solve_1fad071e(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_ONE)
    x3 = size_filter(x2, 4)
    x4 = size(x3)
    x5 = subtract(5, x4)
    x6 = as_tuple(1, x4)
    x7 = create_grid(COLOR_ONE, x6)
    x8 = as_tuple(1, x5)
    x9 = create_grid(COLOR_ZERO, x8)
    O = horizontal_concat(x7, x9)
    return O


def solve_11852cab(I):
    x1 = as_objects(I, True, True, True)
    x2 = flatten(x1)
    x3 = horizontal_mirror(x2)
    x4 = vertical_mirror(x2)
    x5 = diagonal_mirror(x2)
    x6 = counterdiagonal_mirror(x2)
    x7 = paint_onto_grid(I, x3)
    x8 = paint_onto_grid(x7, x4)
    x9 = paint_onto_grid(x8, x5)
    O = paint_onto_grid(x9, x6)
    return O


def solve_3428a4f5(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = as_tuple(6, 5)
    x4 = of_color(x1, COLOR_TWO)
    x5 = of_color(x2, COLOR_TWO)
    x6 = union(x4, x5)
    x7 = intersection(x4, x5)
    x8 = difference(x6, x7)
    x9 = create_grid(COLOR_ZERO, x3)
    O = fill(x9, COLOR_THREE, x8)
    return O


def solve_178fcbfb(I):
    x1 = as_objects(I, True, False, True)
    x2 = of_color(I, COLOR_TWO)
    x3 = transform_and_flatten(vertical_line, x2)
    x4 = fill(I, COLOR_TWO, x3)
    x5 = color_filter(x1, COLOR_TWO)
    x6 = difference(x1, x5)
    x7 = compose(horizontal_line, center)
    x8 = combine_two_function_results(recolor, get_color, x7)
    x9 = transform_and_flatten(x8, x6)
    O = paint_onto_grid(x4, x9)
    return O


def solve_3de23699(I):
    x1 = partition_only_foreground(I)
    x2 = size_filter(x1, 4)
    x3 = get_first(x2)
    x4 = difference(x1, x2)
    x5 = get_first(x4)
    x6 = get_color(x3)
    x7 = get_color(x5)
    x8 = smallest_subgrid_containing(x3, I)
    x9 = trim_border(x8)
    O = replace(x9, x7, x6)
    return O


def solve_54d9e175(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = compose(neighbors, center)
    x4 = combine_two_function_results(recolor, get_color, x3)
    x5 = transform_and_flatten(x4, x2)
    x6 = paint_onto_grid(I, x5)
    x7 = replace(x6, COLOR_ONE, COLOR_SIX)
    x8 = replace(x7, COLOR_TWO, COLOR_SEVEN)
    x9 = replace(x8, COLOR_THREE, COLOR_EIGHT)
    O = replace(x9, COLOR_FOUR, COLOR_NINE)
    return O


def solve_5ad4f10b(I):
    x1 = as_objects(I, True, True, True)
    x2 = argmax(x1, size)
    x3 = get_color(x2)
    x4 = smallest_subgrid_containing(x2, I)
    x5 = least_common_color(x4)
    x6 = replace(x4, x5, COLOR_ZERO)
    x7 = replace(x6, x3, x5)
    x8 = get_height(x7)
    x9 = divide(x8, 3)
    O = downscale(x7, x9)
    return O


def solve_623ea044(I):
    x1 = as_objects(I, True, False, True)
    x2 = get_first(x1)
    x3 = center(x2)
    x4 = get_color(x2)
    #x5 = as_tuple(UNITY, NEG_UNITY)
    x5 = as_generic_tuple(UNITY, NEG_UNITY) # mdda
    #x6 = as_tuple(UP_RIGHT, DOWN_LEFT)
    x6 = as_generic_tuple(UP_RIGHT, DOWN_LEFT) # mdda
    x7 = union(x5, x6)
    x8 = fix_first_argument(shoot, x3)
    x9 = transform_and_flatten(x8, x7)
    O = fill(I, x4, x9)
    return O


def solve_6b9890af(I):
    x1 = as_objects(I, True, True, True)
    x2 = of_color(I, COLOR_TWO)
    x3 = argmin(x1, size)
    x4 = smallest_subgrid_containing(x2, I)
    x5 = get_width(x4)
    x6 = divide(x5, 3)
    x7 = upscale(x3, x6)
    x8 = shift_to_origin(x7)
    x9 = shift_by_vector(x8, UNITY)
    O = paint_onto_grid(x4, x9)
    return O


def solve_794b24be(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = size(x1)
    x3 = decrement(x2)
    x4 = create_grid(COLOR_ZERO, THREE_BY_THREE)
    x5 = to_horizontal_vec(x3)
    x6 = line_between(ORIGIN, x5)
    x7 = is_equal(x2, 4)
    x8 = insert(UNITY, x6)
    x9 = condition_if_else(x7, x8, x6)
    O = fill(x4, COLOR_TWO, x9)
    return O


def solve_88a10436(I):
    x1 = as_objects(I, False, False, True)
    x2 = color_filter(x1, COLOR_FIVE)
    x3 = get_first(x2)
    x4 = center(x3)
    x5 = difference(x1, x2)
    x6 = get_first(x5)
    x7 = shift_to_origin(x6)
    x8 = shift_by_vector(x7, x4)
    x9 = shift_by_vector(x8, NEG_UNITY)
    O = paint_onto_grid(I, x9)
    return O


def solve_88a62173(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = top_half(x1)
    x4 = top_half(x2)
    x5 = bottom_half(x1)
    x6 = bottom_half(x2)
    #x7 = as_tuple(x3, x4)
    x7 = as_generic_tuple(x3, x4) # mdda
    #x8 = as_tuple(x5, x6)
    x8 = as_generic_tuple(x5, x6) # mdda
    x9 = union(x7, x8)
    O = least_common(x9)
    return O


def solve_890034e9(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = inbox(x2)
    x4 = recolor(COLOR_ZERO, x3)
    x5 = occurrences(I, x4)
    x6 = shift_to_origin(x2)
    x7 = shift_by_vector(x6, NEG_UNITY)
    x8 = fix_first_argument(shift_by_vector, x7)
    x9 = transform_and_flatten(x8, x5)
    O = fill(I, x1, x9)
    return O


def solve_99b1bc43(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = of_color(x1, COLOR_ZERO)
    x4 = of_color(x2, COLOR_ZERO)
    x5 = union(x3, x4)
    x6 = intersection(x3, x4)
    x7 = difference(x5, x6)
    x8 = get_shape(x1)
    x9 = create_grid(COLOR_ZERO, x8)
    O = fill(x9, COLOR_THREE, x7)
    return O


def solve_a9f96cdd(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = replace(I, COLOR_TWO, COLOR_ZERO)
    x3 = shift_by_vector(x1, NEG_UNITY)
    x4 = fill(x2, COLOR_THREE, x3)
    x5 = shift_by_vector(x1, UP_RIGHT)
    x6 = fill(x4, COLOR_SIX, x5)
    x7 = shift_by_vector(x1, DOWN_LEFT)
    x8 = fill(x6, COLOR_EIGHT, x7)
    x9 = shift_by_vector(x1, UNITY)
    O = fill(x8, COLOR_SEVEN, x9)
    return O


def solve_af902bf9(I):
    x1 = of_color(I, COLOR_FOUR)
    x2 = apply_function_on_cartesian_product(line_between, x1, x1)
    x3 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x4 = keep_if_condition_and_flatten(x2, x3)
    x5 = fill_background(I, COLOR_BELOW, x4)
    x6 = as_objects(x5, False, False, True)
    x7 = compose(bounding_box_indices, inbox)
    x8 = transform_and_flatten(x7, x6)
    x9 = fill(x5, COLOR_TWO, x8)
    O = replace(x9, COLOR_BELOW, COLOR_ZERO)
    return O


def solve_b548a754(I):
    x1 = as_objects(I, True, False, True)
    x2 = replace(I, COLOR_EIGHT, COLOR_ZERO)
    x3 = least_common_color(x2)
    x4 = replace(x2, x3, COLOR_ZERO)
    x5 = least_common_color(x4)
    x6 = flatten(x1)
    x7 = bounding_box_indices(x6)
    x8 = box(x6)
    x9 = fill(I, x3, x7)
    O = fill(x9, x5, x8)
    return O


def solve_bdad9b1f(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = center(x1)
    x4 = center(x2)
    x5 = horizontal_line(x3)
    x6 = vertical_line(x4)
    x7 = intersection(x5, x6)
    x8 = fill(I, COLOR_TWO, x5)
    x9 = fill(x8, COLOR_EIGHT, x6)
    O = fill(x9, COLOR_FOUR, x7)
    return O


def solve_c3e719e8(I):
    x1 = most_common_color(I)
    x2 = horizontal_concat(I, I)
    x3 = upscale(I, 3)
    x4 = of_color(x3, x1)
    x5 = as_indices(x3)
    x6 = difference(x5, x4)
    x7 = horizontal_concat(x2, I)
    x8 = vertical_concat(x7, x7)
    x9 = vertical_concat(x8, x7)
    O = fill(x9, COLOR_ZERO, x6)
    return O


def solve_de1cd16c(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, False)
    x3 = size_filter(x2, 1)
    x4 = difference(x2, x3)
    x5 = fix_last_argument(smallest_subgrid_containing, I)
    x6 = transform(x5, x4)
    x7 = fix_last_argument(color_count, x1)
    x8 = argmax(x6, x7)
    x9 = most_common_color(x8)
    O = create_grid(x9, UNITY)
    return O


def solve_d8c310e9(I):
    x1 = as_objects(I, False, False, True)
    x2 = get_first(x1)
    x3 = horizontal_periodicity(x2)
    x4 = multiply(x3, 3)
    x5 = to_horizontal_vec(x3)
    x6 = to_horizontal_vec(x4)
    x7 = shift_by_vector(x2, x5)
    x8 = shift_by_vector(x2, x6)
    x9 = paint_onto_grid(I, x7)
    O = paint_onto_grid(x9, x8)
    return O


def solve_a3325580(I):
    x1 = as_objects(I, True, False, True)
    x2 = valmax(x1, size)
    x3 = size_filter(x1, x2)
    x4 = sort(x3, leftmost)
    x5 = transform(get_color, x4)
    x6 = as_tuple(1, x2)
    x7 = fix_last_argument(create_grid, x6)
    x8 = transform(x7, x5)
    x9 = flatten(x8)
    O = diagonal_mirror(x9)
    return O


def solve_8eb1be9a(I):
    x1 = as_objects(I, True, True, True)
    x2 = get_first(x1)
    x3 = interval(-2, 4, 1)
    x4 = fix_first_argument(shift_by_vector, x2)
    x5 = get_height(x2)
    x6 = fix_last_argument(multiply, x5)
    x7 = transform(x6, x3)
    x8 = transform(to_vertical_vec, x7)
    x9 = transform_and_flatten(x4, x8)
    O = paint_onto_grid(I, x9)
    return O


def solve_321b1fc6(I):
    x1 = as_objects(I, False, False, True)
    x2 = color_filter(x1, COLOR_EIGHT)
    x3 = difference(x1, x2)
    x4 = get_first(x3)
    x5 = erase_patch(I, x4)
    x6 = shift_to_origin(x4)
    x7 = fix_first_argument(shift_by_vector, x6)
    x8 = transform(upper_left_corner, x2)
    x9 = transform_and_flatten(x7, x8)
    O = paint_onto_grid(x5, x9)
    return O


def solve_1caeab9d(I):
    x1 = as_objects(I, True, True, True)
    x2 = of_color(I, COLOR_ONE)
    x3 = lowermost(x2)
    x4 = fix_first_argument(subtract, x3)
    x5 = chain(to_vertical_vec, x4, lowermost)
    x6 = combine_two_function_results(shift_by_vector, identity, x5)
    x7 = flatten(x1)
    x8 = erase_patch(I, x7)
    x9 = transform_and_flatten(x6, x1)
    O = paint_onto_grid(x8, x9)
    return O


def solve_77fdfe62(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = smallest_subgrid_containing(x1, I)
    x3 = replace(I, COLOR_EIGHT, COLOR_ZERO)
    x4 = replace(x3, COLOR_ONE, COLOR_ZERO)
    x5 = remove_solid_color_strips_from_grid(x4)
    x6 = get_width(x2)
    x7 = halve(x6)
    x8 = upscale(x5, x7)
    x9 = of_color(x2, COLOR_ZERO)
    O = fill(x8, COLOR_ZERO, x9)
    return O


def solve_c0f76784(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = keep_if_condition(x2, is_square)
    x4 = size_filter(x3, 1)
    x5 = flatten(x4)
    x6 = argmax(x3, size)
    x7 = flatten(x3)
    x8 = fill(I, COLOR_SEVEN, x7)
    x9 = fill(x8, COLOR_EIGHT, x6)
    O = fill(x9, COLOR_SIX, x5)
    return O


def solve_1b60fb0c(I):
    x1 = rot90(I)
    x2 = of_color(I, COLOR_ONE)
    x3 = of_color(x1, COLOR_ONE)
    x4 = neighbors(ORIGIN)
    x5 = transform_and_flatten(neighbors, x4)
    x6 = fix_first_argument(shift_by_vector, x3)
    x7 = transform(x6, x5)
    x8 = fix_first_argument(intersection, x2)
    x9 = compose(size, x8)
    x10 = argmax(x7, x9)
    O = fill_background(I, COLOR_TWO, x10)
    return O


def solve_ddf7fa4f(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = color_filter(x1, COLOR_FIVE)
    x4 = cartesian_product(x2, x3)
    x5 = combine_two_function_results(vertical_matching, get_first, get_last)
    x6 = keep_if_condition(x4, x5)
    x7 = compose(get_color, get_first)
    x8 = combine_two_function_results(recolor, x7, get_last)
    x9 = transform_and_flatten(x8, x6)
    O = paint_onto_grid(I, x9)
    return O


def solve_47c1f68c(I):
    x1 = least_common_color(I)
    x2 = vertical_mirror(I)
    x3 = as_objects(I, True, True, True)
    x4 = flatten(x3)
    x5 = most_common_color(x4)
    x6 = cellwise(I, x2, x1)
    x7 = horizontal_mirror(x6)
    x8 = cellwise(x6, x7, x1)
    x9 = remove_solid_color_strips_from_grid(x8)
    O = replace(x9, x1, x5)
    return O


def solve_6c434453(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 8)
    x3 = direct_neighbors(UNITY)
    x4 = insert(UNITY, x3)
    x5 = flatten(x2)
    x6 = erase_patch(I, x5)
    x7 = transform(upper_left_corner, x2)
    x8 = fix_first_argument(shift_by_vector, x4)
    x9 = transform_and_flatten(x8, x7)
    O = fill(x6, COLOR_TWO, x9)
    return O


def solve_23581191(I):
    x1 = as_objects(I, True, True, True)
    x2 = combine_two_function_results(union, vertical_line, horizontal_line)
    x3 = compose(x2, center)
    x4 = combine_two_function_results(recolor, get_color, x3)
    x5 = transform_and_flatten(x4, x1)
    x6 = paint_onto_grid(I, x5)
    x7 = combine_two_function_results(intersection, get_first, get_last)
    x8 = transform(x3, x1)
    x9 = x7(x8)
    O = fill(x6, COLOR_TWO, x9)
    return O


def solve_c8cbb738(I):
    x1 = most_common_color(I)
    x2 = partition_only_foreground(I)
    #x3 = valmax(x2, get_shape) # mdda: type abuse, since shape is not an int
    x3a = valmax(x2, get_height) # mdda: better type-wise
    x3b = valmax(x2, get_width) # mdda: better type-wise
    x3c = as_tuple(x3a, x3b) # mdda
    x4 = create_grid(x1, x3c) # mdda
    x5 = transform(shift_to_origin, x2)
    x6 = fix_first_argument(subtract, x3c) # mdda
    x7 = chain(halve, x6, get_shape)
    x8 = combine_two_function_results(shift_by_vector, identity, x7)
    x9 = transform_and_flatten(x8, x5)
    O = paint_onto_grid(x4, x9)
    return O


def solve_3eda0437(I):
    x1 = interval(2, 10, 1)
    x2 = apply_function_on_cartesian_product(as_tuple, x1, x1)
    x3 = fix_first_argument(create_grid, COLOR_ZERO)
    x4 = fix_first_argument(occurrences, I)
    x5 = fix_first_argument(fix_first_argument, shift_by_vector)
    x6 = combine_two_function_results(transform, x5, x4)
    x7 = chain(x6, as_object, x3)
    x8 = transform_and_flatten(x7, x2)
    x9 = argmax(x8, size)
    O = fill(I, COLOR_SIX, x9)
    return O


def solve_dc0a314f(I):
    x1 = of_color(I, COLOR_THREE)
    #x2 = replace(I, COLOR_THREE, COLOR_ZERO)  # mdda : Assumes that COLOR_BLACK < other colors
    x2 = replace(I, COLOR_THREE, COLOR_BELOW)  # mdda : FIXED
    x3 = diagonal_mirror(x2)
    x4 = transform_both(pairwise, x2, x3)
    x5 = fix_first_argument(transform, maximum)   # assumption here
    x6 = transform(x5, x4)
    x7 = counterdiagonal_mirror(x6)
    x8 = transform_both(pairwise, x6, x7)
    x9 = transform(x5, x8)
    O = smallest_subgrid_containing(x1, x9)
    return O


def solve_d4469b4b(I):
    x1 = palette(I)
    x2 = get_other(x1, COLOR_ZERO)
    x3 = is_equal(x2, COLOR_ONE)
    x4 = is_equal(x2, COLOR_TWO)
    x5 = condition_if_else(x3, UNITY, TWO_BY_TWO)
    x6 = condition_if_else(x4, RIGHT, x5)
    x7 = combine_two_function_results(union, vertical_line, horizontal_line)
    x8 = x7(x6)
    x9 = create_grid(COLOR_ZERO, THREE_BY_THREE)
    O = fill(x9, COLOR_FIVE, x8)
    return O


def solve_6ecd11f4(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmax(x1, size)
    x3 = argmin(x1, size)
    x4 = smallest_subgrid_containing(x2, I)
    x5 = smallest_subgrid_containing(x3, I)
    x6 = get_width(x4)
    x7 = get_width(x5)
    x8 = divide(x6, x7)
    x9 = downscale(x4, x8)
    x10 = of_color(x9, COLOR_ZERO)
    O = fill(x5, COLOR_ZERO, x10)
    return O


def solve_760b3cac(I):
    x1 = of_color(I, COLOR_FOUR)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = upper_left_corner(x1)
    x4 = color_at_location(I, x3)
    x5 = is_equal(x4, COLOR_FOUR)
    x6 = condition_if_else(x5, -1, 1)
    x7 = multiply(x6, 3)
    x8 = to_horizontal_vec(x7)
    x9 = vertical_mirror(x2)
    x10 = shift_by_vector(x9, x8)
    O = fill(I, COLOR_EIGHT, x10)
    return O


def solve_c444b776(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = argmin(x2, size)
    x4 = bounding_box_indices(x3)
    x5 = to_object(x4, I)
    x6 = shift_to_origin(x5)
    x7 = fix_first_argument(shift_by_vector, x6)
    x8 = compose(x7, upper_left_corner)
    x9 = transform_and_flatten(x8, x2)
    O = paint_onto_grid(I, x9)
    return O


def solve_d4a91cb9(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = of_color(I, COLOR_TWO)
    x3 = get_first(x1)
    x4 = get_first(x2)
    x5 = get_last(x3)
    x6 = get_first(x4)
    x7 = as_tuple(x6, x5)
    x8 = line_between(x7, x3)
    x9 = line_between(x7, x4)
    x10 = union(x8, x9)
    O = fill_background(I, COLOR_FOUR, x10)
    return O


def solve_eb281b96(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = decrement(x1)
    x4 = as_tuple(x3, x2)
    x5 = crop(I, ORIGIN, x4)
    x6 = horizontal_mirror(x5)
    x7 = vertical_concat(I, x6)
    x8 = double(x3)
    x9 = as_tuple(x8, x2)
    x10 = crop(x7, DOWN, x9)
    O = vertical_concat(x7, x10)
    return O


def solve_ff28f65a(I):
    x1 = as_objects(I, True, False, True)
    x2 = size(x1)
    x3 = double(x2)
    x4 = interval(0, x3, 2)
    x5 = transform(to_horizontal_vec, x4)
    x6 = as_tuple(1, 9)
    x7 = create_grid(COLOR_ZERO, x6)
    x8 = fill(x7, COLOR_ONE, x5)
    x9 = horizontal_split(x8, 3)
    O = flatten(x9)
    return O


def solve_7e0986d6(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = replace(I, x1, COLOR_ZERO)
    x4 = least_common_color(x3)
    x5 = fix_last_argument(color_count, x4)
    x6 = chain(is_positive, decrement, x5)
    x7 = fix_last_argument(to_object, x3)
    x8 = chain(x6, x7, direct_neighbors)
    x9 = keep_if_condition(x2, x8)
    O = fill(x3, x4, x9)
    return O


def solve_09629e4f(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmin(x1, count_colors)
    x3 = shift_to_origin(x2)
    x4 = upscale(x3, 4)
    x5 = paint_onto_grid(I, x4)
    x6 = of_color(I, COLOR_FIVE)
    O = fill(x5, COLOR_FIVE, x6)
    return O


def solve_a85d4709(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = fix_first_argument(equals, get_last)
    x3 = fix_first_argument(keep_if_condition, x1)
    x4 = fix_first_argument(transform_and_flatten, horizontal_line)
    x5 = chain(x4, x3, x2)
    x6 = x5(0)
    x7 = x5(2)
    x8 = x5(1)
    x9 = fill(I, COLOR_TWO, x6)
    x10 = fill(x9, COLOR_THREE, x7)
    O = fill(x10, COLOR_FOUR, x8)
    return O


def solve_feca6190(I):  # mdda : Not sure why this is color palette order dependent...  FIXED
    #x1 = as_objects(I, True, False, True)   # mdda : The test case is 0456 - so most common color isn't correct idea
    x1 = as_objects(I, True, False, False)   # mdda : All colors are valid since none is most common
    x1bg = color_filter(x1, COLOR_ZERO)      # mdda - take out COLOR_ZERO ourselves
    x1fg = difference(x1, x1bg)              # mdda - take out COLOR_ZERO ourselves
    x2 = size(x1fg)
    #x2 = size(x1)
    x3 = multiply(x2, 5)
    x4 = as_tuple(x3, x3)
    x5 = create_grid(COLOR_ZERO, x4)
    x6 = fix_last_argument(shoot, UNITY)
    x7 = compose(x6, center)
    x8 = combine_two_function_results(recolor, get_color, x7)
    #x9 = transform_and_flatten(x8, x1)
    x9 = transform_and_flatten(x8, x1fg)
    x10 = paint_onto_grid(x5, x9)
    O = horizontal_mirror(x10)
    return O


def solve_a68b268e(I):
    x1 = top_half(I)
    x2 = bottom_half(I)
    x3 = left_half(x1)
    x4 = right_half(x1)
    x5 = left_half(x2)
    x6 = right_half(x2)
    x7 = of_color(x4, COLOR_FOUR)
    x8 = of_color(x3, COLOR_SEVEN)
    x9 = of_color(x5, COLOR_EIGHT)
    x10 = fill(x6, COLOR_EIGHT, x9)
    x11 = fill(x10, COLOR_FOUR, x7)
    O = fill(x11, COLOR_SEVEN, x8)
    return O


def solve_beb8660c(I):
    x1 = get_shape(I)
    x2 = as_objects(I, True, False, True)
    x3 = compose(negate, size)
    x4 = sort(x2, x3)
    x5 = transform(shift_to_origin, x4)
    x6 = size(x5)
    x7 = interval(0, x6, 1)
    x8 = transform(to_vertical_vec, x7)
    x9 = transform_both_and_flatten(shift_by_vector, x5, x8)
    x10 = create_grid(COLOR_ZERO, x1)
    x11 = paint_onto_grid(x10, x9)
    O = rot180(x11)
    return O


def solve_913fb3ed(I):
    x1 = of_color(I, COLOR_THREE)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = of_color(I, COLOR_TWO)
    x4 = transform_and_flatten(neighbors, x1)
    x5 = transform_and_flatten(neighbors, x2)
    x6 = transform_and_flatten(neighbors, x3)
    x7 = fill(I, COLOR_SIX, x4)
    x8 = fill(x7, COLOR_FOUR, x5)
    O = fill(x8, COLOR_ONE, x6)
    return O


def solve_0962bcdd(I):
    x1 = least_common_color(I)
    x2 = replace(I, COLOR_ZERO, x1)
    x3 = least_common_color(x2)
    x4 = of_color(I, x3)
    x5 = transform_and_flatten(direct_neighbors, x4)
    x6 = fill(I, x3, x5)
    x7 = as_objects(x6, False, True, True)
    x8 = combine_two_function_results(line_between, upper_left_corner, lower_right_corner)
    x9 = combine_two_function_results(line_between, lower_left_corner, upper_right_corner)
    x10 = combine_two_function_results(union, x8, x9)
    x11 = transform_and_flatten(x10, x7)
    O = fill(x6, x1, x11)
    return O


def solve_3631a71a(I):
    x1 = get_shape(I)
    #x2 = replace(I, COLOR_NINE, COLOR_ZERO)
    x2 = replace(I, COLOR_NINE, COLOR_BELOW)  # mdda new
    x3 = fix_first_argument(transform, maximum)  # mdda : Is this over colors??  FIXED now since PLACEHOLDER<other_colors
    x4 = diagonal_mirror(x2)
    x5 = transform_both(pairwise, x2, x4)
    x6pre = transform(x3, x5)
    x6 = replace(x6pre, COLOR_BELOW, COLOR_ZERO)  # mdda changed - refers to old x6
    x7 = subtract(x1, TWO_BY_TWO)
    x8 = crop(x6, TWO_BY_TWO, x7)
    x9 = vertical_mirror(x8)
    x10 = as_objects(x9, True, False, True)
    x11 = flatten(x10)
    x12 = shift_by_vector(x11, TWO_BY_TWO)
    O = paint_onto_grid(x6, x12)
    return O


def solve_05269061(I):
    x1 = as_objects(I, True, True, True)
    x2 = neighbors(ORIGIN)
    x3 = transform_and_flatten(neighbors, x2)
    x4 = fix_last_argument(multiply, 3)
    x5 = transform(x4, x3)
    x6 = flatten(x1)
    x7 = fix_first_argument(shift_by_vector, x6)
    x8 = transform_and_flatten(x7, x5)
    x9 = shift_by_vector(x8, UP_RIGHT)
    x10 = shift_by_vector(x8, DOWN_LEFT)
    x11 = paint_onto_grid(I, x8)
    x12 = paint_onto_grid(x11, x9)
    O = paint_onto_grid(x12, x10)
    return O


def solve_95990924(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform(outbox, x1)
    x3 = transform(upper_left_corner, x2)
    x4 = transform(upper_right_corner, x2)
    x5 = transform(lower_left_corner, x2)
    x6 = transform(lower_right_corner, x2)
    x7 = fill(I, COLOR_ONE, x3)
    x8 = fill(x7, COLOR_TWO, x4)
    x9 = fill(x8, COLOR_THREE, x5)
    O = fill(x9, COLOR_FOUR, x6)
    return O


def solve_e509e548(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_last_argument(smallest_subgrid_containing, I)
    x3 = chain(palette, trim_border, x2)
    x4 = fix_first_argument(contains, COLOR_THREE)
    x5 = compose(x4, x3)
    x6 = combine_two_function_results(add, get_height, get_width)
    x7 = compose(decrement, x6)
    x8 = combine_two_function_results(is_equal, size, x7)
    x9 = keep_if_condition_and_flatten(x1, x5)
    x10 = keep_if_condition_and_flatten(x1, x8)
    x11 = replace(I, COLOR_THREE, COLOR_SIX)
    x12 = fill(x11, COLOR_TWO, x9)
    O = fill(x12, COLOR_ONE, x10)
    return O


def solve_d43fd935(I):
    x1 = as_objects(I, True, False, True)
    x2 = of_color(I, COLOR_THREE)
    x3 = size_filter(x1, 1)
    x4 = fix_last_argument(vertical_matching, x2)
    x5 = fix_last_argument(horizontal_matching, x2)
    x6 = combine_two_function_results(logical_or, x4, x5)
    x7 = keep_if_condition(x3, x6)
    x8 = fix_last_argument(move_until_touching, x2)
    x9 = combine_two_function_results(add, center, x8)
    x10 = combine_two_function_results(line_between, center, x9)
    x11 = combine_two_function_results(recolor, get_color, x10)
    x12 = transform_and_flatten(x11, x7)
    O = paint_onto_grid(I, x12)
    return O


def solve_db3e9e38(I):
    x1 = of_color(I, COLOR_SEVEN)
    x2 = lower_right_corner(x1)
    x3 = shoot(x2, UP_RIGHT)
    x4 = shoot(x2, NEG_UNITY)
    x5 = union(x3, x4)
    x6 = fix_last_argument(shoot, UP)
    x7 = transform_and_flatten(x6, x5)
    x8 = get_last(x2)
    x9 = fix_last_argument(subtract, x8)
    x10 = chain(is_even, x9, get_last)
    x11 = fill(I, COLOR_EIGHT, x7)
    x12 = keep_if_condition(x7, x10)
    O = fill(x11, COLOR_SEVEN, x12)
    return O


def solve_e73095fd(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = combine_two_function_results(is_equal, to_indices, bounding_box_indices)
    x4 = keep_if_condition(x2, x3)
    x5 = fix_first_argument(transform_and_flatten, direct_neighbors)
    x6 = chain(x5, corner_indices, outbox)
    x7 = combine_two_function_results(difference, x6, outbox)
    x8 = of_color(I, COLOR_FIVE)
    x9 = fix_last_argument(intersection, x8)
    x10 = equals(size, 0)
    x11 = chain(x10, x9, x7)
    x12 = keep_if_condition_and_flatten(x4, x11)
    O = fill(I, COLOR_FOUR, x12)
    return O


def solve_1bfc4729(I):
    x1 = as_indices(I)
    x2 = top_half(I)
    x3 = bottom_half(I)
    x4 = least_common_color(x2)
    x5 = least_common_color(x3)
    x6 = horizontal_line(TWO_BY_ZERO)
    x7 = box(x1)
    x8 = union(x6, x7)
    x9 = fill(x2, x4, x8)
    x10 = horizontal_mirror(x9)
    x11 = replace(x10, x4, x5)
    O = vertical_concat(x9, x11)
    return O


def solve_93b581b8(I):
    x1 = partition_only_foreground(I)
    x2 = chain(counterdiagonal_mirror, diagonal_mirror, flatten)
    x3 = x2(x1)
    x4 = upscale(x3, 3)
    x5 = as_tuple(-2, -2)
    x6 = shift_by_vector(x4, x5)
    x7 = paint_onto_grid_background(I, x6)
    x8 = to_indices(x3)
    x9 = combine_two_function_results(union, horizontal_line, vertical_line)
    x10 = transform_and_flatten(x9, x8)
    x11 = difference(x10, x8)
    O = fill(x7, COLOR_ZERO, x11)
    return O


def solve_9edfc990(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = of_color(I, COLOR_ONE)
    x4 = fix_last_argument(adjacent, x3)
    x5 = keep_if_condition_and_flatten(x2, x4)
    x6 = recolor(COLOR_ONE, x5)
    O = paint_onto_grid(I, x6)
    return O


def solve_a65b410d(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = upper_right_corner(x1)
    x3 = shoot(x2, UP_RIGHT)
    x4 = shoot(x2, DOWN_LEFT)
    x5 = fill_background(I, COLOR_THREE, x3)
    x6 = fill_background(x5, COLOR_ONE, x4)
    x7 = fix_last_argument(shoot, LEFT)
    x8 = transform_and_flatten(x7, x3)
    x9 = transform_and_flatten(x7, x4)
    x10 = fill_background(x6, COLOR_ONE, x9)
    O = fill_background(x10, COLOR_THREE, x8)
    return O


def solve_7447852a(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = compose(get_last, center)
    x4 = sort(x2, x3)
    x5 = size(x4)
    x6 = interval(0, x5, 3)
    x7 = fix_last_argument(contains, x6)
    x8 = compose(x7, get_last)
    x9 = interval(0, x5, 1)
    x10 = pairwise(x4, x9)
    x11 = keep_if_condition(x10, x8)
    x12 = transform_and_flatten(get_first, x11)
    O = fill(I, COLOR_FOUR, x12)
    return O


def solve_97999447(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform(to_indices, x1)
    x3 = fix_last_argument(shoot, RIGHT)
    x4 = compose(x3, center)
    x5 = combine_two_function_results(recolor, get_color, x4)
    x6 = transform_and_flatten(x5, x1)
    x7 = paint_onto_grid(I, x6)
    x8 = interval(0, 5, 1)
    x9 = transform(double, x8)
    x10 = transform(increment, x9)
    x11 = transform(to_horizontal_vec, x10)
    x12 = apply_function_on_cartesian_product(shift_by_vector, x2, x11)
    x13 = flatten(x12)
    O = fill(x7, COLOR_FIVE, x13)
    return O


def solve_91714a58(I):
    x1 = get_shape(I)
    x2 = as_indices(I)
    x3 = as_objects(I, True, False, True)
    x4 = argmax(x3, size)
    x5 = most_common_color(x4)
    x6 = create_grid(COLOR_ZERO, x1)
    x7 = paint_onto_grid(x6, x4)
    x8 = fix_last_argument(to_object, x7)
    x9 = fix_last_argument(color_count, x5)
    x10 = chain(x9, x8, neighbors)
    x11 = fix_first_argument(greater_than, 3)
    x12 = compose(x11, x10)
    x13 = keep_if_condition(x2, x12)
    O = fill(x7, COLOR_ZERO, x13)
    return O


def solve_a61ba2ce(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_first_argument(color_at_location, I)
    x3 = equals(x2, COLOR_ZERO)
    x4 = fix_first_argument(extract_first_matching, x1)
    x5 = fix_last_argument(smallest_subgrid_containing, I)
    x6 = fix_first_argument(compose, x3)
    x7 = chain(x5, x4, x6)
    x8 = x7(upper_left_corner)
    x9 = x7(upper_right_corner)
    x10 = x7(lower_left_corner)
    x11 = x7(lower_right_corner)
    x12 = horizontal_concat(x11, x10)
    x13 = horizontal_concat(x9, x8)
    O = vertical_concat(x12, x13)
    return O


def solve_8e1813be(I):
    x1 = replace(I, COLOR_FIVE, COLOR_ZERO)
    x2 = as_objects(x1, True, True, True)
    x3 = get_first(x2)
    x4 = is_vertical_line(x3)
    x5 = condition_if_else(x4, diagonal_mirror, identity)
    x6 = x5(x1)
    x7 = as_objects(x6, True, True, True)
    x8 = sort(x7, uppermost)
    x9 = transform(get_color, x8)
    x10 = remove_duplicates(x9)
    x11 = size(x10)
    x12 = fix_last_argument(repeat, x11)
    x13 = transform(x12, x10)
    O = x5(x13)
    return O


def solve_bc1d5164(I):
    x1 = least_common_color(I)
    x2 = crop(I, ORIGIN, THREE_BY_THREE)
    x3 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x4 = to_horizontal_vec(4)
    x5 = crop(I, x4, THREE_BY_THREE)
    x6 = as_tuple(2, 4)
    x7 = crop(I, x6, THREE_BY_THREE)
    x8 = create_grid(COLOR_ZERO, THREE_BY_THREE)
    x9 = fix_last_argument(of_color, x1)
    #x10 = as_tuple(x2, x3)
    x10 = as_generic_tuple(x2, x3)  # mdda
    #x11 = as_tuple(x5, x7)
    x11 = as_generic_tuple(x5, x7)  # mdda
    x12 = union(x10, x11)
    x13 = transform_and_flatten(x9, x12)
    O = fill(x8, x1, x13)
    return O


def solve_ce602527(I):
    x1 = vertical_mirror(I)
    x2 = partition_only_foreground(x1)
    x3 = sort(x2, size)
    x4 = get_last(x3)
    x5 = remove(x4, x3)
    x6 = compose(to_indices, shift_to_origin)
    x7 = fix_last_argument(upscale, 2)
    x8 = chain(to_indices, x7, shift_to_origin)
    x9 = x6(x4)
    x10 = fix_last_argument(intersection, x9)
    x11 = chain(size, x10, x8)
    x12 = argmax(x5, x11)
    x13 = smallest_subgrid_containing(x12, x1)
    O = vertical_mirror(x13)
    return O


def solve_5c2c9af4(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = center(x2)
    x4 = upper_left_corner(x2)
    x5 = subtract(x3, x4)
    x6 = multiply(-1, 9)
    x7 = interval(0, 9, 1)
    x8 = interval(0, x6, -1)
    x9 = fix_first_argument(multiply, x5)
    x10 = transform(x9, x7)
    x11 = transform(x9, x8)
    x12 = pairwise(x10, x11)
    x13 = transform_and_flatten(box, x12)
    x14 = shift_by_vector(x13, x3)
    O = fill(I, x1, x14)
    return O


def solve_75b8110e(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = top_half(x1)
    x4 = bottom_half(x1)
    x5 = top_half(x2)
    x6 = bottom_half(x2)
    x7 = fix_last_argument(of_color, COLOR_ZERO)
    x8 = combine_two_function_results(difference, as_indices, x7)
    x9 = combine_two_function_results(to_object, x8, identity)
    x10 = x9(x5)
    x11 = x9(x4)
    x12 = x9(x6)
    x13 = paint_onto_grid(x3, x12)
    x14 = paint_onto_grid(x13, x11)
    O = paint_onto_grid(x14, x10)
    return O


def solve_941d9a10(I):
    x1 = get_shape(I)
    x2 = as_objects(I, True, False, False)
    x3 = color_filter(x2, COLOR_ZERO)
    x4 = transform(to_indices, x3)
    x5 = fix_first_argument(fix_first_argument, contains)
    x6 = fix_first_argument(extract_first_matching, x4)
    x7 = compose(x6, x5)
    x8 = decrement(x1)
    x9 = as_tuple(5, 5)
    x10 = x7(ORIGIN)
    x11 = x7(x8)
    x12 = x7(x9)
    x13 = fill(I, COLOR_ONE, x10)
    x14 = fill(x13, COLOR_THREE, x11)
    O = fill(x14, COLOR_TWO, x12)
    return O


def solve_c3f564a4(I):
    x1 = as_indices(I)
    x2 = diagonal_mirror(I)
    x3 = negate(9)
    x4 = transform_both(pairwise, I, x2)
    x5 = fix_first_argument(transform, maximum)
    x6 = transform(x5, x4)
    x7 = of_color(x6, COLOR_ZERO)
    x8 = difference(x1, x7)
    x9 = to_object(x8, x6)
    x10 = interval(x3, 9, 1)
    x11 = interval(9, x3, -1)
    x12 = pairwise(x10, x11)
    x13 = fix_first_argument(shift_by_vector, x9)
    x14 = transform_and_flatten(x13, x12)
    O = paint_onto_grid(x6, x14)
    return O


def solve_1a07d186(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = difference(x1, x2)
    x4 = transform(get_color, x3)
    x5 = fix_last_argument(contains, x4)
    x6 = compose(x5, get_color)
    x7 = keep_if_condition(x2, x6)
    x8 = fix_first_argument(color_filter, x3)
    x9 = chain(get_first, x8, get_color)
    x10 = combine_two_function_results(move_until_touching, identity, x9)
    x11 = combine_two_function_results(shift_by_vector, identity, x10)
    x12 = transform_and_flatten(x11, x7)
    x13 = flatten(x2)
    x14 = erase_patch(I, x13)
    O = paint_onto_grid(x14, x12)
    return O


def solve_d687bc17(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = difference(x1, x2)
    x4 = transform(get_color, x3)
    x5 = fix_last_argument(contains, x4)
    x6 = compose(x5, get_color)
    x7 = keep_if_condition(x2, x6)
    x8 = fix_first_argument(color_filter, x3)
    x9 = chain(get_first, x8, get_color)
    x10 = combine_two_function_results(move_until_touching, identity, x9)
    x11 = combine_two_function_results(shift_by_vector, identity, x10)
    x12 = flatten(x2)
    x13 = transform_and_flatten(x11, x7)
    x14 = erase_patch(I, x12)
    O = paint_onto_grid(x14, x13)
    return O


def solve_9af7a82c(I):
    x1 = as_objects(I, True, False, False)
    x2 = sort(x1, size)
    x3 = valmax(x1, size)
    x4 = fix_last_argument(as_tuple, 1)
    x5 = fix_first_argument(subtract, x3)
    x6 = compose(x4, size)
    x7 = chain(x4, x5, size)
    x8 = combine_two_function_results(create_grid, get_color, x6)
    x9 = fix_first_argument(create_grid, COLOR_ZERO)
    x10 = compose(x9, x7)
    x11 = combine_two_function_results(vertical_concat, x8, x10)
    x12 = compose(counterdiagonal_mirror, x11)
    x13 = transform(x12, x2)
    x14 = flatten(x13)
    O = counterdiagonal_mirror(x14)
    return O


def solve_6e19193c(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = fix_last_argument(to_object, I)
    x4 = compose(get_first, bounding_box_delta)
    x5 = fix_last_argument(color_count, x1)
    x6 = equals(x5, 2)
    x7 = chain(x6, x3, direct_neighbors)
    x8 = fix_last_argument(keep_if_condition, x7)
    x9 = chain(get_first, x8, to_indices)
    x10 = combine_two_function_results(subtract, x4, x9)
    x11 = combine_two_function_results(shoot, x4, x10)
    x12 = transform_and_flatten(x11, x2)
    x13 = fill(I, x1, x12)
    x14 = transform_and_flatten(bounding_box_delta, x2)
    O = fill(x13, COLOR_ZERO, x14)
    return O


def solve_ef135b50(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_ZERO)
    x3 = cartesian_product(x1, x1)
    x4 = power(get_first, 2)
    x5 = compose(get_first, get_last)
    x6 = combine_two_function_results(is_equal, x4, x5)
    x7 = keep_if_condition(x3, x6)
    x8 = combine_two_function_results(line_between, get_first, get_last)
    x9 = transform_and_flatten(x8, x7)
    x10 = intersection(x9, x2)
    x11 = fill(I, COLOR_NINE, x10)
    x12 = trim_border(x11)
    x13 = as_object(x12)
    x14 = shift_by_vector(x13, UNITY)
    O = paint_onto_grid(I, x14)
    return O


def solve_cbded52d(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = cartesian_product(x2, x2)
    x4 = combine_two_function_results(vertical_matching, get_first, get_last)
    x5 = combine_two_function_results(horizontal_matching, get_first, get_last)
    x6 = combine_two_function_results(logical_or, x4, x5)
    x7 = keep_if_condition(x3, x6)
    x8 = compose(center, get_first)
    x9 = compose(center, get_last)
    x10 = combine_two_function_results(line_between, x8, x9)
    x11 = chain(initset, center, x10)
    x12 = compose(get_color, get_first)
    x13 = combine_two_function_results(recolor, x12, x11)
    x14 = transform_and_flatten(x13, x7)
    O = paint_onto_grid(I, x14)
    return O


def solve_8a004b2b(I):
    x1 = as_objects(I, False, True, True)
    x2 = of_color(I, COLOR_FOUR)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = argmax(x1, lowermost)
    x5 = shift_to_origin(x4)
    x6 = replace(x3, COLOR_FOUR, COLOR_ZERO)
    x7 = as_objects(x6, True, False, True)
    x8 = flatten(x7)
    x9 = get_width(x8)
    x10 = upper_left_corner(x8)
    x11 = get_width(x4)
    x12 = divide(x9, x11)
    x13 = upscale(x5, x12)
    x14 = shift_by_vector(x13, x10)
    O = paint_onto_grid(x3, x14)
    return O


def solve_e26a3af2(I):
    x1 = rot90(I)
    x2 = transform(most_common, I)
    x3 = transform(most_common, x1)
    x4 = repeat(x2, 1)
    x5 = repeat(x3, 1)
    x6 = compose(size, remove_duplicates)
    x7 = x6(x2)
    x8 = x6(x3)
    x9 = greater_than(x8, x7)
    x10 = condition_if_else(x9, get_height, get_width)
    x11 = x10(I)
    x12 = rot90(x4)
    x13 = condition_if_else(x9, x5, x12)
    x14 = condition_if_else(x9, vertical_upscale, horizontal_upscale)
    O = x14(x13, x11)
    return O


def solve_6cf79266(I):
    x1 = of_color(I, COLOR_ZERO)
    #x2 = as_tuple(COLOR_ZERO, ORIGIN)
    x2 = make_cell(COLOR_ZERO, ORIGIN) # mdda
    x3 = initset(x2)
    x4 = upscale(x3, 3)
    x5 = to_indices(x4)
    x6 = fix_first_argument(shift_by_vector, x5)
    x7 = fix_last_argument(difference, x1)
    x8 = chain(size, x7, x6)
    x9 = equals(x8, 0)
    x10 = fix_first_argument(add, NEG_UNITY)
    x11 = chain(logical_not, x9, x10)
    x12 = combine_two_function_results(logical_and, x9, x11)
    x13 = keep_if_condition(x1, x12)
    x14 = transform_and_flatten(x6, x13)
    O = fill(I, COLOR_ONE, x14)
    return O


def solve_a87f7484(I):
    x1 = count_colors(I)
    #x2 = diagonal_mirror(I)  # Unused?
    x3 = is_portrait(I)
    m4 = condition_if_else(x3, diagonal_mirror, identity)
    x5 = m4(I)
    x6 = decrement(x1)
    x7 = horizontal_split(x5, x6)
    x8 = fix_last_argument(of_color, COLOR_ZERO)
    x9 = transform(x8, x7)
    x10 = least_common(x9)
    x11 = equals(x8, x10)
    x12 = extract_first_matching(x7, x11)
    O = m4(x12)
    return O


def solve_4093f84a(I):
    x1 = least_common_color(I)
    x2 = replace(I, x1, COLOR_FIVE)
    x3 = of_color(I, COLOR_FIVE)
    x4 = is_portrait(x3)
    m5 = condition_if_else(x4, identity, diagonal_mirror)
    x6pre = m5(x2)
    x6 = replace(x6pre, COLOR_ZERO, COLOR_BELOW)  # mdda - added
    x7 = left_half(x6)
    x8 = right_half(x6)
    x9 = fix_last_argument(sort, identity)  # mdda: depends on BLACK being < other colors NAUGHTY  FIXED
    x10 = fix_last_argument(sort, negate)   # mdda: depends on BLACK being < other colors NAUGHTY  FIXED
    x11 = transform(x9, x7)
    x12 = transform(x10, x8)
    x13pre = horizontal_concat(x11, x12)
    x13 = replace(x13pre, COLOR_BELOW, COLOR_ZERO)  # mdda - added
    O = m5(x13)  
    return O


def solve_ba26e723(I):
    x1 = fix_last_argument(divide, 3)
    x2 = fix_last_argument(multiply, 3)
    x3 = compose(x2, x1)
    x4 = combine_two_function_results(is_equal, identity, x3)
    x5 = compose(x4, get_last)
    x6 = of_color(I, COLOR_FOUR)
    x7 = keep_if_condition(x6, x5)
    O = fill(I, COLOR_SIX, x7)
    return O


def solve_4612dd53(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = box(x1)
    x3 = fill(I, COLOR_TWO, x2)
    x4 = smallest_subgrid_containing(x1, x3)
    x5 = of_color(x4, COLOR_ONE)
    x6 = transform_and_flatten(vertical_line, x5)
    x7 = transform_and_flatten(horizontal_line, x5)
    x8 = size(x6)
    x9 = size(x7)
    x10 = greater_than(x8, x9)
    x11 = condition_if_else(x10, x7, x6)
    x12 = fill(x4, COLOR_TWO, x11)
    x13 = of_color(x12, COLOR_TWO)
    x14 = upper_left_corner(x1)
    x15 = shift_by_vector(x13, x14)
    O = fill_background(I, COLOR_TWO, x15)
    return O


def solve_29c11459(I):
    x1 = left_half(I)
    x2 = right_half(I)
    x3 = as_objects(x2, True, False, True)
    x4 = as_objects(x1, True, False, True)
    x5 = compose(horizontal_line, center)
    x6 = combine_two_function_results(recolor, get_color, x5)
    x7 = transform_and_flatten(x6, x4)
    x8 = paint_onto_grid(x1, x7)
    x9 = transform_and_flatten(x6, x3)
    x10 = paint_onto_grid(I, x9)
    x11 = as_objects(x8, True, False, True)
    x12 = transform(upper_right_corner, x11)
    x13 = shift_by_vector(x12, RIGHT)
    x14 = flatten(x11)
    x15 = paint_onto_grid(x10, x14)
    O = fill(x15, COLOR_FIVE, x13)
    return O


def solve_963e52fc(I):
    x1 = get_width(I)
    x2 = as_object(I)
    x3 = horizontal_periodicity(x2)
    x4 = get_height(x2)
    x5 = as_tuple(x4, x3)
    x6 = upper_left_corner(x2)
    x7 = crop(I, x6, x5)
    x8 = rot90(x7)
    x9 = double(x1)
    x10 = divide(x9, x3)
    x11 = increment(x10)
    x12 = repeat(x8, x11)
    x13 = flatten(x12)
    x14 = rot270(x13)
    x15 = as_tuple(x4, x9)
    O = crop(x14, ORIGIN, x15)
    return O


def solve_ae3edfdc(I):
    x1 = as_objects(I, True, False, True)
    x2 = replace(I, COLOR_THREE, COLOR_ZERO)
    x3 = replace(x2, COLOR_SEVEN, COLOR_ZERO)
    x4 = fix_first_argument(color_filter, x1)
    x5 = fix_first_argument(fix_last_argument, move_until_touching)
    x6 = chain(x5, get_first, x4)
    x7 = x6(COLOR_TWO)
    x8 = x6(COLOR_ONE)
    x9 = x4(COLOR_THREE)
    x10 = x4(COLOR_SEVEN)
    x11 = combine_two_function_results(shift_by_vector, identity, x7)
    x12 = combine_two_function_results(shift_by_vector, identity, x8)
    x13 = transform_and_flatten(x11, x9)
    x14 = transform_and_flatten(x12, x10)
    x15 = paint_onto_grid(x3, x13)
    O = paint_onto_grid(x15, x14)
    return O


def solve_1f0c79e5(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = replace(I, COLOR_TWO, COLOR_ZERO)
    x3 = least_common_color(x2)
    x4 = of_color(x2, x3)
    x5 = union(x1, x4)
    x6 = recolor(x3, x5)
    x7 = compose(decrement, double)
    x8 = upper_left_corner(x5)
    x9 = negate(x8)
    x10 = shift_by_vector(x1, x9)
    x11 = transform(x7, x10)
    x12 = interval(0, 9, 1)
    x13 = apply_function_on_cartesian_product(multiply, x11, x12)
    x14 = fix_first_argument(shift_by_vector, x6)
    x15 = transform_and_flatten(x14, x13)
    O = paint_onto_grid(I, x15)
    return O


def solve_56dc2b01(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_THREE)
    x3 = get_first(x2)
    x4 = of_color(I, COLOR_TWO)
    x5 = move_until_touching(x3, x4)
    x6 = get_first(x5)
    x7 = is_equal(x6, 0)
    x8 = condition_if_else(x7, get_width, get_height)
    x9 = x8(x3)
    x10 = move_until_touching(x4, x3)
    x11 = sign(x10)
    x12 = multiply(x11, x9)
    x13 = crement(x12)
    x14 = recolor(COLOR_EIGHT, x4)
    x15 = shift_by_vector(x14, x13)
    x16 = paint_onto_grid(I, x15)
    O = move_object(x16, x3, x5)
    return O


def solve_e48d4e1a(I):
    x1 = get_shape(I)
    x2 = of_color(I, COLOR_FIVE)
    x3 = fill(I, COLOR_ZERO, x2)
    x4 = least_common_color(x3)
    x5 = size(x2)
    x6 = of_color(I, x4)
    x7 = fix_last_argument(to_object, I)
    x8 = fix_last_argument(color_count, x4)
    x9 = chain(x8, x7, direct_neighbors)
    x10 = equals(x9, 4)
    x11 = extract_first_matching(x6, x10)
    x12 = multiply(DOWN_LEFT, x5)
    x13 = add(x12, x11)
    x14 = create_grid(COLOR_ZERO, x1)
    x15 = combine_two_function_results(union, vertical_line, horizontal_line)
    x16 = x15(x13)
    O = fill(x14, x4, x16)
    return O


def solve_6773b310(I):
    x1 = remove_solid_color_strips_from_grid(I)
    x2 = neighbors(ORIGIN)
    x3 = insert(ORIGIN, x2)
    x4 = fix_last_argument(multiply, 3)
    x5 = transform(x4, x3)
    x6 = as_tuple(4, 4)
    x7 = shift_by_vector(x5, x6)
    x8 = combine_two_function_results(insert, identity, neighbors)
    x9 = transform(x8, x7)
    x10 = fix_last_argument(to_object, x1)
    x11 = transform(x10, x9)
    x12 = fix_last_argument(color_count, COLOR_SIX)
    x13 = equals(x12, 2)
    x14 = keep_if_condition_and_flatten(x11, x13)
    x15 = fill(x1, COLOR_ONE, x14)
    x16 = replace(x15, COLOR_SIX, COLOR_ZERO)
    O = downscale(x16, 3)
    return O


def solve_780d0b14(I):
    x1 = as_indices(I)
    x2 = as_objects(I, True, True, True)
    x3 = fix_last_argument(greater_than, 2)
    x4 = compose(x3, size)
    x5 = keep_if_condition(x2, x4)
    x6 = to_tuple(x5)
    x7 = transform(get_color, x6)
    x8 = transform(center, x6)
    x9 = pairwise(x7, x8)
    x10 = fill(I, COLOR_ZERO, x1)
    x11 = paint_onto_grid(x10, x9)
    x12 = fix_last_argument(greater_than, 1)
    x13 = compose(remove_duplicates, to_tuple)
    x14 = chain(x12, size, x13)
    x15 = keep_if_condition(x11, x14)
    x16 = rot90(x15)
    x17 = keep_if_condition(x16, x14)
    O = rot270(x17)
    return O


def solve_2204b7a8(I):
    x1 = as_objects(I, True, False, True)
    x2 = fix_first_argument(keep_if_condition, x1)
    x3 = compose(size, x2)
    x4 = x3(is_vertical_line)
    x5 = x3(is_horizontal_line)
    x6 = greater_than(x4, x5)
    x7 = condition_if_else(x6, left_half, top_half)
    x8 = condition_if_else(x6, right_half, bottom_half)
    x9 = condition_if_else(x6, horizontal_concat, vertical_concat)
    x10 = x7(I)
    x11 = x8(I)
    x12 = color_at_location(x10, ORIGIN)
    x13 = get_shape(x11)
    x14 = decrement(x13)
    x15 = color_at_location(x11, x14)
    x16 = replace(x10, COLOR_THREE, x12)
    x17 = replace(x11, COLOR_THREE, x15)
    O = x9(x16, x17)
    return O


def solve_d9f24cd1(I):  # mdda : Fixed - count_colors should be compared to int, not COLOR
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_FIVE)
    x3 = apply_function_on_cartesian_product(line_between, x1, x2)
    x4 = keep_if_condition_and_flatten(x3, is_vertical_line)
    x5 = fill_background(I, COLOR_TWO, x4)        # Draw lines up to COLOR_TWO points
    x6 = equals(count_colors, 2)       
    x7 = as_objects(x5, False, False, True) # Get objects now
    x8 = keep_if_condition(x7, x6)          # The lines with 2 colors
    x9 = difference(x7, x8)                 # The single points
    x10 = color_filter(x9, COLOR_TWO)
    x11 = transform_and_flatten(to_indices, x10)  # Just the solitary COLOR_TWO points
    x12 = transform(upper_right_corner, x8)
    x13 = shift_by_vector(x12, UNITY)
    x14 = fix_last_argument(shoot, UP)
    x15 = transform_and_flatten(x14, x13)
    x16 = fill(x5, COLOR_TWO, x15)
    x17 = transform_and_flatten(vertical_line, x11)   # Shoot the solitary ones up
    O = fill(x16, COLOR_TWO, x17)
    return O


def solve_b782dc8a(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, False)
    x3 = of_color(I, x1)
    x4 = get_first(x3)
    x5 = direct_neighbors(x4)
    x6 = to_object(x5, I)
    x7 = most_common_color(x6)
    x8 = of_color(I, x7)
    x9 = color_filter(x2, COLOR_ZERO)
    x10 = fix_last_argument(adjacent, x8)
    x11 = keep_if_condition_and_flatten(x9, x10)
    x12 = to_indices(x11)
    x13 = fix_last_argument(manhattan_distance, x3)
    x14 = chain(is_even, x13, initset)
    x15 = keep_if_condition(x12, x14)
    x16 = difference(x12, x15)
    x17 = fill(I, x1, x15)
    O = fill(x17, x7, x16)
    return O


def solve_673ef223(I):
    x1 = as_objects(I, True, False, True)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = replace(I, COLOR_EIGHT, COLOR_FOUR)
    x4 = color_filter(x1, COLOR_TWO)
    x5 = argmin(x1, uppermost)
    x6 = transform(uppermost, x4)
    x7 = combine_two_function_results(subtract, maximum, minimum)
    x8 = x7(x6)
    x9 = to_vertical_vec(x8)
    x10 = leftmost(x5)
    x11 = is_equal(x10, 0)
    x12 = condition_if_else(x11, LEFT, RIGHT)
    x13 = fix_last_argument(shoot, x12)
    x14 = transform_and_flatten(x13, x2)
    x15 = fill_background(x3, COLOR_EIGHT, x14)
    x16 = shift_by_vector(x2, x9)
    x17 = transform_and_flatten(horizontal_line, x16)
    O = fill_background(x15, COLOR_EIGHT, x17)
    return O


def solve_f5b8619d(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = transform_and_flatten(vertical_line, x2)
    x4 = fill_background(I, COLOR_EIGHT, x3)
    x5 = horizontal_concat(x4, x4)
    O = vertical_concat(x5, x5)
    return O


def solve_f8c80d96(I):
    x1 = least_common_color(I)
    x2 = as_objects(I, True, False, False)
    x3 = color_filter(x2, x1)
    x4 = argmax(x3, size)
    x5 = argmin(x2, get_width)
    x6 = size(x5)
    x7 = is_equal(x6, 1)   # mdda : Fix bad use of COLOR_1
    x8 = condition_if_else(x7, identity, outbox)
    x9 = chain(outbox, outbox, x8)
    x10 = power(x9, 2)
    x11 = power(x9, 3)
    x12 = x9(x4)
    x13 = x10(x4)
    x14 = x11(x4)
    x15 = fill(I, x1, x12)
    x16 = fill(x15, x1, x13)
    x17 = fill(x16, x1, x14)
    O = replace(x17, COLOR_ZERO, COLOR_FIVE)
    return O


def solve_ecdecbb3(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_TWO)
    x3 = color_filter(x1, COLOR_EIGHT)
    x4 = cartesian_product(x2, x3)
    x5 = combine_two_function_results(move_until_touching, get_first, get_last)
    x6 = compose(crement, x5)
    x7 = compose(center, get_first)
    x8 = combine_two_function_results(add, x7, x6)
    x9 = combine_two_function_results(line_between, x7, x8)
    x10 = transform(x9, x4)
    x11 = fix_first_argument(greater_than, 8)
    x12 = compose(x11, size)
    x13 = keep_if_condition_and_flatten(x10, x12)
    x14 = fill(I, COLOR_TWO, x13)
    x15 = transform(x8, x4)
    x16 = intersection(x13, x15)
    x17 = transform_and_flatten(neighbors, x16)
    O = fill(x14, COLOR_EIGHT, x17)
    return O


def solve_e5062a87(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = recolor(COLOR_ZERO, x1)
    x3 = shift_to_origin(x2)
    x4 = occurrences(I, x2)
    x5 = fix_first_argument(shift_by_vector, x3)
    x6 = transform(x5, x4)
    x7 = as_tuple(1, 3)
    x8 = as_tuple(5, 1)
    x9 = as_tuple(2, 6)
    x10 = initset(x7)
    x11 = insert(x8, x10)
    x12 = insert(x9, x11)
    x13 = fix_last_argument(contains, x12)
    x14 = chain(logical_not, x13, upper_left_corner)
    x15 = keep_if_condition(x6, x14)
    x16 = flatten(x15)
    x17 = recolor(COLOR_TWO, x16)
    O = paint_onto_grid(I, x17)
    return O


def solve_a8d7556c(I):
    x1 = initset(ORIGIN)
    x2 = recolor(COLOR_ZERO, x1)
    x3 = upscale(x2, 2)
    x4 = occurrences(I, x3)
    x5 = fix_first_argument(shift_by_vector, x3)
    x6 = transform_and_flatten(x5, x4)
    x7 = fill(I, COLOR_TWO, x6)
    x8 = add(6, 6)
    x9 = as_tuple(8, x8)
    x10 = color_at_location(x7, x9)
    x11 = is_equal(x10, COLOR_TWO)
    x12 = initset(x9)
    x13 = add(x9, DOWN)
    x14 = insert(x13, x12)
    x15 = to_object(x14, x7)
    x16 = to_object(x14, I)
    x17 = condition_if_else(x11, x16, x15)
    O = paint_onto_grid(x7, x17)
    return O


def solve_4938f0c2(I):
    x1 = as_objects(I, True, True, True)
    x2 = of_color(I, COLOR_TWO)
    x3 = vertical_mirror(x2)
    x4 = get_height(x2)
    x5 = get_width(x2)
    x6 = to_vertical_vec(x4)
    x7 = to_horizontal_vec(x5)
    x8 = add(x7, ZERO_BY_TWO)
    x9 = add(x6, TWO_BY_ZERO)
    x10 = shift_by_vector(x3, x8)
    x11 = fill(I, COLOR_TWO, x10)
    x12 = of_color(x11, COLOR_TWO)
    x13 = horizontal_mirror(x12)
    x14 = shift_by_vector(x13, x9)
    x15 = fill(x11, COLOR_TWO, x14)
    x16 = size(x1)
    x17 = greater_than(x16, 4)
    O = condition_if_else(x17, I, x15)
    return O


def solve_834ec97d(I):
    x1 = as_indices(I)
    x2 = as_objects(I, True, False, True)
    x3 = get_first(x2)
    x4 = shift_by_vector(x3, DOWN)
    x5 = fill(I, COLOR_ZERO, x3)
    x6 = paint_onto_grid(x5, x4)
    x7 = uppermost(x4)
    x8 = leftmost(x4)
    x9 = subtract(x8, 10)
    x10 = add(x8, 10)
    x11 = interval(x9, x10, 2)
    x12 = fix_first_argument(greater_than, x7)
    x13 = compose(x12, get_first)
    x14 = fix_last_argument(contains, x11)
    x15 = compose(x14, get_last)
    x16 = keep_if_condition(x1, x13)
    x17 = keep_if_condition(x16, x15)
    O = fill(x6, COLOR_FOUR, x17)
    return O


def solve_846bdb03(I):
    x1 = as_objects(I, False, False, True)
    x2 = fix_last_argument(color_count, COLOR_FOUR)
    x3 = equals(x2, 0)
    x4 = extract_first_matching(x1, x3)
    x5 = remove(x4, x1)
    x6 = flatten(x5)
    x7 = smallest_subgrid_containing(x6, I)
    x8 = color_at_location(x7, DOWN)
    x9 = smallest_subgrid_containing(x4, I)
    x10 = left_half(x9)
    x11 = palette(x10)
    x12 = get_other(x11, COLOR_ZERO)
    x13 = is_equal(x8, x12)
    x14 = condition_if_else(x13, identity, vertical_mirror)
    x15 = x14(x4)
    x16 = shift_to_origin(x15)
    x17 = shift_by_vector(x16, UNITY)
    O = paint_onto_grid(x7, x17)
    return O


def solve_90f3ed37(I):
    x1 = as_objects(I, True, True, True)
    x2 = sort(x1, uppermost)
    x3 = get_first(x2)
    x4 = remove(x3, x2)
    x5 = shift_to_origin(x3)
    x6 = fix_first_argument(shift_by_vector, x5)
    x7 = compose(x6, upper_left_corner)
    x8 = interval(2, -1, -1)
    x9 = transform(to_horizontal_vec, x8)
    x10 = fix_last_argument(transform, x9)
    x11 = fix_first_argument(compose, size)
    x12 = fix_first_argument(fix_first_argument, intersection)
    x13 = compose(x11, x12)
    x14 = fix_first_argument(fix_first_argument, shift_by_vector)
    x15 = chain(x10, x14, x7)
    x16 = combine_two_function_results(argmax, x15, x13)
    x17 = transform_and_flatten(x16, x4)
    O = fill_background(I, COLOR_ONE, x17)
    return O


def solve_8403a5d5(I):
    x1 = as_indices(I)
    x2 = as_objects(I, True, False, True)
    x3 = get_first(x2)
    x4 = get_color(x3)
    x5 = leftmost(x3)
    x6 = interval(x5, 10, 2)
    x7 = fix_last_argument(contains, x6)
    x8 = compose(x7, get_last)
    x9 = keep_if_condition(x1, x8)
    x10 = increment(x5)
    x11 = add(x5, 3)
    x12 = interval(x10, 10, 4)
    x13 = interval(x11, 10, 4)
    x14 = fix_first_argument(as_tuple, 9)
    x15 = transform(to_horizontal_vec, x12)
    x16 = transform(x14, x13)
    x17 = fill(I, x4, x9)
    x18 = fill(x17, COLOR_FIVE, x15)
    O = fill(x18, COLOR_FIVE, x16)
    return O


def solve_91413438(I):
    x1 = color_count(I, COLOR_ZERO)
    x2 = subtract(9, x1)
    x3 = multiply(x1, 3)
    x4 = multiply(x3, x1)
    x5 = subtract(x4, 3)
    x6 = as_tuple(3, x5)
    x7 = create_grid(COLOR_ZERO, x6)
    x8 = horizontal_concat(I, x7)
    x9 = as_objects(x8, True, True, True)
    x10 = get_first(x9)
    x11 = fix_first_argument(shift_by_vector, x10)
    x12 = compose(x11, to_horizontal_vec)
    x13 = interval(0, x2, 1)
    x14 = fix_last_argument(multiply, 3)
    x15 = transform(x14, x13)
    x16 = transform_and_flatten(x12, x15)
    x17 = paint_onto_grid(x8, x16)
    x18 = horizontal_split(x17, x1)
    O = flatten(x18)
    return O


def solve_539a4f51(I):
    x1 = get_shape(I)
    x2 = color_at_location(I, ORIGIN)
    x3 = color_count(I, COLOR_ZERO)
    x4 = decrement(x1)
    x5 = is_positive(x3)
    x6 = condition_if_else(x5, x4, x1)
    x7 = crop(I, ORIGIN, x6)
    x8 = get_width(x7)
    x9 = as_tuple(1, x8)
    x10 = crop(x7, ORIGIN, x9)
    x11 = vertical_upscale(x10, x8)
    x12 = diagonal_mirror(x11)
    x13 = horizontal_concat(x7, x11)
    x14 = horizontal_concat(x12, x7)
    x15 = vertical_concat(x13, x14)
    x16 = as_object(x15)
    x17 = multiply(UNITY, 10)
    x18 = create_grid(x2, x17)
    O = paint_onto_grid(x18, x16)
    return O


def solve_5daaa586(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = fix_last_argument(bordering, I)
    x4 = compose(logical_not, x3)
    x5 = extract_first_matching(x2, x4)
    x6 = outbox(x5)
    x7 = smallest_subgrid_containing(x6, I)
    x8 = partition_only_foreground(x7)
    x9 = argmax(x8, size)
    x10 = get_color(x9)
    x11 = to_indices(x9)
    x12 = apply_function_on_cartesian_product(line_between, x11, x11)
    x13 = keep_if_condition_and_flatten(x12, is_vertical_line)
    x14 = keep_if_condition_and_flatten(x12, is_horizontal_line)
    x15 = size(x13)
    x16 = size(x14)
    x17 = greater_than(x15, x16)
    x18 = condition_if_else(x17, x13, x14)
    O = fill(x7, x10, x18)
    return O


def solve_3bdb4ada(I):
    x1 = as_objects(I, True, False, True)
    x2 = to_tuple(x1)
    x3 = compose(increment, upper_left_corner)
    x4 = compose(decrement, lower_right_corner)
    x5 = transform(x3, x2)
    x6 = transform(x4, x2)
    x7 = transform_both(line_between, x5, x6)
    x8 = transform(get_last, x5)
    x9 = compose(get_last, get_first)
    x10 = power(get_last, 2)
    x11 = combine_two_function_results(subtract, x9, x10)
    x12 = compose(is_even, x11)
    x13 = fix_first_argument(fix_last_argument, as_tuple)
    x14 = fix_first_argument(compose, x12)
    x15 = compose(x14, x13)
    x16 = combine_two_function_results(keep_if_condition, get_first, x15)
    x17 = pairwise(x7, x8)
    x18 = transform_and_flatten(x16, x17)
    O = fill(I, COLOR_ZERO, x18)
    return O


def solve_ec883f72(I):
    x1 = palette(I)
    x2 = as_objects(I, True, True, True)
    x3 = combine_two_function_results(multiply, get_height, get_width)
    x4 = argmax(x2, x3)
    x5 = get_color(x4)
    x6 = remove(COLOR_ZERO, x1)
    x7 = get_other(x6, x5)
    x8 = lower_right_corner(x4)
    x9 = lower_left_corner(x4)
    x10 = upper_right_corner(x4)
    x11 = upper_left_corner(x4)
    x12 = shoot(x8, UNITY)
    x13 = shoot(x9, DOWN_LEFT)
    x14 = shoot(x10, UP_RIGHT)
    x15 = shoot(x11, NEG_UNITY)
    x16 = union(x12, x13)
    x17 = union(x14, x15)
    x18 = union(x16, x17)
    O = fill_background(I, x7, x18)
    return O


def solve_2bee17df(I):
    x1 = get_height(I)
    x2 = rot90(I)
    x3 = subtract(x1, 2)
    x4 = interval(0, x1, 1)
    x5 = fix_last_argument(color_count, COLOR_ZERO)
    x6 = equals(x5, x3)
    x7 = fix_last_argument(vertical_split, x1)
    x8 = fix_first_argument(transform, x6)
    x9 = compose(x8, x7)
    x10 = x9(I)
    x11 = pairwise(x4, x10)
    x12 = keep_if_condition(x11, get_last)
    x13 = transform_and_flatten(horizontal_line, x12)
    x14 = x9(x2)
    x15 = pairwise(x14, x4)
    x16 = keep_if_condition(x15, get_first)
    x17 = transform_and_flatten(vertical_line, x16)
    #x18 = as_tuple(x13, x17)
    x18 = as_generic_tuple(x13, x17)  # mdda
    x19 = flatten(x18)
    O = fill_background(I, COLOR_THREE, x19)
    return O


def solve_e8dc4411(I):
    x1 = least_common_color(I)
    x2 = of_color(I, COLOR_ZERO)
    x3 = of_color(I, x1)
    x4 = position(x2, x3)
    x5 = combine_two_function_results(line_between, upper_left_corner, lower_right_corner)
    x6 = x5(x2)
    x7 = intersection(x2, x6)
    x8 = is_equal(x6, x7)
    x9 = combine_two_function_results(subtract, identity, crement)
    x10 = combine_two_function_results(add, identity, x9)
    x11 = condition_if_else(x8, identity, x10)
    x12 = get_shape(x2)
    x13 = multiply(x12, x4)
    x14 = transform(x11, x13)
    x15 = interval(1, 5, 1)
    x16 = fix_first_argument(multiply, x14)
    x17 = transform(x16, x15)
    x18 = fix_first_argument(shift_by_vector, x2)
    x19 = transform_and_flatten(x18, x17)
    O = fill(I, x1, x19)
    return O


def solve_e40b9e2f(I):
    x1 = as_objects(I, False, True, True)
    x2 = neighbors(ORIGIN)
    x3 = transform_and_flatten(neighbors, x2)
    x4 = get_first(x1)
    x5 = fix_first_argument(intersection, x4)
    # NIX.start
    #x6 = compose(horizontal_mirror, vertical_mirror)
    #x7 = x6(x4)
    #x8 = fix_first_argument(shift_by_vector, x7)
    #x9 = transform(x8, x3)
    #x10 = argmax(x9, x5)
    #x11 = paint_onto_grid(I, x10)
    #x12 = as_objects(x11, False, True, True)
    #x13 = get_first(x12)
    #x14 = compose(size, x5)
    # NIX.end
    x6 = compose(size, x5)
    x7 = compose(horizontal_mirror, vertical_mirror)
    x8 = x7(x4)
    x9 = fix_first_argument(shift_by_vector, x8)
    x10 = transform(x9, x3)
    x11 = argmax(x10, x6)
    x12 = paint_onto_grid(I, x11)
    x13 = as_objects(x12, False, True, True)
    x14 = get_first(x13)
    # same (https://github.com/michaelhodel/arc-dsl/pull/10/files)
    x15 = compose(vertical_mirror, diagonal_mirror)
    # small changes
    x16 = x15(x14)
    x17 = fix_first_argument(shift_by_vector, x16)
    x18 = transform(x17, x3)
    x19 = argmax(x18, x6)
    O = paint_onto_grid(x12, x19)
    return O


def solve_29623171(I):
    x1 = least_common_color(I)
    x2 = interval(0, 9, 4)
    x3 = cartesian_product(x2, x2)
    x4 = fix_last_argument(add, 3)
    x5 = fix_last_argument(interval, 1)
    x6 = combine_two_function_results(x5, identity, x4)
    x7 = compose(x6, get_first)
    x8 = compose(x6, get_last)
    x9 = combine_two_function_results(cartesian_product, x7, x8)
    x10 = fix_last_argument(color_count, x1)
    x11 = fix_last_argument(to_object, I)
    x12 = compose(x10, x11)
    x13 = transform(x9, x3)
    x14 = valmax(x13, x12)
    x15 = equals(x12, x14)
    x16 = compose(logical_not, x15)
    x17 = keep_if_condition_and_flatten(x13, x15)
    x18 = keep_if_condition_and_flatten(x13, x16)
    x19 = fill(I, x1, x17)
    O = fill(x19, COLOR_ZERO, x18)
    return O


def solve_a2fd1cf0(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_THREE)
    x3 = uppermost(x1)
    x4 = leftmost(x1)
    x5 = uppermost(x2)
    x6 = leftmost(x2)
    x7 = as_tuple(x3, x5)
    x8 = minimum(x7)
    x9 = maximum(x7)
    x10 = as_tuple(x8, x6)
    x11 = as_tuple(x9, x6)
    x12 = line_between(x10, x11)
    x13 = as_tuple(x4, x6)
    x14 = minimum(x13)
    x15 = maximum(x13)
    x16 = as_tuple(x3, x14)
    x17 = as_tuple(x3, x15)
    x18 = line_between(x16, x17)
    x19 = union(x12, x18)
    O = fill_background(I, COLOR_EIGHT, x19)
    return O


def solve_b0c4d837(I):
    x1 = of_color(I, COLOR_FIVE)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = get_height(x1)
    x4 = decrement(x3)
    x5 = get_height(x2)
    x6 = subtract(x4, x5)
    x7 = as_tuple(1, x6)
    x8 = create_grid(COLOR_EIGHT, x7)
    x9 = subtract(6, x6)
    x10 = as_tuple(1, x9)
    x11 = create_grid(COLOR_ZERO, x10)
    x12 = horizontal_concat(x8, x11)
    x13 = horizontal_split(x12, 2)
    x14 = get_first(x13)
    x15 = get_last(x13)
    x16 = vertical_mirror(x15)
    x17 = vertical_concat(x14, x16)
    x18 = as_tuple(1, 3)
    x19 = create_grid(COLOR_ZERO, x18)
    O = vertical_concat(x17, x19)
    return O


def solve_8731374e(I):
    x1 = as_objects(I, True, False, False)
    x2 = argmax(x1, size)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = get_height(x3)
    x5 = get_width(x3)
    x6 = vertical_split(x3, x4)
    x7 = fix_first_argument(greater_than, 4)
    x8 = compose(x7, count_colors)
    x9 = keep_if_condition(x6, x8)
    x10 = flatten(x9)
    x11 = rot90(x10)
    x12 = vertical_split(x11, x5)
    x13 = keep_if_condition(x12, x8)
    x14 = flatten(x13)
    x15 = rot270(x14)
    x16 = least_common_color(x15)
    x17 = of_color(x15, x16)
    x18 = combine_two_function_results(union, vertical_line, horizontal_line)
    x19 = transform_and_flatten(x18, x17)
    O = fill(x15, x16, x19)
    return O


def solve_272f95fa(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = transform(to_indices, x2)
    x4 = fix_last_argument(bordering, I)
    x5 = compose(logical_not, x4)
    x6 = extract_first_matching(x3, x5)
    x7 = remove(x6, x3)
    x8 = fix_first_argument(vertical_matching, x6)
    x9 = fix_first_argument(horizontal_matching, x6)
    x10 = keep_if_condition(x7, x8)
    x11 = keep_if_condition(x7, x9)
    x12 = argmin(x10, uppermost)
    x13 = argmax(x10, uppermost)
    x14 = argmin(x11, leftmost)
    x15 = argmax(x11, leftmost)
    x16 = fill(I, COLOR_SIX, x6)
    x17 = fill(x16, COLOR_TWO, x12)
    x18 = fill(x17, COLOR_ONE, x13)
    x19 = fill(x18, COLOR_FOUR, x14)
    O = fill(x19, COLOR_THREE, x15)
    return O


def solve_db93a21d(I):
    x1 = as_objects(I, True, True, True)
    x2 = of_color(I, COLOR_NINE)
    x3 = color_filter(x1, COLOR_NINE)
    x4 = fix_last_argument(shoot, DOWN)
    x5 = transform_and_flatten(x4, x2)
    x6 = fill_background(I, COLOR_ONE, x5)
    x7 = compose(halve, get_width)
    x8 = fix_last_argument(greater_than, 1)
    x9 = compose(x8, x7)
    x10 = equals(x7, 3)
    x11 = power(outbox, 2)
    x12 = power(outbox, 3)
    x13 = transform_and_flatten(outbox, x3)
    x14 = keep_if_condition(x3, x9)
    x15 = keep_if_condition(x3, x10)
    x16 = transform_and_flatten(x11, x14)
    x17 = transform_and_flatten(x12, x15)
    x18 = fill(x6, COLOR_THREE, x13)
    x19 = fill(x18, COLOR_THREE, x16)
    O = fill(x19, COLOR_THREE, x17)
    return O


def solve_53b68214(I):
    x1 = get_width(I)
    x2 = as_objects(I, True, True, True)
    x3 = get_first(x2)
    x4 = vertical_periodicity(x3)
    x5 = to_vertical_vec(x4)
    x6 = interval(0, 9, 1)
    x7 = fix_first_argument(multiply, x5)
    x8 = transform(x7, x6)
    x9 = fix_first_argument(shift_by_vector, x3)
    x10 = transform_and_flatten(x9, x8)
    x11 = as_tuple(x1, x1)
    x12 = is_portrait(x3)
    x13 = get_shape(x3)
    x14 = add(DOWN, x13)
    x15 = decrement(x14)
    x16 = shift_by_vector(x3, x15)
    x17 = condition_if_else(x12, x10, x16)
    x18 = create_grid(COLOR_ZERO, x11)
    x19 = paint_onto_grid(x18, x3)
    O = paint_onto_grid(x19, x17)
    return O


def solve_d6ad076f(I):
    x1 = as_objects(I, True, False, True)
    x2 = argmin(x1, size)
    x3 = argmax(x1, size)
    x4 = vertical_matching(x2, x3)
    x5 = condition_if_else(x4, DOWN, RIGHT)
    x6 = condition_if_else(x4, uppermost, leftmost)
    x7 = valmax(x1, x6)
    x8 = x6(x2)
    x9 = is_equal(x7, x8)
    x10 = condition_if_else(x9, -1, 1)
    x11 = multiply(x5, x10)
    x12 = inbox(x2)
    x13 = fix_last_argument(shoot, x11)
    x14 = transform_and_flatten(x13, x12)
    x15 = fill_background(I, COLOR_EIGHT, x14)
    x16 = as_objects(x15, True, False, True)
    x17 = color_filter(x16, COLOR_EIGHT)
    x18 = fix_last_argument(bordering, I)
    x19 = keep_if_condition_and_flatten(x17, x18)
    O = erase_patch(x15, x19)
    return O


def solve_6cdd2623(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = apply_function_on_cartesian_product(line_between, x2, x2)
    x4 = partition_only_foreground(I)
    x5 = flatten(x4)
    x6 = erase_patch(I, x5)
    x7 = combine_two_function_results(logical_or, is_horizontal_line, is_vertical_line)
    x8 = box(x5)
    x9 = fix_last_argument(difference, x8)
    x10 = chain(is_positive, size, x9)
    x11 = combine_two_function_results(logical_and, x7, x10)
    x12 = keep_if_condition_and_flatten(x3, x11)
    O = fill(x6, x1, x12)
    return O


def solve_a3df8b1e(I):
    x1 = get_shape(I)
    x2 = of_color(I, COLOR_ONE)
    x3 = get_first(x2)
    x4 = shoot(x3, UP_RIGHT)
    x5 = fill(I, COLOR_ONE, x4)
    x6 = of_color(x5, COLOR_ONE)
    x7 = upper_right_corner(x6)
    x8 = shoot(x7, NEG_UNITY)
    x9 = fill(x5, COLOR_ONE, x8)
    x10 = as_objects(x9, True, True, True)
    x11 = get_first(x10)
    x12 = smallest_subgrid_containing(x11, x9)
    x13 = get_shape(x12)
    x14 = subtract(x13, DOWN)
    x15 = crop(x12, DOWN, x14)
    x16 = vertical_concat(x15, x15)
    x17 = vertical_concat(x16, x16)
    x18 = vertical_concat(x17, x17)
    x19 = horizontal_mirror(x18)
    x20 = crop(x19, ORIGIN, x1)
    O = horizontal_mirror(x20)
    return O


def solve_8d510a79(I):
    x1 = of_color(I, COLOR_ONE)
    x2 = of_color(I, COLOR_TWO)
    x3 = of_color(I, COLOR_FIVE)
    x4 = uppermost(x3)
    x5 = chain(to_vertical_vec, decrement, double)
    x6 = fix_first_argument(greater_than, x4)
    x7 = compose(x6, get_first)
    x8 = chain(negate, x5, x7)
    x9 = combine_two_function_results(shoot, identity, x8)
    x10 = compose(x5, x7)
    x11 = combine_two_function_results(shoot, identity, x10)
    x12 = fix_first_argument(equals, x7)
    x13 = compose(x12, x7)
    x14 = combine_two_function_results(keep_if_condition, x11, x13)
    x15 = transform_and_flatten(x9, x1)
    x16 = transform_and_flatten(x14, x2)
    x17 = fill_background(I, COLOR_TWO, x16)
    O = fill(x17, COLOR_ONE, x15)
    return O


def solve_cdecee7f(I):
    x1 = as_objects(I, True, False, True)
    x2 = as_tuple(1, 3)
    x3 = size(x1)
    x4 = sort(x1, leftmost)
    x5 = transform(get_color, x4)
    x6 = fix_last_argument(create_grid, UNITY)
    x7 = transform(x6, x5)
    x8 = flatten(x7)
    x9 = diagonal_mirror(x8)
    x10 = subtract(9, x3)
    x11 = as_tuple(1, x10)
    x12 = create_grid(COLOR_ZERO, x11)
    x13 = horizontal_concat(x9, x12)
    x14 = horizontal_split(x13, 3)
    x15 = flatten(x14)
    x16 = crop(x15, ORIGIN, x2)
    x17 = crop(x15, DOWN, x2)
    x18 = crop(x15, TWO_BY_ZERO, x2)
    x19 = vertical_mirror(x17)
    x20 = vertical_concat(x16, x19)
    O = vertical_concat(x20, x18)
    return O


def solve_3345333e(I):
    x1 = least_common_color(I)
    x2 = of_color(I, x1)
    x3 = erase_patch(I, x2)
    x4 = least_common_color(x3)
    x5 = of_color(x3, x4)
    x6 = neighbors(ORIGIN)
    x7 = transform_and_flatten(neighbors, x6)
    x8 = vertical_mirror(x5)
    x9 = fix_first_argument(shift_by_vector, x8)
    x10 = transform(x9, x7)
    x11 = fix_last_argument(intersection, x5)
    x12 = compose(size, x11)
    x13 = argmax(x10, x12)
    O = fill(x3, x4, x13)
    return O


def solve_b190f7f5(I):
    x1 = is_portrait(I)
    x2 = condition_if_else(x1, vertical_split, horizontal_split)
    x3 = x2(I, 2)
    x4 = argmin(x3, count_colors)
    x5 = argmax(x3, count_colors)
    x6 = get_width(x5)
    x7 = fix_last_argument(repeat, x6)
    x8 = chain(diagonal_mirror, flatten, x7)
    x9 = upscale(x5, x6)
    x10 = x8(x4)
    x11 = x8(x10)
    x12 = of_color(x11, COLOR_ZERO)
    O = fill(x9, COLOR_ZERO, x12)
    return O


def solve_caa06a1f(I):   # Super-mean, since the test case is more complicated than the training ones - need to guess intent
    x1 = as_object(I)
    x2 = get_shape(I)
    x3 = decrement(x2)
    x4 = color_at_location(I, x3)
    x5 = double(x2)
    x6 = create_grid(x4, x5)
    x7 = paint_onto_grid(x6, x1)
    x8 = as_objects(x7, False, False, True)
    x9 = get_first(x8)
    x10 = shift_by_vector(x9, LEFT)
    x11 = vertical_periodicity(x10)
    x12 = horizontal_periodicity(x10)
    x13 = neighbors(ORIGIN)
    x14 = fix_first_argument(transform_and_flatten, neighbors)
    x15 = power(x14, 2)
    x16 = x15(x13)
    x17 = as_tuple(x11, x12)
    x18 = fix_first_argument(multiply, x17)
    x19 = transform(x18, x16)
    x20 = fix_first_argument(shift_by_vector, x10)
    x21 = transform_and_flatten(x20, x19)
    O = paint_onto_grid(I, x21)
    return O


def solve_e21d9049(I):
    x1 = as_indices(I)
    x2 = least_common_color(I)
    x3 = as_objects(I, True, False, True)
    x4 = of_color(I, x2)
    x5 = flatten(x3)
    x6 = get_shape(x5)
    x7 = neighbors(ORIGIN)
    x8 = fix_first_argument(transform_and_flatten, neighbors)
    x9 = power(x8, 2)
    x10 = x9(x7)
    x11 = fix_first_argument(multiply, x6)
    x12 = fix_first_argument(shift_by_vector, x5)
    x13 = transform(x11, x10)
    x14 = transform_and_flatten(x12, x13)
    x15 = fix_first_argument(horizontal_matching, x4)
    x16 = fix_first_argument(vertical_matching, x4)
    x17 = combine_two_function_results(logical_or, x15, x16)
    x18 = compose(x17, initset)
    x19 = paint_onto_grid(I, x14)
    x20 = keep_if_condition(x1, x18)
    x21 = difference(x1, x20)
    O = erase_patch(x19, x21)
    return O


def solve_d89b689b(I):
    x1 = as_objects(I, True, False, True)
    x2 = of_color(I, COLOR_EIGHT)
    x3 = size_filter(x1, 1)
    x4 = transform(initset, x2)
    x5 = fix_first_argument(argmin, x4)
    x6 = fix_first_argument(fix_last_argument, manhattan_distance)
    x7 = compose(x5, x6)
    x8 = combine_two_function_results(recolor, get_color, x7)
    x9 = transform_and_flatten(x8, x3)
    x10 = flatten(x3)
    x11 = erase_patch(I, x10)
    O = paint_onto_grid(x11, x9)
    return O


def solve_746b3537(I):
    x1 = chain(size, remove_duplicates, get_first)
    x2 = x1(I)
    x3 = is_equal(x2, 1)
    x4 = condition_if_else(x3, diagonal_mirror, identity)
    x5 = x4(I)
    x6 = as_objects(x5, True, False, False)
    x7 = sort(x6, leftmost)
    x8 = transform(get_color, x7)
    x9 = repeat(x8, 1)
    O = x4(x9)
    return O


def solve_63613498(I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = of_color(x1, COLOR_ZERO)
    x3 = as_indices(x1)
    x4 = difference(x3, x2)
    x5 = shift_to_origin(x4)
    x6 = as_objects(I, True, False, True)
    x7 = compose(to_indices, shift_to_origin)
    x8 = equals(x7, x5)
    x9 = keep_if_condition_and_flatten(x6, x8)
    x10 = fill(I, COLOR_FIVE, x9)
    x11 = as_object(x1)
    O = paint_onto_grid(x10, x11)
    return O


def solve_06df4c85(I):
    x1 = partition(I)
    x2 = most_common_color(I)
    x3 = of_color(I, x2)
    x4 = color_filter(x1, COLOR_ZERO)
    x5 = argmax(x1, size)
    x6 = difference(x1, x4)
    x7 = remove(x5, x6)
    x8 = flatten(x7)
    x9 = cartesian_product(x8, x8)
    x10 = power(get_first, 2)
    x11 = compose(get_first, get_last)
    x12 = combine_two_function_results(is_equal, x10, x11)
    x13 = keep_if_condition(x9, x12)
    x14 = compose(get_last, get_first)
    x15 = power(get_last, 2)
    x16 = combine_two_function_results(line_between, x14, x15)
    x17 = combine_two_function_results(recolor, get_color, x16)
    x18 = transform(x17, x13)
    x19 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x20 = keep_if_condition_and_flatten(x18, x19)
    x21 = paint_onto_grid(I, x20)
    O = fill(x21, x2, x3)
    return O


def solve_f9012d9b(I):
    x1 = as_objects(I, True, False, False)
    x2 = of_color(I, COLOR_ZERO)
    x3 = fix_first_argument(contains, COLOR_ZERO)
    x4 = chain(logical_not, x3, palette)
    x5 = keep_if_condition_and_flatten(x1, x4)
    x6 = vertical_split(I, 2)
    x7 = horizontal_split(I, 2)
    x8 = extract_first_matching(x6, x4)
    x9 = extract_first_matching(x7, x4)
    x10 = as_object(x8)
    x11 = as_object(x9)
    x12 = vertical_periodicity(x10)
    x13 = horizontal_periodicity(x11)
    x14 = neighbors(ORIGIN)
    x15 = transform_and_flatten(neighbors, x14)
    x16 = as_tuple(x12, x13)
    x17 = fix_last_argument(multiply, x16)
    x18 = transform(x17, x15)
    x19 = fix_first_argument(shift_by_vector, x5)
    x20 = transform_and_flatten(x19, x18)
    x21 = paint_onto_grid(I, x20)
    O = smallest_subgrid_containing(x2, x21)
    return O


def solve_4522001f(I):
    x1 = as_objects(I, False, False, True)
    x2 = get_first(x1)
    x3 = to_indices(x2)
    x4 = contains(ZERO_BY_TWO, x3)
    x5 = contains(TWO_BY_TWO, x3)
    x6 = contains(TWO_BY_ZERO, x3)
    x7 = as_tuple(9, 9)
    x8 = create_grid(COLOR_ZERO, x7)
    #x9 = as_tuple(COLOR_THREE, ORIGIN)
    x9 = make_cell(COLOR_THREE, ORIGIN)  # mdda
    x10 = initset(x9)
    x11 = upscale(x10, 2)
    x12 = upscale(x11, 2)
    x13 = get_shape(x12)
    x14 = shift_by_vector(x12, x13)
    x15 = union(x12, x14)
    x16 = paint_onto_grid(x8, x15)
    x17 = rot90(x16)
    x18 = rot180(x16)
    x19 = rot270(x16)
    x20 = condition_if_else(x4, x17, x16)
    x21 = condition_if_else(x5, x18, x20)
    O = condition_if_else(x6, x19, x21)
    return O


def solve_a48eeaf7(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = outbox(x1)
    x3 = transform(initset, x2)
    x4 = of_color(I, COLOR_FIVE)
    x5 = fix_first_argument(argmin, x3)
    x6 = fix_first_argument(fix_first_argument, manhattan_distance)
    x7 = compose(x6, initset)
    x8 = compose(x5, x7)
    x9 = transform_and_flatten(x8, x4)
    x10 = erase_patch(I, x4)
    O = fill(x10, COLOR_FIVE, x9)
    return O


def solve_eb5a1d5d(I):
    x1 = compose(diagonal_mirror, remove_duplicates)
    x2 = x1(I)
    x3 = x1(x2)
    x4 = combine_two_function_results(remove, get_last, identity)
    x5 = compose(horizontal_mirror, x4)
    x6 = combine_two_function_results(vertical_concat, identity, x5)
    x7 = x6(x3)
    x8 = diagonal_mirror(x7)
    O = x6(x8)
    return O


def solve_e179c5f4(I):
    x1 = get_height(I)
    x2 = of_color(I, COLOR_ONE)
    x3 = get_first(x2)
    x4 = shoot(x3, UP_RIGHT)
    x5 = fill(I, COLOR_ONE, x4)
    x6 = of_color(x5, COLOR_ONE)
    x7 = upper_right_corner(x6)
    x8 = shoot(x7, NEG_UNITY)
    x9 = fill(x5, COLOR_ONE, x8)
    x10 = of_color(x9, COLOR_ONE)
    x11 = smallest_subgrid_containing(x10, x9)
    x12 = get_height(x11)
    x13 = get_width(x11)
    x14 = decrement(x12)
    x15 = as_tuple(x14, x13)
    x16 = upper_left_corner(x10)
    x17 = crop(x9, x16, x15)
    x18 = repeat(x17, 9)
    x19 = flatten(x18)
    x20 = as_tuple(x1, x13)
    x21 = crop(x19, ORIGIN, x20)
    x22 = horizontal_mirror(x21)
    O = replace(x22, COLOR_ZERO, COLOR_EIGHT)
    return O


def solve_228f6490(I):
    x1 = as_objects(I, True, False, False)
    x2 = color_filter(x1, COLOR_ZERO)
    x3 = fix_last_argument(bordering, I)
    x4 = compose(logical_not, x3)
    x5 = keep_if_condition(x2, x4)
    x6 = get_first(x5)
    x7 = get_last(x5)
    x8 = difference(x1, x2) # This is a list of all the non-interior objects
    x8_object_tuple = to_tuple(x8)  # Make a list that we can transform
    x8_object_colors_tuple = transform(get_color, x8_object_tuple)  # Find colour of each object
    x8_noise_color = most_common(x8_object_colors_tuple)  # Find most common colour of objects
    x8_noise_objects = color_filter(x1, x8_noise_color)
    x8_filtered = difference(x8, x8_noise_objects)
    x9 = compose(shift_to_origin, to_indices)
    x10 = x9(x6)
    x11 = x9(x7)
    x12 = equals(x9, x10)
    x13 = equals(x9, x11)
    #x14 = extract_first_matching(x8, x12)
    #x15 = extract_first_matching(x8, x13)
    x14 = extract_first_matching(x8_filtered, x12)  # mdda : Update since first training example has pair of points
    x15 = extract_first_matching(x8_filtered, x13)  # mdda : Update since first training example has pair of points
    x16 = upper_left_corner(x6)
    x17 = upper_left_corner(x7)
    x18 = upper_left_corner(x14)
    x19 = upper_left_corner(x15)
    x20 = subtract(x16, x18)
    x21 = subtract(x17, x19)
    x22 = move_object(I, x14, x20)
    O = move_object(x22, x15, x21)
    return O


def solve_995c5fa3(I):
    x1 = horizontal_split(I, 3)
    x2 = as_tuple(2, 1)
    x3 = fix_last_argument(of_color, COLOR_ZERO)      # Look for black pieces
    x4 = compose(upper_left_corner, x3)
    x5 = compose(size, x3)
    x6 = equals(x5, 0)                   # No black pieces -> COLOR_TWO
    x7 = equals(x4, UNITY)               # black at 1,1    -> COLOR_EIGHT
    x8 = equals(x4, DOWN)                # black at 1,0    -> COLOR_THREE
    x9 = equals(x4, x2)                  # black at 2,1    -> COLOR_FOUR

    #x10 = fix_last_argument(multiply, 3)      # 3x mdda : These lines are computing COLOR integers, rather than look-up : NAUGHTY
    #x11 = power(double, 2)        # 4x

    #x12 = compose(double, x6)     # 2x   = 2
    #x13 = chain(x11, double, x7)  # 2x4x = 8
    #x14 = compose(x10, x8)        # 3x   = 3
    #x15 = compose(x11, x9)        # 4x   = 4

    # Instead, let's compute a simple index since we can add integers, only one of which is non-zero
    x10a = fix_last_argument(multiply, 0)
    x10b = fix_last_argument(multiply, 1)
    x10c = fix_last_argument(multiply, 2)
    x10d = fix_last_argument(multiply, 3)

    x12 = compose(x10a, x6)
    x13 = compose(x10b, x7)
    x14 = compose(x10c, x8)
    x15 = compose(x10d, x9)

    x16 = combine_two_function_results(add, x12, x13)
    x17 = combine_two_function_results(add, x14, x15)
    x18 = combine_two_function_results(add, x16, x17)

    # mdda : Now we have an index that we can use to look into a tuple...

    c12 = as_generic_tuple(COLOR_TWO, COLOR_EIGHT)
    c34 = as_generic_tuple(COLOR_THREE, COLOR_FOUR)
    c4 = union(c12, c34)
    cgrid = as_generic_tuple(c4, c4)  # Two row grid - so was can do color_at_location
    
    #x18loc = as_tuple(x18, 0)
    #x18post = color_at_location(cgrid, x18loc)
    x18loc = fix_first_argument(as_tuple, 0)
    x18post = fix_first_argument(color_at_location, cgrid)
    x18lookup = chain(x18post, x18loc, x18)

    x19 = fix_last_argument(create_grid, UNITY)
    x20 = compose(x19, x18lookup)  # mdda : refer to table look-up
    x21 = transform(x20, x1)
    x22 = flatten(x21)
    O = horizontal_upscale(x22, 3)
    return O


def solve_d06dbe63(I):
    x1 = of_color(I, COLOR_EIGHT)
    x2 = center(x1)
    x3 = line_between(ORIGIN, DOWN)
    x4 = line_between(ORIGIN, ZERO_BY_TWO)
    x5 = union(x3, x4)
    x6 = subtract(x2, TWO_BY_ZERO)
    x7 = shift_by_vector(x5, x6)
    x8 = as_tuple(-2, 2)
    x9 = interval(0, 5, 1)
    x10 = fix_first_argument(multiply, x8)
    x11 = transform(x10, x9)
    x12 = fix_first_argument(shift_by_vector, x7)
    x13 = transform_and_flatten(x12, x11)
    x14 = fill(I, COLOR_FIVE, x13)
    x15 = rot180(x14)
    x16 = of_color(x15, COLOR_EIGHT)
    x17 = center(x16)
    x18 = subtract(x17, x6)
    x19 = shift_by_vector(x13, x18)
    x20 = to_vertical_vec(NEG_TWO)
    x21 = shift_by_vector(x19, x20)
    x22 = fill(x15, COLOR_FIVE, x21)
    O = rot180(x22)
    return O


def solve_36fdfd69(I):
    x1 = upscale(I, 2)
    x2 = as_objects(x1, True, True, True)
    x3 = color_filter(x2, COLOR_TWO)
    x4 = combine_two_function_results(manhattan_distance, get_first, get_last)
    x5 = fix_first_argument(greater_than, 5)
    x6 = compose(x5, x4)
    x7 = cartesian_product(x3, x3)
    x8 = keep_if_condition(x7, x6)
    x9 = transform(flatten, x8)
    x10 = transform_and_flatten(bounding_box_delta, x9)
    x11 = fill(x1, COLOR_FOUR, x10)
    x12 = flatten(x3)
    x13 = paint_onto_grid(x11, x12)
    O = downscale(x13, 2)
    return O


def solve_0a938d79(I):
    x1 = is_portrait(I)
    x2 = condition_if_else(x1, diagonal_mirror, identity)
    x3 = x2(I)
    x4 = partition_only_foreground(x3)
    x5 = flatten(x4)
    x6 = chain(double, decrement, get_width)
    x7 = x6(x5)
    x8 = compose(vertical_line, to_horizontal_vec)
    x9 = fix_first_argument(transform_and_flatten, x8)
    x10 = fix_last_argument(interval, x7)
    x11 = get_width(x3)
    x12 = fix_last_argument(x10, x11)
    x13 = chain(x9, x12, leftmost)
    x14 = combine_two_function_results(recolor, get_color, x13)
    x15 = transform_and_flatten(x14, x4)
    x16 = paint_onto_grid(x3, x15)
    O = x2(x16)
    return O


def solve_045e512c(I):
    x1 = as_objects(I, True, True, True)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = fix_first_argument(shift_by_vector, x2)
    x5 = fix_first_argument(transform_and_flatten, x4)
    x6 = double(10)
    x7 = interval(4, x6, 4)
    x8 = fix_last_argument(transform, x7)
    x9 = fix_first_argument(position, x2)
    x10 = fix_first_argument(fix_last_argument, multiply)
    x11 = chain(x8, x10, x9)
    x12 = compose(x5, x11)
    x13 = combine_two_function_results(recolor, get_color, x12)
    x14 = transform_and_flatten(x13, x3)
    O = paint_onto_grid(I, x14)
    return O


def solve_82819916(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = shift_to_origin(x2)
    x5 = compose(get_last, get_last)
    x6 = fix_last_argument(argmin, x5)
    x7 = compose(get_first, x6)
    x8 = combine_two_function_results(get_other, palette, x7)
    x9 = x7(x4)
    x10 = equals(get_first, x9)
    x11 = keep_if_condition(x4, x10)
    x12 = difference(x4, x11)
    x13 = compose(to_vertical_vec, uppermost)
    x14 = fix_first_argument(shift_by_vector, x11)
    x15 = fix_first_argument(shift_by_vector, x12)
    x16 = compose(x14, x13)
    x17 = compose(x15, x13)
    x18 = combine_two_function_results(recolor, x7, x16)
    x19 = combine_two_function_results(recolor, x8, x17)
    x20 = combine_two_function_results(union, x18, x19)
    x21 = transform_and_flatten(x20, x3)
    O = paint_onto_grid(I, x21)
    return O


def solve_99fa7670(I):
    x1 = get_shape(I)
    x2 = as_objects(I, True, False, True)
    x3 = fix_last_argument(shoot, RIGHT)
    x4 = compose(x3, center)
    x5 = combine_two_function_results(recolor, get_color, x4)
    x6 = transform_and_flatten(x5, x2)
    x7 = paint_onto_grid(I, x6)
    x8 = add(x1, DOWN_LEFT)
    x9 = initset(x8)
    x10 = recolor(COLOR_ZERO, x9)
    x11 = as_objects(x7, True, False, True)
    x12 = insert(x10, x11)
    x13 = sort(x12, uppermost)
    x14 = get_first(x13)
    x15 = remove(x10, x13)
    x16 = remove(x14, x13)
    x17 = compose(lower_right_corner, get_first)
    x18 = compose(lower_right_corner, get_last)
    x19 = combine_two_function_results(line_between, x17, x18)
    x20 = compose(get_color, get_first)
    x21 = combine_two_function_results(recolor, x20, x19)
    x22 = pairwise(x15, x16)
    x23 = transform_and_flatten(x21, x22)
    O = paint_onto_grid_background(x7, x23)
    return O


def solve_72322fa7(I):
    x1 = as_objects(I, False, True, True)
    x2 = equals(count_colors, 1)
    x3 = keep_if_condition(x1, x2)
    x4 = difference(x1, x3)
    x5 = fix_first_argument(equals, get_first)
    x6 = compose(x5, most_common_color)
    x7 = combine_two_function_results(keep_if_condition, identity, x6)
    x8 = combine_two_function_results(difference, identity, x7)
    x9 = fix_first_argument(occurrences, I)
    x10 = compose(x9, x7)
    x11 = compose(x9, x8)
    x12 = compose(upper_left_corner, x8)
    x13 = combine_two_function_results(subtract, upper_left_corner, x12)
    x14 = fix_first_argument(fix_last_argument, add)
    x15 = compose(x14, x13)
    x16 = combine_two_function_results(transform, x15, x11)
    x17 = fix_first_argument(fix_first_argument, shift_by_vector)
    x18 = compose(x17, shift_to_origin)
    x19 = combine_two_function_results(transform_and_flatten, x18, x10)
    x20 = combine_two_function_results(transform_and_flatten, x18, x16)
    x21 = transform_and_flatten(x19, x4)
    x22 = transform_and_flatten(x20, x4)
    x23 = paint_onto_grid(I, x21)
    O = paint_onto_grid(x23, x22)
    return O


def solve_855e0971(I):
    #x1 = rot90(I)  # Unused?
    x2 = solid_color_strips_in_grid(I)
    x3 = keep_if_condition(x2, is_horizontal_line)
    x4 = size(x3)
    x6 = is_positive(x4)
    x7 = condition_if_else(x6, identity, diagonal_mirror)
    x8 = x7(I)
    x9 = fix_last_argument(smallest_subgrid_containing, x8)
    x10 = equals(get_color, COLOR_ZERO)
    x11 = compose(logical_not, x10)
    x12 = partition(x8)
    x13 = keep_if_condition(x12, x11)
    x14 = fix_last_argument(of_color, COLOR_ZERO)
    x15 = fix_first_argument(transform_and_flatten, vertical_line)
    x16 = chain(x15, x14, x9)
    x17 = combine_two_function_results(shift_by_vector, x16, upper_left_corner)
    x18 = combine_two_function_results(intersection, to_indices, x17)
    x19 = transform_and_flatten(x18, x13)
    x20 = fill(x8, COLOR_ZERO, x19)
    O = x7(x20)
    return O


def solve_a78176bb(I):
    x1 = palette(I)
    x2 = as_objects(I, True, False, True)
    x3 = remove(COLOR_ZERO, x1)
    x4 = get_other(x3, COLOR_FIVE)
    x5 = color_filter(x2, COLOR_FIVE)
    x6 = fix_first_argument(color_at_location, I)
    x7 = compose(x6, upper_right_corner)
    x8 = equals(x7, COLOR_FIVE)
    x9 = keep_if_condition(x5, x8)
    x10 = difference(x5, x9)
    x11 = transform(upper_right_corner, x9)
    x12 = transform(lower_left_corner, x10)
    x13 = fix_last_argument(add, UP_RIGHT)
    x14 = fix_last_argument(add, DOWN_LEFT)
    x15 = transform(x13, x11)
    x16 = transform(x14, x12)
    x17 = fix_last_argument(shoot, UNITY)
    x18 = fix_last_argument(shoot, NEG_UNITY)
    x19 = combine_two_function_results(union, x17, x18)
    x20 = transform_and_flatten(x19, x15)
    x21 = transform_and_flatten(x19, x16)
    x22 = union(x20, x21)
    x23 = fill(I, x4, x22)
    O = replace(x23, COLOR_FIVE, COLOR_ZERO)
    return O


def solve_952a094c(I):
    x1 = as_objects(I, True, False, True)
    x2 = size_filter(x1, 1)
    x3 = argmax(x1, size)
    x4 = outbox(x3)
    x5 = corner_indices(x4)
    x6 = fix_first_argument(fix_last_argument, manhattan_distance)
    x7 = fix_first_argument(argmax, x2)
    x8 = chain(x7, x6, initset)
    x9 = compose(get_color, x8)
    x10 = combine_two_function_results(as_tuple, x9, identity)
    x11 = transform(x10, x5)
    x12 = flatten(x2)
    x13 = erase_patch(I, x12)
    O = paint_onto_grid(x13, x11)
    return O


def solve_6d58a25d(I):
    x1 = as_objects(I, True, True, True)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = flatten(x3)
    x5 = get_color(x4)
    x6 = uppermost(x2)
    x7 = fix_last_argument(greater_than, x6)
    x8 = compose(x7, uppermost)
    x9 = fix_last_argument(vertical_matching, x2)
    x10 = combine_two_function_results(logical_and, x9, x8)
    x11 = keep_if_condition(x3, x10)
    x12 = increment(x6)
    x13 = fix_last_argument(greater_than, x12)
    x14 = compose(x13, get_first)
    x15 = fix_last_argument(keep_if_condition, x14)
    x16 = chain(x15, vertical_line, center)
    x17 = transform_and_flatten(x16, x11)
    O = fill_background(I, x5, x17)
    return O


def solve_6aa20dc0(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmax(x1, count_colors)
    x3 = shift_to_origin(x2)
    x4 = fix_first_argument(equals, get_first)
    x5 = compose(x4, most_common_color)
    x6 = combine_two_function_results(keep_if_condition, identity, x5)
    x7 = combine_two_function_results(difference, identity, x6)
    x8 = fix_first_argument(fix_last_argument, upscale)
    x9 = interval(1, 4, 1)
    x10 = transform(x8, x9)
    x11 = initset(identity)
    x12 = insert(vertical_mirror, x11)
    x13 = insert(horizontal_mirror, x12)
    x14 = insert(counterdiagonal_mirror, x13)
    x15 = insert(diagonal_mirror, x14)
    x16 = combine_two_function_results(compose, get_first, get_last)
    x17 = fix_first_argument(occurrences, I)
    x18 = fix_first_argument(fix_first_argument, shift_by_vector)
    x19 = compose(x17, x7)
    x20 = cartesian_product(x15, x10)
    x21 = transform(x16, x20)
    x22 = apply_each_function(x21, x3)
    x23 = combine_two_function_results(transform_and_flatten, x18, x19)
    x24 = transform_and_flatten(x23, x22)
    O = paint_onto_grid(I, x24)
    return O


def solve_e6721834(I):
    x1 = is_portrait(I)
    x2 = condition_if_else(x1, vertical_split, horizontal_split)
    x3 = x2(I, 2)
    x4 = sort(x3, count_colors)
    x5 = get_first(x4)
    x6 = get_last(x4)
    x7 = as_objects(x6, False, False, True)
    x8 = flatten(x7)
    x9 = most_common_color(x8)
    x10 = equals(get_first, x9)
    x11 = compose(logical_not, x10)
    x12 = fix_last_argument(keep_if_condition, x11)
    x13 = fix_first_argument(occurrences, x5)
    x14 = compose(x13, x12)
    x15 = chain(is_positive, size, x14)
    x16 = keep_if_condition(x7, x15)
    x17 = chain(get_first, x13, x12)
    x18 = compose(upper_left_corner, x12)
    x19 = combine_two_function_results(subtract, x17, x18)
    x20 = combine_two_function_results(shift_by_vector, identity, x19)
    x21 = transform(x20, x16)
    x22 = compose(decrement, get_width)
    x23 = chain(is_positive, decrement, x22)
    x24 = keep_if_condition_and_flatten(x21, x23)
    O = paint_onto_grid(x5, x24)
    return O


def solve_447fd412(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmax(x1, count_colors)
    x3 = shift_to_origin(x2)
    x4 = fix_first_argument(equals, get_first)
    x5 = compose(x4, most_common_color)
    x6 = combine_two_function_results(keep_if_condition, identity, x5)
    x7 = combine_two_function_results(difference, identity, x6)
    x8 = fix_first_argument(fix_last_argument, upscale)
    x9 = interval(1, 4, 1)
    x10 = transform(x8, x9)
    x11 = fix_first_argument(recolor, COLOR_ZERO)
    x12 = compose(x11, outbox)
    x13 = combine_two_function_results(union, identity, x12)
    x14 = fix_first_argument(occurrences, I)
    x15 = fix_first_argument(fix_last_argument, subtract)
    x16 = fix_first_argument(transform, increment)
    x17 = fix_first_argument(fix_first_argument, shift_by_vector)
    x18 = chain(x15, upper_left_corner, x7)
    x19 = chain(x14, x13, x7)
    x20 = combine_two_function_results(transform, x18, x19)
    x21 = compose(x16, x20)
    x22 = combine_two_function_results(transform_and_flatten, x17, x21)
    x23 = apply_each_function(x10, x3)
    x24 = transform_and_flatten(x22, x23)
    O = paint_onto_grid(I, x24)
    return O


def solve_2bcee788(I):
    x1 = most_common_color(I)
    x2 = as_objects(I, True, False, True)
    x3 = replace(I, x1, COLOR_THREE)
    x4 = argmax(x2, size)
    x5 = argmin(x2, size)
    x6 = position(x4, x5)
    x7 = get_first(x6)
    x8 = get_last(x6)
    x9 = smallest_subgrid_containing(x4, x3)
    x10 = is_horizontal_line(x5)
    x11 = horizontal_mirror(x9)
    x12 = vertical_mirror(x9)
    x13 = condition_if_else(x10, x11, x12)
    x14 = condition_if_else(x10, x7, 0)
    x15 = condition_if_else(x10, 0, x8)
    x16 = as_object(x13)
    x17 = equals(get_first, COLOR_THREE)
    x18 = compose(logical_not, x17)
    x19 = keep_if_condition(x16, x18)
    x20 = upper_left_corner(x4)
    x21 = get_shape(x4)
    x22 = as_tuple(x14, x15)
    x23 = multiply(x21, x22)
    x24 = add(x20, x23)
    x25 = shift_by_vector(x19, x24)
    O = paint_onto_grid(x3, x25)
    return O


def solve_776ffc46(I):
    x1 = as_objects(I, True, False, True)
    x2 = color_filter(x1, COLOR_FIVE)
    x3 = combine_two_function_results(is_equal, to_indices, box)
    x4 = extract_first_matching(x2, x3)
    x5 = inbox(x4)
    x6 = smallest_subgrid_containing(x5, I)
    x7 = as_object(x6)
    x8 = equals(get_first, COLOR_ZERO)
    x9 = compose(logical_not, x8)
    x10 = keep_if_condition(x7, x9)
    x11 = shift_to_origin(x10)
    x12 = to_indices(x11)
    x13 = compose(to_indices, shift_to_origin)
    x14 = equals(x13, x12)
    x15 = keep_if_condition_and_flatten(x1, x14)
    x16 = get_color(x11)
    O = fill(I, x16, x15)
    return O


def solve_f35d900a(I):
    x1 = as_objects(I, True, False, True)
    x2 = palette(I)
    x3 = remove(COLOR_ZERO, x2)
    x4 = fix_first_argument(get_other, x3)
    x5 = compose(x4, get_color)
    x6 = combine_two_function_results(recolor, x5, outbox)
    x7 = transform_and_flatten(x6, x1)
    x8 = transform_and_flatten(to_indices, x1)
    x9 = box(x8)
    x10 = difference(x9, x8)
    x11 = fix_first_argument(argmin, x8)
    x12 = fix_last_argument(compose, initset)
    x13 = fix_first_argument(fix_last_argument, manhattan_distance)
    x14 = chain(x12, x13, initset)
    x15 = chain(initset, x11, x14)
    x16 = combine_two_function_results(manhattan_distance, initset, x15)
    x17 = compose(is_even, x16)
    x18 = keep_if_condition(x10, x17)
    x19 = paint_onto_grid(I, x7)
    O = fill(x19, COLOR_FIVE, x18)
    return O


def solve_0dfd9992(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = partition(I)
    x4 = color_filter(x3, COLOR_ZERO)
    x5 = difference(x3, x4)
    x6 = flatten(x5)
    x7 = as_tuple(x1, 1)
    x8 = as_tuple(1, x2)
    x9 = decrement(x1)
    x10 = decrement(x2)
    x11 = to_vertical_vec(x10)
    x12 = to_horizontal_vec(x9)
    x13 = crop(I, x11, x8)
    x14 = crop(I, x12, x7)
    x15 = as_object(x14)
    x16 = as_object(x13)
    x17 = vertical_periodicity(x15)
    x18 = horizontal_periodicity(x16)
    x19 = as_tuple(x17, x18)
    x20 = fix_first_argument(multiply, x19)
    x21 = neighbors(ORIGIN)
    x22 = transform_and_flatten(neighbors, x21)
    x23 = transform(x20, x22)
    x24 = fix_first_argument(shift_by_vector, x6)
    x25 = transform_and_flatten(x24, x23)
    O = paint_onto_grid(I, x25)
    return O


def solve_29ec7d0e(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = partition(I)
    x4 = color_filter(x3, COLOR_ZERO)
    x5 = difference(x3, x4)
    x6 = flatten(x5)
    x7 = as_tuple(x1, 1)
    x8 = as_tuple(1, x2)
    x9 = decrement(x1)
    x10 = decrement(x2)
    x11 = to_vertical_vec(x10)
    x12 = to_horizontal_vec(x9)
    x13 = crop(I, x11, x8)
    x14 = crop(I, x12, x7)
    x15 = as_object(x14)
    x16 = as_object(x13)
    x17 = vertical_periodicity(x15)
    x18 = horizontal_periodicity(x16)
    x19 = as_tuple(x17, x18)
    x20 = fix_first_argument(multiply, x19)
    x21 = neighbors(ORIGIN)
    x22 = transform_and_flatten(neighbors, x21)
    x23 = transform(x20, x22)
    x24 = fix_first_argument(shift_by_vector, x6)
    x25 = transform_and_flatten(x24, x23)
    O = paint_onto_grid(I, x25)
    return O


def solve_36d67576(I):
    x1 = as_objects(I, False, False, True)
    x2 = argmax(x1, count_colors)
    x3 = as_tuple(COLOR_TWO, COLOR_FOUR)
    x4 = fix_last_argument(contains, x3)
    x5 = compose(x4, get_first)
    x6 = fix_last_argument(keep_if_condition, x5)
    x7 = fix_first_argument(fix_last_argument, subtract)
    x8 = fix_first_argument(occurrences, I)
    x9 = fix_first_argument(fix_first_argument, shift_by_vector)
    x10 = compose(x7, upper_left_corner)
    x11 = chain(x10, x6, shift_to_origin)
    x12 = chain(x8, x6, shift_to_origin)
    x13 = combine_two_function_results(transform, x11, x12)
    x14 = compose(x9, shift_to_origin)
    x15 = combine_two_function_results(transform_and_flatten, x14, x13)
    #x16 = as_tuple(counterdiagonal_mirror, diagonal_mirror)
    x16 = as_generic_tuple(counterdiagonal_mirror, diagonal_mirror) # mdda
    #x17 = as_tuple(horizontal_mirror, vertical_mirror)
    x17 = as_generic_tuple(horizontal_mirror, vertical_mirror) # mdda
    x18 = union(x16, x17)
    x19 = cartesian_product(x18, x18)
    x20 = combine_two_function_results(compose, get_first, get_last)
    x21 = transform(x20, x19)
    x22 = to_tuple(x21)
    x23 = union(x18, x22)
    x24 = apply_each_function(x23, x2)
    x25 = transform_and_flatten(x15, x24)
    O = paint_onto_grid(I, x25)
    return O


def solve_98cf29f8(I):
    x1 = partition_only_foreground(I)
    x2 = combine_two_function_results(multiply, get_height, get_width)
    x3 = combine_two_function_results(is_equal, size, x2)
    x4 = extract_first_matching(x1, x3)
    x5 = get_other(x1, x4)
    x6 = get_color(x5)
    x7 = fix_last_argument(greater_than, 3)
    x8 = fix_last_argument(to_object, I)
    x9 = fix_last_argument(color_count, x6)
    x10 = chain(x8, diagonal_neighbors, get_last)
    x11 = chain(x7, x9, x10)
    x12 = keep_if_condition(x5, x11)
    x13 = outbox(x12)
    x14 = bounding_box_indices(x13)
    x15 = erase_patch(I, x5)
    x16 = move_until_touching(x14, x4)
    x17 = shift_by_vector(x14, x16)
    O = fill(x15, x6, x17)
    return O


def solve_469497ad(I):
    x1 = count_colors(I)
    x2 = decrement(x1)
    x3 = upscale(I, x2)
    x4 = as_objects(x3, False, False, True)
    x5 = argmin(x4, size)
    x6 = upper_left_corner(x5)
    x7 = lower_left_corner(x5)
    x8 = shoot(x6, NEG_UNITY)
    x9 = shoot(x6, UNITY)
    x10 = shoot(x7, DOWN_LEFT)
    x11 = shoot(x7, UP_RIGHT)
    x12 = union(x8, x9)
    x13 = union(x10, x11)
    x14 = union(x12, x13)
    x15 = fill_background(x3, COLOR_TWO, x14)
    x16 = as_objects(x15, True, False, True)
    x17 = argmax(x16, lower_right_corner)
    O = paint_onto_grid(x15, x17)
    return O


def solve_39e1d7f9(I):
    x1 = partition_only_foreground(I)
    x2 = as_objects(I, True, False, True)
    x3 = sort(x1, get_height)
    x4 = get_last(x3)
    x5 = remove(x4, x3)
    x6 = get_last(x5)
    x7 = get_color(x6)
    x8 = color_filter(x2, x7)
    x9 = power(outbox, 2)
    x10 = fix_last_argument(to_object, I)
    # Nix.start
    #x11 = chain(count_colors, x10, x9)
    #x12 = argmax(x8, x11)
    #x13 = upper_left_corner(x12)
    #x14 = get_shape(x12)
    #x15 = subtract(x13, x14)
    #x16 = decrement(x15)
    #x17 = multiply(x14, 3)
    #x18 = add(x17, TWO_BY_TWO)
    #x19 = crop(I, x16, x18)
    #x20 = as_object(x19)
    #x21 = transform(upper_left_corner, x8)
    #x22 = increment(x14)
    #x23 = fix_last_argument(subtract, x22)
    #x24 = transform(x23, x21)
    #x25 = fix_first_argument(shift_by_vector, x20)
    #x26 = transform_and_flatten(x25, x24)
    #O = paint_onto_grid(I, x26)
    # NIX.end
    x11 = most_common_color(I)
    x12 = fix_first_argument(remove, x11)
    x13 = chain(size, x12, palette)
    x14 = chain(x13, x10, x9)
    x15 = argmax(x8, x14)
    x16 = upper_left_corner(x15)
    x17 = get_shape(x15)
    x18 = subtract(x16, x17)
    x19 = decrement(x18)
    x20 = multiply(x17, 3)
    x21 = add(x20, TWO_BY_TWO)
    x22 = crop(I, x19, x21)
    x23 = as_object(x22)
    x24 = transform(upper_left_corner, x8)
    x25 = increment(x17)
    x26 = fix_last_argument(subtract, x25)
    x27 = transform(x26, x24)
    x28 = fix_first_argument(shift_by_vector, x23)
    x29 = transform_and_flatten(x28, x27)
    O = paint_onto_grid(I, x29)
    return O


def solve_484b58aa(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = partition(I)
    x4 = color_filter(x3, COLOR_ZERO)
    x5 = difference(x3, x4)
    x6 = flatten(x5)
    x7 = as_tuple(x1, 2)
    x8 = as_tuple(2, x2)
    x9 = power(decrement, 2)
    x10 = x9(x1)
    x11 = x9(x2)
    x12 = to_vertical_vec(x11)
    x13 = to_horizontal_vec(x10)
    x14 = crop(I, x12, x8)
    x15 = crop(I, x13, x7)
    x16 = as_object(x15)
    x17 = as_object(x14)
    x18 = vertical_periodicity(x16)
    x19 = horizontal_periodicity(x17)
    x20 = as_tuple(x18, x19)
    x21 = fix_first_argument(multiply, x20)
    x22 = neighbors(ORIGIN)
    x23 = transform_and_flatten(neighbors, x22)
    x24 = transform(x21, x23)
    x25 = fix_first_argument(shift_by_vector, x6)
    x26 = transform_and_flatten(x25, x24)
    O = paint_onto_grid(I, x26)
    return O


def solve_3befdf3e(I):
    x1 = as_objects(I, False, False, True)
    x2 = least_common_color(I)
    x3 = palette(I)
    x4 = remove(COLOR_ZERO, x3)
    x5 = get_other(x4, x2)
    x6 = switch(I, x2, x5)
    x7 = compose(get_width, inbox)
    x8 = fix_first_argument(power, outbox)
    x9 = compose(x8, x7)
    x10 = initset(x9)
    x11 = fix_first_argument(apply_each_function, x10)
    x12 = chain(initset, get_first, x11)
    x13 = combine_two_function_results(apply_each_function, x12, identity)
    x14 = compose(get_first, x13)
    x15 = compose(bounding_box_indices, x14)
    x16 = fix_first_argument(chain, bounding_box_indices)
    x17 = fix_first_argument(x16, inbox)
    x18 = compose(x17, x9)
    x19 = fix_first_argument(transform, initset)
    x20 = chain(x19, corner_indices, x15)
    x21 = combine_two_function_results(transform_and_flatten, x18, x20)
    x22 = combine_two_function_results(intersection, x15, x21)
    x23 = transform_and_flatten(x15, x1)
    x24 = transform_and_flatten(x22, x1)
    x25 = fill_background(x6, x5, x23)
    O = fill(x25, COLOR_ZERO, x24)
    return O


def solve_9aec4887(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmin(x1, count_colors)
    x3 = get_other(x1, x2)
    x4 = smallest_subgrid_containing(x3, I)
    x5 = shift_to_origin(x2)
    x6 = shift_by_vector(x5, UNITY)
    x7 = to_indices(x6)
    x8 = shift_to_origin(x3)
    x9 = fix_first_argument(argmin, x8)
    x11 = fix_first_argument(fix_last_argument, manhattan_distance)
    x12 = fix_last_argument(compose, initset)
    x13 = chain(x12, x11, initset)
    x14 = chain(get_first, x9, x13)
    x15 = combine_two_function_results(as_tuple, x14, identity)
    x16 = transform(x15, x7)
    x17 = paint_onto_grid(x4, x16)
    x18 = combine_two_function_results(line_between, upper_left_corner, lower_right_corner)
    x19 = x18(x7)
    x20 = combine_two_function_results(union, identity, vertical_mirror)
    x21 = x20(x19)
    x22 = intersection(x7, x21)
    O = fill(x17, COLOR_EIGHT, x22)
    return O


def solve_49d1d64f(I):
    x1 = get_shape(I)
    x2 = add(x1, 2)
    x3 = create_grid(COLOR_ZERO, x2)
    x4 = as_object(I)
    x5 = shift_by_vector(x4, UNITY)
    x6 = paint_onto_grid(x3, x5)
    x7 = as_indices(x3)
    x8 = combine_two_function_results(difference, box, corner_indices)
    x9 = x8(x7)
    x10 = fix_first_argument(fix_first_argument, manhattan_distance)
    x11 = fix_last_argument(compose, initset)
    x12 = chain(x11, x10, initset)
    x13 = fix_first_argument(argmin, x5)
    x14 = chain(get_first, x13, x12)
    x15 = combine_two_function_results(as_tuple, x14, identity)
    x16 = transform(x15, x9)
    O = paint_onto_grid(x6, x16)
    return O


def solve_57aa92db(I):
    x1 = as_objects(I, False, True, True)
    x2 = as_objects(I, True, False, True)
    x3 = fix_first_argument(fix_first_argument, color_count)
    x4 = combine_two_function_results(transform, x3, palette)
    x5 = compose(maximum, x4)
    x6 = compose(minimum, x4)
    x7 = combine_two_function_results(subtract, x5, x6)
    x8 = argmax(x1, x7)
    x9 = least_common_color(x8)
    x10 = shift_to_origin(x8)
    x11 = equals(get_first, x9)
    x12 = keep_if_condition(x10, x11)
    x13 = upper_left_corner(x12)
    x14 = color_filter(x2, x9)
    x15 = fix_last_argument(to_object, I)
    x16 = fix_first_argument(remove, COLOR_ZERO)
    x17 = chain(get_first, x16, palette)
    x18 = chain(x17, x15, outbox)
    x19 = fix_first_argument(multiply, x13)
    x20 = compose(x19, get_width)
    x21 = combine_two_function_results(subtract, upper_left_corner, x20)
    x22 = fix_first_argument(shift_by_vector, x10)
    x23 = compose(x22, x21)
    x24 = combine_two_function_results(upscale, x23, get_width)
    x25 = combine_two_function_results(recolor, x18, x24)
    x26 = transform_and_flatten(x25, x14)
    x27 = paint_onto_grid(I, x26)
    x28 = flatten(x2)
    O = paint_onto_grid(x27, x28)
    return O


def solve_aba27056(I):
    x1 = as_objects(I, True, False, True)
    x2 = transform_and_flatten(to_indices, x1)
    x3 = box(x2)
    x4 = difference(x3, x2)
    x5 = bounding_box_delta(x2)
    x6 = position(x5, x4)
    x7 = interval(0, 9, 1)
    x8 = fix_first_argument(multiply, x6)
    x9 = transform(x8, x7)
    x10 = fix_first_argument(shift_by_vector, x4)
    x11 = transform_and_flatten(x10, x9)
    x12 = fill(I, COLOR_FOUR, x5)
    x13 = fill(x12, COLOR_FOUR, x11)
    x14 = corner_indices(x4)
    x15 = of_color(x13, COLOR_ZERO)
    x16 = fix_last_argument(to_object, x13)
    x17 = fix_last_argument(color_count, COLOR_ZERO)
    x18 = chain(x17, x16, direct_neighbors)
    x19 = equals(x18, 2)
    x20 = fix_last_argument(adjacent, x2)
    x21 = fix_last_argument(adjacent, x11)
    x22 = combine_two_function_results(logical_and, x20, x21)
    x23 = compose(x22, initset)
    x24 = keep_if_condition(x15, x19)
    x25 = keep_if_condition(x24, x23)
    x26 = cartesian_product(x14, x25)
    x27 = combine_two_function_results(subtract, get_last, get_first)
    x28 = combine_two_function_results(shoot, get_first, x27)
    x29 = transform_and_flatten(x28, x26)
    O = fill(x13, COLOR_FOUR, x29)
    return O


def solve_f1cefba8(I):
    x1 = palette(I)
    x2 = as_objects(I, False, False, True)
    x3 = of_color(I, COLOR_ZERO)
    x4 = get_first(x2)
    x5 = upper_left_corner(x4)
    x6 = smallest_subgrid_containing(x4, I)
    x7 = power(trim_border, 2)
    x8 = x7(x6)
    x9 = as_indices(x8)
    x10 = shift_by_vector(x9, TWO_BY_TWO)
    x11 = fill(x6, COLOR_ZERO, x10)
    x12 = least_common_color(x11)
    x13 = remove(COLOR_ZERO, x1)
    x14 = get_other(x13, x12)
    x15 = of_color(x11, x12)
    x16 = shift_by_vector(x15, x5)
    x17 = of_color(I, x12)
    x18 = uppermost(x17)
    x19 = lowermost(x17)
    x20 = equals(get_first, x18)
    x21 = equals(get_first, x19)
    x22 = combine_two_function_results(logical_or, x20, x21)
    x23 = keep_if_condition(x16, x22)
    x24 = difference(x16, x23)
    x25 = transform_and_flatten(vertical_line, x23)
    x26 = transform_and_flatten(horizontal_line, x24)
    x27 = union(x25, x26)
    x28 = intersection(x3, x27)
    x29 = fill(I, x14, x27)
    O = fill(x29, x12, x28)
    return O


def solve_1e32b0e9(I):
    x1 = get_height(I)
    x2 = most_common_color(I)
    x3 = as_object(I)
    x4 = subtract(x1, 2)
    x5 = divide(x4, 3)
    x6 = as_tuple(x5, x5)
    x7 = crop(I, ORIGIN, x6)
    x8 = partition(x7)
    x9 = equals(get_color, COLOR_ZERO)
    x10 = compose(logical_not, x9)
    x11 = extract_first_matching(x8, x10)
    x12 = initset(x2)
    x13 = palette(x3)
    x14 = palette(x11)
    x15 = difference(x13, x14)
    x16 = difference(x15, x12)
    x17 = get_first(x16)
    x18 = interval(0, 3, 1)
    x19 = cartesian_product(x18, x18)
    x20 = to_tuple(x19)
    x21 = transform(get_first, x20)
    x22 = transform(get_last, x20)
    x23 = fix_first_argument(multiply, x5)
    x24 = transform(x23, x21)
    x25 = transform(x23, x22)
    x26 = transform_both(add, x24, x21)
    x27 = transform_both(add, x25, x22)
    x28 = transform_both(as_tuple, x26, x27)
    x29 = fix_first_argument(shift_by_vector, x11)
    x30 = transform_and_flatten(x29, x28)
    O = fill_background(I, x17, x30)
    return O


def solve_28e73c20(I):
    x1 = get_width(I)
    x2 = as_tuple(1, 2)
    x3 = as_tuple(2, 2)
    x4 = as_tuple(2, 1)
    x5 = as_tuple(3, 1)
    x6 = create_grid(COLOR_THREE, UNITY)
    x7 = upscale(x6, 4)
    x8 = initset(DOWN)
    x9 = insert(UNITY, x8)
    x10 = insert(x2, x9)
    x11 = insert(x3, x10)
    x12 = fill(x7, COLOR_ZERO, x11)
    x13 = vertical_upscale(x6, 5)
    x14 = horizontal_upscale(x13, 3)
    x15 = insert(x4, x9)
    x16 = insert(x5, x15)
    x17 = fill(x14, COLOR_ZERO, x16)
    x18 = is_even(x1)
    x19 = condition_if_else(x18, x12, x17)
    x20 = create_grid(COLOR_ZERO, UNITY)
    x21 = fix_first_argument(horizontal_upscale, x20)
    x22 = chain(x21, decrement, get_height)
    x23 = fix_last_argument(horizontal_concat, x6)
    x24 = compose(x23, x22)
    x25 = fix_first_argument(horizontal_upscale, x6)
    x26 = compose(x25, get_height)
    x27 = combine_two_function_results(vertical_concat, x24, rot90)
    x28 = combine_two_function_results(vertical_concat, x26, x27)
    x29 = subtract(x1, 4)
    x30 = power(x28, x29)
    O = x30(x19)
    return O


def solve_4c5c2cf0(I):
    x1 = as_objects(I, True, True, True)
    x2 = as_objects(I, False, True, True)
    x3 = get_first(x2)
    x4 = fix_last_argument(smallest_subgrid_containing, I)
    x5 = combine_two_function_results(is_equal, identity, rot90)
    x6 = compose(x5, x4)
    x7 = extract_first_matching(x1, x6)
    x8 = center(x7)
    x9 = smallest_subgrid_containing(x3, I)
    x10 = horizontal_mirror(x9)
    x11 = as_objects(x10, False, True, True)
    x12 = get_first(x11)
    x13 = as_objects(x10, True, True, True)
    #
    # See: https://github.com/michaelhodel/arc-dsl/pull/12/commits/20e94eb88030a45ed9cb9bbf3027d315f9eede0d
    #x14 = extract_first_matching(x13, x6)
    #
    y1 = fix_last_argument(smallest_subgrid_containing, x10)
    y2 = compose(x5, y1)
    x14 = extract_first_matching(x13, y2)    
    #
    x15 = center(x14)
    x16 = subtract(x8, x15)
    x17 = shift_by_vector(x12, x16)
    x18 = paint_onto_grid(I, x17)
    x19 = as_objects(x18, False, True, True)
    x20 = get_first(x19)
    x21 = smallest_subgrid_containing(x20, x18)
    x22 = vertical_mirror(x21)
    x23 = as_objects(x22, False, True, True)
    x24 = get_first(x23)
    x25 = as_objects(x22, True, True, True)
    x26 = get_color(x7)
    x27 = equals(get_color, x26)
    x28 = extract_first_matching(x25, x27)
    x29 = center(x28)
    x30 = subtract(x8, x29)
    x31 = shift_by_vector(x24, x30)
    O = paint_onto_grid(x18, x31)
    return O


def solve_508bd3b6(I):
    x1 = get_width(I)
    x2 = as_objects(I, True, True, True)
    x3 = argmin(x2, size)
    x4 = argmax(x2, size)
    x5 = upper_left_corner(x3)
    x6 = upper_right_corner(x3)
    x7 = color_at_location(I, x5)
    x8 = is_equal(x7, COLOR_EIGHT)
    x9 = condition_if_else(x8, x5, x6)
    x10 = condition_if_else(x8, UNITY, DOWN_LEFT)
    x11 = multiply(x10, x1)
    x12 = double(x11)
    x13 = add(x9, x12)
    x14 = subtract(x9, x12)
    x15 = line_between(x13, x14)
    x16 = fill(I, COLOR_THREE, x15)
    x17 = paint_onto_grid(x16, x4)
    x18 = as_objects(x17, True, False, True)
    x19 = fix_last_argument(adjacent, x4)
    x20 = extract_first_matching(x18, x19)
    x21 = get_first(x20)
    x22 = get_last(x21)
    x23 = logical_not(x8)
    x24 = condition_if_else(x23, UNITY, DOWN_LEFT)
    x25 = multiply(x24, x1)
    x26 = double(x25)
    x27 = add(x22, x26)
    x28 = subtract(x22, x26)
    x29 = line_between(x27, x28)
    x30 = fill(x17, COLOR_THREE, x29)
    x31 = paint_onto_grid(x30, x3)
    O = paint_onto_grid(x31, x4)
    return O


def solve_6d0160f0(I):
    x1 = of_color(I, COLOR_FOUR)
    x2 = get_first(x1)   # coords of COLOR_FOUR
    x3 = get_first(x2)   # row
    x4 = get_last(x2)    # col
    x5 = greater_than(x3, 3)
    x6 = greater_than(x3, 7)
    x7 = greater_than(x4, 3)
    x8 = greater_than(x4, 7)
    x9 = condition_if_else(x5, 4, 0)
    x10 = condition_if_else(x6, 8, x9)
    x11 = condition_if_else(x7, 4, 0)
    x12 = condition_if_else(x8, 8, x11)
    x13 = as_tuple(x10, x12)
    x14 = initset(0)
    x15 = insert(4, x14)
    x16 = insert(8, x15)
    x17 = cartesian_product(x16, x16)
    x18 = crop(I, ORIGIN, THREE_BY_THREE)
    x19 = as_indices(x18)
    x20 = recolor(COLOR_ZERO, x19)
    x21 = fix_first_argument(shift_by_vector, x20)
    x22 = transform_and_flatten(x21, x17)
    x23 = paint_onto_grid(I, x22)
    x24 = crop(I, x13, THREE_BY_THREE)
    x25 = replace(x24, COLOR_FIVE, COLOR_ZERO)
    x26 = of_color(x25, COLOR_FOUR)
    x27 = get_first(x26)
    x28 = as_indices(x25)
    x29 = to_object(x28, x25)
    x30 = multiply(x27, 4)
    x31 = shift_by_vector(x29, x30)
    O = paint_onto_grid(x23, x31)
    return O


def solve_f8a8fe49(I):
    x1 = as_objects(I, True, False, True)
    x2 = replace(I, COLOR_FIVE, COLOR_ZERO)
    x3 = color_filter(x1, COLOR_TWO)
    x4 = get_first(x3)
    x5 = is_portrait(x4)
    x6 = condition_if_else(x5, horizontal_split, vertical_split)
    x7 = condition_if_else(x5, vertical_mirror, horizontal_mirror)
    x8 = of_color(I, COLOR_TWO)
    x9 = smallest_subgrid_containing(x8, I)
    x10 = trim_border(x9)
    x11 = x7(x10)
    x12 = x6(x11, 2)
    x13 = compose(shift_to_origin, as_object)
    x14 = transform(x13, x12)
    x15 = get_last(x14)
    x16 = get_first(x14)
    x17 = upper_left_corner(x8)
    x18 = increment(x17)
    x19 = shift_by_vector(x15, x18)
    x20 = shift_by_vector(x16, x18)
    x21 = condition_if_else(x5, get_width, get_height)
    x22 = condition_if_else(x5, to_horizontal_vec, to_vertical_vec)
    x23 = x21(x15)
    x24 = double(x23)
    x25 = compose(x22, increment)
    x26 = x25(x23)
    x27 = negate(x26)
    x28 = x25(x24)
    x29 = shift_by_vector(x19, x27)
    x30 = shift_by_vector(x20, x28)
    x31 = paint_onto_grid(x2, x29)
    O = paint_onto_grid(x31, x30)
    return O


def solve_d07ae81c(I):
    x1 = as_objects(I, True, False, False)
    x2 = size_filter(x1, 1)
    x3 = transform(get_color, x2)
    x4 = difference(x1, x2)
    x5 = transform(get_color, x4)
    x6 = get_first(x5)
    x7 = get_last(x5)
    x8 = of_color(I, x6)
    x9 = of_color(I, x7)
    x10 = fix_last_argument(shoot, UNITY)
    x11 = fix_last_argument(shoot, NEG_UNITY)
    x12 = fix_last_argument(shoot, DOWN_LEFT)
    x13 = fix_last_argument(shoot, UP_RIGHT)
    x14 = combine_two_function_results(union, x10, x11)
    x15 = combine_two_function_results(union, x12, x13)
    x16 = combine_two_function_results(union, x14, x15)
    x17 = compose(x16, center)
    x18 = transform_and_flatten(x17, x2)
    x19 = intersection(x8, x18)
    x20 = intersection(x9, x18)
    x21 = get_first(x2)
    x22 = get_color(x21)
    x23 = center(x21)
    x24 = neighbors(x23)
    x25 = to_object(x24, I)
    x26 = most_common_color(x25)
    x27 = get_other(x3, x22)
    x28 = is_equal(x26, x6)
    x29 = condition_if_else(x28, x22, x27)
    x30 = condition_if_else(x28, x27, x22)
    x31 = fill(I, x29, x19)
    O = fill(x31, x30, x20)
    return O


def solve_6a1e5592(I):
    x1 = get_width(I)
    x2 = as_objects(I, True, False, True)
    x3 = as_tuple(5, x1)
    x4 = crop(I, ORIGIN, x3)
    x5 = color_filter(x2, COLOR_FIVE)
    x6 = flatten(x5)
    x7 = erase_patch(I, x6)
    x8 = compose(to_indices, shift_to_origin)
    x9 = transform(x8, x5)
    x10 = as_indices(x4)
    x11 = of_color(x4, COLOR_ZERO)
    x12 = of_color(x4, COLOR_TWO)
    x13 = fix_last_argument(multiply, 10)
    #
    # See : https://github.com/michaelhodel/arc-dsl/pull/13/commits/eeaebe6233035def60510fc538c912569acd3116
    #x14 = fix_last_argument(multiply, 8)
    x14 = fix_last_argument(multiply, 5)
    #
    x15 = fix_last_argument(intersection, x12)
    x16 = fix_last_argument(intersection, x11)
    x17 = fix_last_argument(intersection, x10)
    x18 = chain(x13, size, x15)
    x19 = chain(size, x16, bounding_box_delta)
    x20 = compose(x14, uppermost)
    x21 = chain(size, x16, outbox)
    x22 = chain(x13, size, x17)
    x23 = compose(negate, x18)
    x24 = combine_two_function_results(add, x22, x23)
    x25 = combine_two_function_results(subtract, x24, x21)
    x26 = combine_two_function_results(subtract, x25, x20)
    x27 = combine_two_function_results(subtract, x26, x19)
    x28 = fix_last_argument(transform, x10)
    x29 = fix_first_argument(fix_first_argument, shift_by_vector)
    x30 = fix_last_argument(argmax, x27)
    x31 = chain(x30, x28, x29)
    x32 = transform_and_flatten(x31, x9)
    O = fill(x7, COLOR_ONE, x32)
    return O


def solve_0e206a2e(I):
    x1 = palette(I)
    x2 = as_objects(I, False, False, True)
    x3 = fix_last_argument(greater_than, 1)
    x4 = compose(x3, count_colors)
    x5 = keep_if_condition(x2, x4)
    x6 = remove(COLOR_ZERO, x1)
    x7 = fix_first_argument(color_count, I)
    x8 = argmax(x6, x7)
    x9 = remove(x8, x6)
    x10 = fix_last_argument(contains, x9)
    x11 = compose(x10, get_first)
    x12 = fix_last_argument(keep_if_condition, x11)
    x13 = fix_first_argument(fix_last_argument, subtract)
    x14 = fix_first_argument(occurrences, I)
    x15 = fix_first_argument(fix_first_argument, shift_by_vector)
    x16 = compose(x13, upper_left_corner)
    x17 = chain(x16, x12, shift_to_origin)
    x18 = chain(x14, x12, shift_to_origin)
    x19 = combine_two_function_results(transform, x17, x18)
    x20 = compose(x15, shift_to_origin)
    x21 = combine_two_function_results(transform_and_flatten, x20, x19)
    #x22 = as_tuple(counterdiagonal_mirror, diagonal_mirror)
    x22 = as_generic_tuple(counterdiagonal_mirror, diagonal_mirror)  # mdda
    #x23 = as_tuple(horizontal_mirror, vertical_mirror)
    x23 = as_generic_tuple(horizontal_mirror, vertical_mirror) # mdda
    x24 = union(x22, x23)
    x25 = cartesian_product(x24, x24)
    x26 = combine_two_function_results(compose, get_first, get_last)
    x27 = transform(x26, x25)
    x28 = to_tuple(x27)
    x29 = union(x24, x28)
    x30 = fix_first_argument(apply_each_function, x29)
    x31 = transform_and_flatten(x30, x5)
    x32 = transform_and_flatten(x21, x31)
    x33 = paint_onto_grid(I, x32)
    x34 = flatten(x5)
    O = erase_patch(x33, x34)
    return O


def solve_d22278a0(I):
    x1 = as_indices(I)
    x2 = as_objects(I, True, False, True)
    x3 = combine_two_function_results(multiply, sign, identity)
    x4 = fix_first_argument(transform, x3)
    x5 = chain(is_even, maximum, x4)
    x6 = fix_first_argument(keep_if_condition, x1)
    x7 = combine_two_function_results(add, get_first, get_last)
    x8 = fix_last_argument(remove, x2)
    x9 = compose(center, get_last)
    x10 = combine_two_function_results(subtract, get_first, x9)
    x11 = compose(x5, x10)
    x12 = fix_first_argument(fix_last_argument, is_equal)
    x13 = fix_first_argument(argmin, x2)
    x14 = chain(x7, x4, x10)
    x15 = fix_first_argument(fix_first_argument, as_tuple)
    x16 = fix_first_argument(fix_last_argument, as_tuple)
    x17 = fix_first_argument(compose, x11)
    x18 = fix_first_argument(compose, x14)
    x19 = compose(x18, x15)
    x20 = compose(x18, x16)
    x21 = compose(x13, x19)
    x22 = fix_last_argument(compose, x21)
    x23 = fix_first_argument(fix_first_argument, valmin)
    x24 = fix_last_argument(compose, x19)
    x25 = chain(x24, x23, x8)
    x26 = fix_first_argument(combine_two_function_results, greater_than)
    x27 = combine_two_function_results(x26, x25, x20)
    x28 = chain(x6, x17, x16)
    x29 = chain(x6, x22, x12)
    x30 = combine_two_function_results(intersection, x28, x29)
    x31 = compose(x6, x27)
    x32 = combine_two_function_results(intersection, x30, x31)
    x33 = combine_two_function_results(recolor, get_color, x32)
    x34 = transform_and_flatten(x33, x2)
    O = paint_onto_grid(I, x34)
    return O


def solve_4290ef0e(I):
    x1 = most_common_color(I)
    x2 = partition_only_foreground(I)
    x3 = as_objects(I, True, False, True)
    x4 = fix_last_argument(valmax, get_width)
    x5 = fix_first_argument(color_filter, x3)
    #
    # See : https://github.com/michaelhodel/arc-dsl/pull/11/commits/785a0f74d2fce740ad7294640daa8b1c11fc7c50
    #x6 = chain(x4, x5, get_color)
    #x7 = compose(maximum, get_shape)
    #x8 = combine_two_function_results(add, x7, x6)
    #x9 = compose(negate, x8)
    #
    x6 = compose(x5, get_color)
    y1 = compose(double, x4)
    y2 = fix_first_argument(apply_function_on_cartesian_product, manhattan_distance)
    y3 = combine_two_function_results(y2, identity, identity)
    y4 = fix_first_argument(remove, 0)
    y5 = compose(y4, y3)
    y6 = fix_last_argument(condition_if_else, -2)
    y7 = combine_two_function_results(y6, is_positive, decrement)
    y8 = chain(y7, minimum, y5)
    y9 = combine_two_function_results(add, y8, y1)
    y10 = compose(y9, x6)
    x9 = compose(negate, y10)
    #
    x10 = sort(x2, x9)
    x11 = fix_last_argument(argmin, centerofmass)
    x12 = compose(initset, vertical_mirror)
    x13 = combine_two_function_results(insert, diagonal_mirror, x12)
    x14 = combine_two_function_results(insert, counterdiagonal_mirror, x13)
    x15 = combine_two_function_results(insert, horizontal_mirror, x14)
    x16 = compose(x11, x15)
    x17 = transform(x16, x10)
    x18 = size(x2)
    x19 = transform(size, x2)
    x20 = contains(1, x19)   # mdda : not COLOR_ONE
    x21 = increment(x18)
    x22 = condition_if_else(x20, x18, x21)
    x23 = double(x22)
    x24 = decrement(x23)
    x25 = transform(shift_to_origin, x17)
    x26 = interval(0, x22, 1)
    x27 = pairwise(x26, x26)
    x28 = transform_both_and_flatten(shift_by_vector, x25, x27)
    x29 = as_tuple(x24, x24)
    x30 = create_grid(x1, x29)
    x31 = paint_onto_grid(x30, x28)
    x32 = rot90(x31)
    x33 = paint_onto_grid(x32, x28)
    x34 = rot90(x33)
    x35 = paint_onto_grid(x34, x28)
    x36 = rot90(x35)
    O = paint_onto_grid(x36, x28)
    return O


def solve_50846271(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = apply_function_on_cartesian_product(line_between, x1, x1)
    x3 = fix_first_argument(greater_than, 6)
    x4 = compose(x3, size)
    x5 = combine_two_function_results(logical_or, is_vertical_line, is_horizontal_line)
    x6 = combine_two_function_results(logical_and, x4, x5)
    x7 = keep_if_condition_and_flatten(x2, x6)
    x8 = fill(I, COLOR_TWO, x7)
    x9 = as_objects(x8, True, False, False)
    x10 = color_filter(x9, COLOR_TWO)
    x11 = valmax(x10, get_width)
    x12 = halve(x11)
    x13 = to_vertical_vec(x12)
    x14 = to_horizontal_vec(x12)
    x15 = fix_last_argument(add, ZERO_BY_TWO)
    x16 = fix_last_argument(add, TWO_BY_ZERO)
    x17 = fix_last_argument(subtract, ZERO_BY_TWO)
    x18 = fix_last_argument(subtract, TWO_BY_ZERO)
    x19 = fix_last_argument(color_count, COLOR_TWO)
    x20 = fix_last_argument(to_object, x8)
    x21 = compose(initset, x15)
    x22 = combine_two_function_results(insert, x16, x21)
    x23 = combine_two_function_results(insert, x17, x22)
    x24 = combine_two_function_results(insert, x18, x23)
    x25 = combine_two_function_results(union, direct_neighbors, x24)
    x26 = chain(x19, x20, x25)
    x27 = fix_last_argument(argmax, x26)
    x28 = compose(x27, to_indices)
    x29 = transform(x28, x10)
    x30 = fix_last_argument(add, x13)
    x31 = fix_last_argument(subtract, x13)
    x32 = fix_last_argument(add, x14)
    x33 = fix_last_argument(subtract, x14)
    x34 = combine_two_function_results(line_between, x30, x31)
    x35 = combine_two_function_results(line_between, x32, x33)
    x36 = combine_two_function_results(union, x34, x35)
    x37 = transform_and_flatten(x36, x29)
    x38 = fill(x8, COLOR_EIGHT, x37)
    O = fill(x38, COLOR_TWO, x1)
    return O


def solve_b527c5c6(I):
    x1 = as_objects(I, False, False, True)
    x2 = equals(get_first, COLOR_TWO)
    x3 = fix_last_argument(keep_if_condition, x2)
    x4 = compose(lowermost, x3)
    x5 = compose(rightmost, x3)
    x6 = compose(uppermost, x3)
    x7 = compose(leftmost, x3)
    x8 = combine_two_function_results(is_equal, x4, lowermost)
    x9 = combine_two_function_results(is_equal, x5, rightmost)
    x10 = combine_two_function_results(is_equal, x6, uppermost)
    x11 = combine_two_function_results(is_equal, x7, leftmost)
    x12 = compose(negate, x10)
    x13 = compose(negate, x11)
    x14 = combine_two_function_results(add, x12, x8)
    x15 = combine_two_function_results(add, x13, x9)
    x16 = combine_two_function_results(as_tuple, x14, x15)
    x17 = compose(center, x3)
    x18 = combine_two_function_results(shoot, x17, x16)
    x19 = transform_and_flatten(x18, x1)
    x20 = fill(I, COLOR_TWO, x19)
    x21 = compose(is_vertical_line, x18)
    x22 = keep_if_condition(x1, x21)
    x23 = difference(x1, x22)
    x24 = chain(decrement, minimum, get_shape)
    x25 = compose(increment, x24)
    x26 = compose(negate, x24)
    x27 = fix_last_argument(interval, 1)
    x28 = combine_two_function_results(x27, x26, x25)
    x29 = fix_first_argument(transform, to_vertical_vec)
    x30 = fix_first_argument(transform, to_horizontal_vec)
    x31 = fix_first_argument(fix_first_argument, shift_by_vector)
    x32 = compose(x31, x18)
    x33 = compose(x29, x28)
    x34 = compose(x30, x28)
    x35 = combine_two_function_results(transform_and_flatten, x32, x33)
    x36 = combine_two_function_results(transform_and_flatten, x32, x34)
    x37 = transform_and_flatten(x35, x23)
    x38 = transform_and_flatten(x36, x22)
    x39 = union(x37, x38)
    O = fill_background(x20, COLOR_THREE, x39)
    return O


def solve_150deff5(I):
    x1 = create_grid(COLOR_FIVE, TWO_BY_TWO)
    x2 = as_object(x1)
    x3 = occurrences(I, x2)
    x4 = fix_first_argument(shift_by_vector, x2)
    x5 = transform_and_flatten(x4, x3)
    x6 = fill(I, COLOR_EIGHT, x5)
    x7 = create_grid(COLOR_FIVE, UNITY)
    x8 = as_tuple(2, 1)
    x9 = create_grid(COLOR_EIGHT, x8)
    x10 = vertical_concat(x9, x7)
    x11 = as_object(x10)
    x12 = occurrences(x6, x11)
    x13 = fix_first_argument(shift_by_vector, x11)
    x14 = transform_and_flatten(x13, x12)
    x15 = fill(x6, COLOR_TWO, x14)
    x16 = as_tuple(1, 3)
    x17 = create_grid(COLOR_FIVE, x16)
    x18 = as_object(x17)
    x19 = occurrences(x15, x18)
    x20 = fix_first_argument(shift_by_vector, x18)
    x21 = transform_and_flatten(x20, x19)
    x22 = fill(x15, COLOR_TWO, x21)
    x23 = horizontal_mirror(x10)
    x24 = as_object(x23)
    x25 = occurrences(x22, x24)
    x26 = fix_first_argument(shift_by_vector, x24)
    x27 = transform_and_flatten(x26, x25)
    x28 = fill(x22, COLOR_TWO, x27)
    x29 = diagonal_mirror(x10)
    x30 = as_object(x29)
    x31 = occurrences(x28, x30)
    x32 = fix_first_argument(shift_by_vector, x30)
    x33 = transform_and_flatten(x32, x31)
    x34 = fill(x28, COLOR_TWO, x33)
    x35 = vertical_mirror(x29)
    x36 = as_object(x35)
    x37 = occurrences(x34, x36)
    x38 = fix_first_argument(shift_by_vector, x36)
    x39 = transform_and_flatten(x38, x37)
    O = fill(x34, COLOR_TWO, x39)
    return O


def solve_b7249182(I):
    x1 = as_objects(I, True, False, True)
    x2 = flatten(x1)
    x3 = is_portrait(x2)
    x4 = condition_if_else(x3, identity, diagonal_mirror)
    x5 = x4(I)
    x6 = as_objects(x5, True, False, True)
    x7 = sort(x6, uppermost)
    x8 = get_first(x7)
    x9 = get_last(x7)
    x10 = get_color(x8)
    x11 = get_color(x9)
    x12 = compose(get_first, to_indices)
    x13 = x12(x8)
    x14 = x12(x9)
    x15 = line_between(x13, x14)
    x16 = centerofmass(x15)
    x17 = line_between(x13, x16)
    x18 = fill(x5, x11, x15)
    x19 = fill(x18, x10, x17)
    x20 = add(x16, DOWN)
    x21 = initset(x16)
    x22 = insert(x20, x21)
    x23 = to_object(x22, x19)
    x24 = as_tuple(0, -2)
    x25 = shift_by_vector(x23, ZERO_BY_TWO)
    x26 = shift_by_vector(x23, x24)
    x27 = union(x25, x26)
    x28 = upper_left_corner(x27)
    x29 = upper_right_corner(x27)
    x30 = line_between(x28, x29)
    x31 = shift_by_vector(x30, UP)
    x32 = lower_left_corner(x27)
    x33 = lower_right_corner(x27)
    x34 = line_between(x32, x33)
    x35 = shift_by_vector(x34, DOWN)
    x36 = paint_onto_grid(x19, x27)
    x37 = fill(x36, x10, x31)
    x38 = fill(x37, x11, x35)
    x39 = erase_patch(x38, x22)
    O = x4(x39)
    return O


def solve_9d9215db(I):
    Ipost = replace(I, COLOR_ZERO, COLOR_BELOW)  # mdda added 
    x1 = rot90(Ipost)
    x2 = rot180(Ipost)
    x3 = rot270(Ipost)
    x4 = initset(Ipost)
    x5 = chain(count_colors, left_half, top_half)
    x6 = insert(x1, x4)
    x7 = insert(x2, x6)
    x8 = insert(x3, x7)
    x9 = argmax(x8, x5)
    x10 = vertical_mirror(x9)
    x11 = transform_both(pairwise, x9, x10)
    x12 = fix_first_argument(transform, maximum)   # mdda: Implicitly assumes BLACK < other colors FIXED
    x13 = transform(x12, x11)
    x14 = partition(x13)
    x15 = size_filter(x14, 4)
    x16 = transform(lower_left_corner, x15)
    x17 = transform(lower_right_corner, x15)
    x18 = union(x16, x17)
    x19 = erase_patch(x13, x18)
    x20 = to_horizontal_vec(NEG_TWO)
    x21 = fix_last_argument(add, ZERO_BY_TWO)
    x22 = fix_last_argument(add, x20)
    x23 = compose(x21, upper_left_corner)
    x24 = compose(x22, upper_right_corner)
    x25 = combine_two_function_results(line_between, x23, x24)
    x26 = compose(is_even, get_last)
    x27 = fix_last_argument(keep_if_condition, x26)
    x28 = chain(shift_to_origin, x27, x25)
    x29 = combine_two_function_results(shift_by_vector, x28, x23)
    x30 = combine_two_function_results(recolor, get_color, x29)
    x31 = transform_and_flatten(x30, x15)
    x32 = paint_onto_grid(x19, x31)
    x33 = rot90(x32)
    x34 = rot180(x32)
    x35 = rot270(x32)
    x36 = transform_both(pairwise, x32, x33)
    x37 = transform(x12, x36)
    x38 = transform_both(pairwise, x37, x34)
    x39 = transform(x12, x38)
    x40 = transform_both(pairwise, x39, x35)
    Opre = transform(x12, x40)
    O = replace(Opre, COLOR_BELOW, COLOR_ZERO) # mdda added
    return O


def solve_6855a6e4(I):
    x1 = partition_only_foreground(I)
    x2 = rot90(I)
    x3 = color_filter(x1, COLOR_TWO)
    x4 = get_first(x3)
    x5 = is_portrait(x4)
    x6 = condition_if_else(x5, I, x2)
    x7 = as_objects(x6, True, False, True)
    x8 = color_filter(x7, COLOR_FIVE)
    x9 = transform(center, x8)
    x10 = valmin(x9, get_first)
    x11 = compose(get_first, center)
    x12 = equals(x11, x10)
    x13 = compose(logical_not, x12)
    x14 = extract_first_matching(x8, x12)
    x15 = extract_first_matching(x8, x13)
    x16 = upper_left_corner(x14)
    x17 = upper_left_corner(x15)
    x18 = smallest_subgrid_containing(x14, x6)
    x19 = smallest_subgrid_containing(x15, x6)
    x20 = horizontal_mirror(x18)
    x21 = horizontal_mirror(x19)
    x22 = of_color(x20, COLOR_FIVE)
    x23 = recolor(COLOR_FIVE, x22)
    x24 = of_color(x21, COLOR_FIVE)
    x25 = recolor(COLOR_FIVE, x24)
    x26 = get_height(x23)
    x27 = get_height(x25)
    x28 = add(3, x26)
    x29 = add(3, x27)
    x30 = to_vertical_vec(x28)
    x31 = to_vertical_vec(x29)
    x32 = add(x16, x30)
    x33 = subtract(x17, x31)
    x34 = shift_by_vector(x23, x32)
    x35 = shift_by_vector(x25, x33)
    x36 = flatten(x8)
    x37 = erase_patch(x6, x36)
    x38 = paint_onto_grid(x37, x34)
    x39 = paint_onto_grid(x38, x35)
    x40 = rot270(x39)
    O = condition_if_else(x5, x39, x40)
    return O


def solve_264363fd(I):
    x1 = as_objects(I, False, False, True)
    x2 = argmin(x1, size)
    x3 = shift_to_origin(x2)
    x4 = get_height(x2)
    x5 = get_width(x2)
    x6 = is_equal(x4, 5)
    x7 = is_equal(x5, 5)
    x8 = as_tuple(x6, x7)
    x9 = add(UNITY, x8)
    x10 = negate(x9)
    x11 = center(x2)
    x12 = color_at_location(I, x11)
    x13 = condition_if_else(x6, UP, RIGHT)
    x14 = add(x13, x11)
    x15 = color_at_location(I, x14)
    #x16 = as_tuple(x12, ORIGIN)
    x16 = make_cell(x12, ORIGIN)  # mdda
    x17 = initset(x16)
    x18 = erase_patch(I, x2)
    x19 = most_common_color(x18)
    x20 = of_color(x18, x19)
    x21 = occurrences(x18, x17)
    x22 = as_objects(x18, False, False, True)
    x23 = fix_last_argument(occurrences, x17)
    x24 = fix_last_argument(smallest_subgrid_containing, x18)
    x25 = compose(x23, x24)
    x26 = fix_first_argument(transform_and_flatten, vertical_line)
    x27 = fix_first_argument(transform_and_flatten, horizontal_line)
    x28 = compose(x26, x25)
    x29 = compose(x27, x25)
    x30 = condition_if_else(x6, x28, x29)
    x31 = condition_if_else(x7, x29, x28)
    x32 = combine_two_function_results(union, x30, x31)
    x33 = fix_first_argument(recolor, x15)
    x34 = compose(x33, x32)
    x35 = combine_two_function_results(paint_onto_grid, x24, x34)
    x36 = compose(as_object, x35)
    x37 = combine_two_function_results(shift_by_vector, x36, upper_left_corner)
    x38 = transform_and_flatten(x37, x22)
    x39 = paint_onto_grid(x18, x38)
    x40 = shift_by_vector(x3, x10)
    x41 = fix_first_argument(shift_by_vector, x40)
    x42 = transform_and_flatten(x41, x21)
    x43 = paint_onto_grid(x39, x42)
    O = fill(x43, x19, x20)
    return O


def solve_7df24a62(I):
    x1 = get_height(I)
    x2 = get_width(I)
    x3 = of_color(I, COLOR_ONE)
    x4 = of_color(I, COLOR_FOUR)
    x5 = upper_left_corner(x3)
    x6 = smallest_subgrid_containing(x3, I)
    x7 = rot90(x6)
    x8 = rot180(x6)
    x9 = rot270(x6)
    x10 = equals(size, 0)
    x11 = fix_last_argument(of_color, COLOR_ONE)
    x12 = compose(shift_to_origin, x11)
    x13 = fix_last_argument(of_color, COLOR_FOUR)
    x14 = fix_last_argument(shift_by_vector, x5)
    x15 = compose(x14, x13)
    x16 = fix_first_argument(subtract, x1)
    x17 = chain(increment, x16, get_height)
    x18 = fix_first_argument(subtract, x2)
    x19 = chain(increment, x18, get_width)
    x20 = fix_last_argument(interval, 1)
    x21 = fix_first_argument(x20, 0)
    x22 = compose(x21, x17)
    x23 = compose(x21, x19)
    x24 = combine_two_function_results(cartesian_product, x22, x23)
    x25 = fix_last_argument(shift_by_vector, NEG_UNITY)
    x26 = fix_first_argument(fix_first_argument, shift_by_vector)
    x27 = chain(x26, x25, x12)
    #x28 = as_tuple(x6, x7)
    x28 = as_generic_tuple(x6, x7)  # mdda
    #x29 = as_tuple(x8, x9)
    x29 = as_generic_tuple(x8, x9)  # mdda
    x30 = union(x28, x29)
    x31 = transform(x15, x30)
    x32 = fix_first_argument(difference, x4)
    x33 = transform(x32, x31)
    x34 = transform(shift_to_origin, x31)
    x35 = transform(x24, x34)
    x36 = fix_first_argument(fix_last_argument, difference)
    x37 = transform(x26, x34)
    x38 = transform(x36, x33)
    x39 = transform_both(compose, x38, x37)
    x40 = fix_first_argument(compose, x10)
    x41 = transform(x40, x39)
    x42 = transform_both(keep_if_condition, x35, x41)
    x43 = transform(x27, x30)
    x44 = transform_both_and_flatten(transform_and_flatten, x43, x42)
    O = fill(I, COLOR_ONE, x44)
    return O


def solve_f15e1fac(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = is_portrait(x1)
    x3 = condition_if_else(x2, identity, diagonal_mirror)
    x4 = x3(I)
    x5 = leftmost(x1)
    x6 = is_equal(x5, 0)
    x7 = condition_if_else(x6, identity, vertical_mirror)
    x8 = x7(x4)
    x9 = of_color(x8, COLOR_EIGHT)
    x10 = uppermost(x9)
    x11 = is_equal(x10, 0)
    x12 = condition_if_else(x11, identity, horizontal_mirror)
    x13 = x12(x8)
    x14 = of_color(x13, COLOR_EIGHT)
    x15 = of_color(x13, COLOR_TWO)
    x16 = fix_last_argument(shoot, DOWN)
    x17 = transform_and_flatten(x16, x14)
    x18 = get_height(x13)
    x19 = transform(get_first, x15)
    x20 = insert(0, x19)
    x21 = insert(x18, x19)
    x22 = transform(decrement, x21)
    x23 = sort(x20, identity)
    x24 = sort(x22, identity)
    x25 = size(x15)
    x26 = increment(x25)
    x27 = interval(0, x26, 1)
    x28 = transform(to_horizontal_vec, x27)
    x29 = pairwise(x23, x24)
    x30 = fix_first_argument(keep_if_condition, x17)
    x31 = compose(get_first, get_last)
    x32 = chain(decrement, get_first, get_first)
    x33 = combine_two_function_results(greater_than, x31, x32)
    x34 = chain(increment, get_last, get_first)
    x35 = combine_two_function_results(greater_than, x34, x31)
    x36 = combine_two_function_results(logical_and, x33, x35)
    x37 = fix_first_argument(fix_first_argument, as_tuple)
    x38 = fix_first_argument(compose, x36)
    x39 = chain(x30, x38, x37)
    x40 = transform(x39, x29)
    x41 = transform_both(shift_by_vector, x40, x28)
    x42 = flatten(x41)
    x43 = fill(x13, COLOR_EIGHT, x42)
    x44 = chain(x3, x7, x12)
    O = x44(x43)
    return O


def solve_234bbc79(I):
    x1 = as_objects(I, False, False, True)
    x2 = fix_last_argument(get_other, COLOR_FIVE)
    x3 = compose(x2, palette)
    x4 = combine_two_function_results(recolor, x3, identity)
    x5 = transform(x4, x1)
    x6 = sort(x5, leftmost)
    x7 = compose(get_last, get_last)
    x8 = fix_first_argument(equals, x7)
    x9 = compose(x8, leftmost)
    x10 = compose(x8, rightmost)
    x11 = combine_two_function_results(keep_if_condition, identity, x9)
    x12 = combine_two_function_results(keep_if_condition, identity, x10)
    x13 = compose(direct_neighbors, get_last)
    x14 = fix_last_argument(chain, x13)
    x15 = fix_first_argument(x14, size)
    x16 = fix_first_argument(fix_last_argument, intersection)
    x17 = chain(x15, x16, to_indices)
    x18 = combine_two_function_results(argmin, x11, x17)
    x19 = combine_two_function_results(argmin, x12, x17)
    x20 = compose(get_last, x18)
    x21 = compose(get_last, x19)
    #x22 = as_tuple(COLOR_ZERO, DOWN_LEFT)
    x22 = make_cell(COLOR_ZERO, DOWN_LEFT)  # mdda
    x23 = initset(x22)
    x24 = fix_first_argument(add, RIGHT)
    x25 = chain(x20, get_first, get_last)
    x26 = compose(x21, get_first)
    x27 = combine_two_function_results(subtract, x26, x25)
    x28 = compose(get_first, get_last)
    x29 = compose(x24, x27)
    x30 = combine_two_function_results(shift_by_vector, x28, x29)
    x31 = combine_two_function_results(union, get_first, x30)
    x32 = combine_two_function_results(remove, x28, get_last)
    x33 = combine_two_function_results(as_tuple, x31, x32)
    x34 = size(x1)
    x35 = power(x33, x34)
    #x36 = as_tuple(x23, x6)
    x36 = as_generic_tuple(x23, x6) # mdda
    x37 = x35(x36)
    x38 = get_first(x37)
    x39 = get_width(x38)
    x40 = decrement(x39)
    x41 = as_tuple(3, x40)
    x42 = create_grid(COLOR_ZERO, x41)
    O = paint_onto_grid(x42, x38)
    return O


def solve_22233c11(I):
    x1 = as_objects(I, True, True, True)
    x2 = fix_last_argument(upscale, 2)
    x3 = chain(negate, halve, get_shape)
    x4 = combine_two_function_results(union, horizontal_line, vertical_line)
    x5 = compose(x2, vertical_mirror)
    x6 = combine_two_function_results(shift_by_vector, x5, x3)
    x7 = compose(to_indices, x6)
    x8 = fix_first_argument(transform_and_flatten, x4)
    x9 = compose(x8, to_indices)
    x10 = combine_two_function_results(difference, x7, x9)
    x11 = transform_and_flatten(x10, x1)
    O = fill(I, COLOR_EIGHT, x11)
    return O


def solve_2dd70a9a(I):
    x1 = of_color(I, COLOR_TWO)
    x2 = of_color(I, COLOR_THREE)
    x3 = is_vertical_line(x1)
    x4 = is_vertical_line(x2)
    x5 = center(x1)
    x6 = condition_if_else(x4, uppermost, rightmost)
    x7 = x6(x1)
    x8 = x6(x2)
    x9 = greater_than(x7, x8)
    x10 = logical_and(x4, x9)
    x11 = condition_if_else(x10, lowermost, uppermost)
    x12 = x11(x2)
    x13 = condition_if_else(x4, leftmost, rightmost)
    x14 = x13(x2)
    x15 = as_tuple(x12, x14)
    x16 = get_other(x2, x15)
    x17 = subtract(x15, x16)
    x18 = shoot(x15, x17)
    x19 = fill_background(I, COLOR_ONE, x18)
    x20 = as_objects(x19, True, False, False)
    x21 = color_filter(x20, COLOR_ONE)
    x22 = fix_last_argument(adjacent, x2)
    x23 = keep_if_condition(x21, x22)
    x24 = difference(x21, x23)
    x25 = flatten(x24)
    x26 = erase_patch(x19, x25)
    x27 = shoot(x5, DOWN)
    x28 = shoot(x5, UP)
    x29 = shoot(x5, LEFT)
    x30 = shoot(x5, RIGHT)
    x31 = union(x27, x28)
    x32 = union(x29, x30)
    x33 = condition_if_else(x3, x31, x32)
    x34 = of_color(x26, COLOR_ONE)
    x35 = initset(x15)
    x36 = fix_last_argument(manhattan_distance, x35)
    x37 = compose(x36, initset)
    x38 = argmax(x34, x37)
    x39 = initset(x38)
    x40 = move_until_touching(x39, x33)
    x41 = crement(x40)
    x42 = add(x38, x41)
    x43 = line_between(x38, x42)
    x44 = fill(x26, COLOR_ONE, x43)
    x45 = line_between(x42, x5)
    x46 = fill_background(x44, COLOR_ONE, x45)
    O = replace(x46, COLOR_ONE, COLOR_THREE)
    return O


def solve_a64e4611(I):
    x1 = as_indices(I)
    x2 = combine_two_function_results(cartesian_product, identity, identity)
    x3 = fix_first_argument(create_grid, COLOR_ZERO)
    x4 = compose(as_object, x3)
    x5 = combine_two_function_results(multiply, get_first, get_last)
    x6 = compose(is_positive, size)
    x7 = fix_first_argument(fix_first_argument, shift_by_vector)
    x8 = fix_last_argument(combine_two_function_results, x5)
    x9 = fix_first_argument(x8, multiply)
    x10 = fix_first_argument(chain, x6)
    x11 = fix_last_argument(x10, x4)
    x12 = fix_first_argument(fix_first_argument, occurrences)
    x13 = chain(x9, x11, x12)
    x14 = compose(x2, get_first)
    x15 = compose(x13, get_last)
    x16 = combine_two_function_results(argmax, x14, x15)
    x17 = chain(x7, x4, x16)
    x18 = compose(x4, x16)
    x19 = combine_two_function_results(occurrences, get_last, x18)
    x20 = combine_two_function_results(transform_and_flatten, x17, x19)
    x21 = multiply(2, 6)
    x22 = interval(3, x21, 1)
    #x23 = as_tuple(x22, I)
    x23 = as_generic_tuple(x22, I)  # mdda
    x24 = x20(x23)
    x25 = fill(I, COLOR_THREE, x24)
    x26 = interval(3, 10, 1)
    #x27 = as_tuple(x26, x25)
    x27 = as_generic_tuple(x26, x25)  # mdda
    x28 = x20(x27)
    x29 = fill(x25, COLOR_THREE, x28)
    #x30 = as_tuple(x26, x29)
    x30 = as_generic_tuple(x26, x29)  # mdda
    x31 = x20(x30)
    x32 = fill(x29, COLOR_THREE, x31)
    x33 = fix_last_argument(to_object, x32)
    x34 = fix_last_argument(color_count, COLOR_THREE)
    x35 = chain(x34, x33, neighbors)
    x36 = equals(x35, 8)
    x37 = keep_if_condition(x1, x36)
    x38 = fill(I, COLOR_THREE, x37)
    x39 = of_color(x38, COLOR_ZERO)
    x40 = fix_last_argument(bordering, x38)
    x41 = compose(x40, initset)
    x42 = fix_first_argument(contains, COLOR_THREE)
    x43 = fix_last_argument(to_object, x38)
    x44 = chain(x42, palette, x43)
    x45 = compose(x44, direct_neighbors)
    x46 = combine_two_function_results(logical_and, x45, x41)
    x47 = keep_if_condition(x39, x46)
    O = fill(x38, COLOR_THREE, x47)
    return O


def solve_7837ac64(I):
    x1 = partition_only_foreground(I)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = flatten(x3)
    x5 = smallest_subgrid_containing(x4, I)
    x6 = chain(get_color, flatten, solid_color_strips_in_grid)
    x7 = x6(I)
    x8 = as_objects(x5, True, False, False)
    x9 = color_filter(x8, COLOR_ZERO)
    x10 = fix_last_argument(to_object, x5)
    x11 = chain(x10, corner_indices, outbox)
    x12 = fix_first_argument(contains, x7)
    x13 = chain(x12, palette, x11)
    x14 = compose(count_colors, x11)
    x15 = compose(logical_not, x13)
    x16 = equals(x14, 1)
    x17 = combine_two_function_results(logical_and, x15, x16)
    x18 = keep_if_condition(x9, x17)
    x19 = compose(get_color, x11)
    x20 = combine_two_function_results(recolor, x19, identity)
    x21 = transform_and_flatten(x20, x18)
    x22 = paint_onto_grid(x5, x21)
    x23 = get_first(x9)
    x24 = get_height(x23)
    x25 = get_height(x5)
    x26 = increment(x24)
    x27 = interval(0, x25, x26)
    x28 = interval(0, x25, 1)
    x29 = fix_last_argument(contains, x27)
    x30 = chain(logical_not, x29, get_last)
    x31 = fix_first_argument(transform, get_first)
    x32 = fix_last_argument(keep_if_condition, x30)
    x33 = fix_last_argument(pairwise, x28)
    x34 = chain(x31, x32, x33)
    x35 = compose(diagonal_mirror, x34)
    x36 = power(x35, 2)
    x37 = x36(x22)
    O = downscale(x37, x24)
    return O


def solve_a8c38be5(I):
    x1 = replace(I, COLOR_FIVE, COLOR_ZERO)
    x2 = as_objects(x1, True, False, True)
    x3 = transform(shift_to_origin, x2)
    x4 = as_tuple(9, 9)
    x5 = create_grid(COLOR_FIVE, x4)
    x6 = as_indices(x5)
    x7 = box(x6)
    x8 = center(x6)
    x9 = fix_first_argument(contains, 0)
    x10 = fix_last_argument(subtract, x8)
    x11 = compose(x9, x10)
    x12 = chain(outbox, outbox, initset)
    x13 = corner_indices(x6)
    x14 = transform_and_flatten(x12, x13)
    x15 = difference(x7, x14)
    x16 = inbox(x7)
    x17 = keep_if_condition(x16, x11)
    x18 = union(x15, x17)
    x19 = fill(x5, COLOR_ONE, x18)
    x20 = as_objects(x19, True, False, True)
    x21 = transform(to_indices, x20)
    x22 = fix_first_argument(equals, shift_to_origin)
    x23 = fix_first_argument(extract_first_matching, x21)
    x24 = chain(upper_left_corner, x23, x22)
    x25 = compose(x24, to_indices)
    x26 = combine_two_function_results(shift_by_vector, identity, x25)
    x27 = transform_and_flatten(x26, x3)
    O = paint_onto_grid(x5, x27)
    return O


def solve_b775ac94(I):
    x1 = as_objects(I, False, True, True)
    x2 = fix_first_argument(fix_last_argument, is_equal)
    x3 = fix_last_argument(compose, get_first)
    x4 = chain(x3, x2, most_common_color)
    x5 = combine_two_function_results(keep_if_condition, identity, x4)
    x6 = combine_two_function_results(difference, identity, x5)
    x7 = fix_first_argument(fix_last_argument, adjacent)
    x8 = fix_last_argument(compose, initset)
    x9 = chain(x8, x7, x6)
    x10 = combine_two_function_results(extract_first_matching, x5, x9)
    x11 = combine_two_function_results(insert, x10, x6)
    x12 = fix_first_argument(recolor, COLOR_ZERO)
    x13 = chain(x12, bounding_box_delta, x11)
    x14 = combine_two_function_results(union, x11, x13)
    x15 = combine_two_function_results(position, x5, x6)
    x16 = chain(to_vertical_vec, get_first, x15)
    x17 = chain(to_horizontal_vec, get_last, x15)
    x18 = combine_two_function_results(multiply, get_shape, x16)
    x19 = combine_two_function_results(multiply, get_shape, x17)
    x20 = combine_two_function_results(multiply, get_shape, x15)
    x21 = combine_two_function_results(shift_by_vector, horizontal_mirror, x18)
    x22 = combine_two_function_results(shift_by_vector, vertical_mirror, x19)
    x23 = compose(horizontal_mirror, vertical_mirror)
    x24 = combine_two_function_results(shift_by_vector, x23, x20)
    x25 = fix_first_argument(compose, x5)
    x26 = x25(x21)
    x27 = x25(x22)
    x28 = x25(x24)
    x29 = compose(crement, negate)
    x30 = fix_first_argument(compose, x29)
    x31 = x30(x16)
    x32 = x30(x17)
    x33 = x30(x15)
    x34 = combine_two_function_results(shift_by_vector, x26, x31)
    x35 = combine_two_function_results(shift_by_vector, x27, x32)
    x36 = combine_two_function_results(shift_by_vector, x28, x33)
    x37 = fix_first_argument(color_at_location, I)
    x38 = fix_first_argument(compose, to_indices)
    x39 = x38(x14)
    x40 = x38(x34)
    x41 = x38(x35)
    x42 = x38(x36)
    x43 = combine_two_function_results(intersection, x39, x40)
    x44 = combine_two_function_results(intersection, x39, x41)
    x45 = combine_two_function_results(intersection, x39, x42)
    x46 = chain(x37, get_first, x43)
    x47 = chain(x37, get_first, x44)
    x48 = chain(x37, get_first, x45)
    x49 = combine_two_function_results(recolor, x46, x34)
    x50 = combine_two_function_results(recolor, x47, x35)
    x51 = combine_two_function_results(recolor, x48, x36)
    x52 = transform_and_flatten(x49, x1)
    x53 = transform_and_flatten(x50, x1)
    x54 = transform_and_flatten(x51, x1)
    x55 = paint_onto_grid(I, x52)
    x56 = paint_onto_grid(x55, x53)
    O = paint_onto_grid(x56, x54)
    return O


def solve_97a05b5b(I):
    x1 = as_objects(I, False, True, True)
    x2 = argmax(x1, size)
    x3 = smallest_subgrid_containing(x2, I)
    x4 = fix_last_argument(greater_than, 1)
    x5 = compose(x4, count_colors)
    x6 = keep_if_condition(x1, x5)
    x7 = fix_first_argument(fix_last_argument, subtract)
    x8 = switch(x3, COLOR_TWO, COLOR_ZERO)
    x9 = fix_first_argument(occurrences, x8)
    x10 = fix_first_argument(fix_first_argument, shift_by_vector)
    x11 = compose(x7, upper_left_corner)
    x12 = equals(get_first, COLOR_TWO)
    x13 = compose(logical_not, x12)
    x14 = fix_last_argument(keep_if_condition, x12)
    x15 = fix_last_argument(keep_if_condition, x13)
    x16 = fix_first_argument(recolor, COLOR_ZERO)
    x17 = compose(x16, x15)
    x18 = combine_two_function_results(union, x17, x14)
    x19 = chain(x11, x18, shift_to_origin)
    x20 = as_objects(x8, True, True, True)
    x21 = transform(to_indices, x20)
    x22 = chain(x9, x18, shift_to_origin)
    x23 = fix_last_argument(color_count, COLOR_TWO)
    x24 = fix_first_argument(keep_if_condition, x21)
    x25 = chain(size, get_first, x24)
    x26 = compose(is_positive, size)
    x27 = fix_first_argument(fix_first_argument, contains)
    x28 = chain(x26, x24, x27)
    x29 = compose(x25, x27)
    x30 = fix_last_argument(keep_if_condition, x28)
    x31 = compose(x30, x22)
    x32 = fix_first_argument(fix_last_argument, is_equal)
    x33 = fix_last_argument(compose, x29)
    x34 = chain(x33, x32, x23)
    x35 = combine_two_function_results(keep_if_condition, x31, x34)
    x36 = combine_two_function_results(transform, x19, x35)
    x37 = compose(x10, shift_to_origin)
    x38 = combine_two_function_results(transform_and_flatten, x37, x36)
    #x39 = as_tuple(counterdiagonal_mirror, diagonal_mirror)
    x39 = as_generic_tuple(counterdiagonal_mirror, diagonal_mirror)  # mdda
    #x40 = as_tuple(horizontal_mirror, vertical_mirror)
    x40 = as_generic_tuple(horizontal_mirror, vertical_mirror)  # mdda
    x41 = union(x39, x40)
    x42 = cartesian_product(x41, x41)
    x43 = combine_two_function_results(compose, get_first, get_last)
    x44 = transform(x43, x42)
    x45 = fix_first_argument(apply_each_function, x44)
    x46 = transform_and_flatten(x45, x6)
    x47 = transform_and_flatten(x38, x46)
    x48 = paint_onto_grid(x3, x47)
    x49 = palette(x47)
    x50 = fix_first_argument(remove, COLOR_TWO)
    x51 = x50(x49)
    x52 = chain(get_first, x50, palette)
    x53 = fix_last_argument(contains, x51)
    x54 = chain(logical_not, x53, x52)
    x55 = keep_if_condition(x6, x54)
    x56 = combine_two_function_results(transform, x19, x22)
    x57 = combine_two_function_results(transform_and_flatten, x37, x56)
    x58 = transform_and_flatten(x45, x55)
    x59 = transform_and_flatten(x57, x58)
    O = paint_onto_grid(x48, x59)
    return O


def solve_3e980e27(I):
    x1 = as_objects(I, False, True, True)
    x2 = as_tuple(10, 10)
    x3 = negate(x2)
    #x4 = as_tuple(COLOR_TWO, x3)
    x4 = make_cell(COLOR_TWO, x3)
    #x5 = as_tuple(COLOR_THREE, x3)
    x5 = make_cell(COLOR_THREE, x3)
    x6 = initset(x4)
    x7 = insert(x5, x6)
    x8 = insert(x7, x1)
    x9 = fix_first_argument(contains, COLOR_TWO)
    x10 = fix_first_argument(contains, COLOR_THREE)
    x11 = compose(negate, upper_left_corner)
    x12 = fix_first_argument(compose, x11)
    x13 = fix_first_argument(fix_last_argument, keep_if_condition)
    x14 = compose(x12, x13)
    x15 = fix_last_argument(compose, center)
    x16 = fix_first_argument(fix_first_argument, shift_by_vector)
    x17 = x14(x9)
    x18 = x14(x10)
    x19 = combine_two_function_results(shift_by_vector, identity, x17)
    x20 = combine_two_function_results(shift_by_vector, identity, x18)
    x21 = compose(x9, palette)
    x22 = compose(x10, palette)
    x23 = keep_if_condition(x8, x21)
    x24 = argmax(x23, size)
    x25 = remove(x24, x23)
    x26 = vertical_mirror(x24)
    x27 = chain(x15, x16, x19)
    x28 = x27(x26)
    x29 = transform_and_flatten(x28, x25)
    x30 = keep_if_condition(x8, x22)
    x31 = argmax(x30, size)
    x32 = remove(x31, x30)
    x33 = chain(x15, x16, x20)
    x34 = x33(x31)
    x35 = transform_and_flatten(x34, x32)
    x36 = union(x29, x35)
    O = paint_onto_grid(I, x36)
    return O
