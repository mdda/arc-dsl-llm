import os
from .arc_types import Color

if 'ARC_DSL_LLM_COLOR_FLIP' in os.environ:
    # This idea doesn't work : Need to change the grid IO values too... 
    #   Therefore : Must do this with a 'higher level' color permutation idea
    COLOR_BELOW: Color = 1009
    COLOR_ZERO: Color = 1010
    COLOR_ONE: Color = 1011
    COLOR_TWO: Color = 1012
    COLOR_THREE: Color = 1013
    COLOR_FOUR: Color = 1014
    COLOR_FIVE: Color = 1015
    COLOR_SIX: Color = 1016
    COLOR_SEVEN: Color = 1017
    COLOR_EIGHT: Color = 1018
    COLOR_NINE: Color = 1019
    #COLOR_TEN: Color = 1020
    COLOR_ABOVE: Color = 1020
else:
    # This is the default behaviour
    COLOR_BELOW: Color = -1
    COLOR_ZERO: Color = 0
    COLOR_ONE: Color = 1
    COLOR_TWO: Color = 2
    COLOR_THREE: Color = 3
    COLOR_FOUR: Color = 4
    COLOR_FIVE: Color = 5
    COLOR_SIX: Color = 6
    COLOR_SEVEN: Color = 7
    COLOR_EIGHT: Color = 8
    COLOR_NINE: Color = 9
    #COLOR_TEN: Color = 10
    COLOR_ABOVE: Color = 10

#F = False
#T = True

NEG_ONE = -1
NEG_TWO = -2

DOWN = (1, 0)
RIGHT = (0, 1)
UP = (-1, 0)
LEFT = (0, -1)

ORIGIN = (0, 0)
UNITY = (1, 1)
NEG_UNITY = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)

ZERO_BY_TWO = (0, 2)
TWO_BY_ZERO = (2, 0)
TWO_BY_TWO = (2, 2)
THREE_BY_THREE = (3, 3)
