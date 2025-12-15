from enum import Enum
from locale import atoi

# INPUT_FILE = "./day1/test_input.txt"
INPUT_FILE = "./actual_inputs/d1_input.txt"


# Enum class to represent direction
class Direction(Enum):
    LEFT = 1
    RIGHT = 2


# Function to interpret the direction
def interpret_instruction(instruction: str) -> tuple[Direction, int]:
    direction_char = instruction[0]
    steps = atoi(instruction[1:])

    direction = None

    if direction_char == "L":
        direction = Direction.LEFT
    else:
        direction = Direction.RIGHT

    return (direction, steps)


# Read and store instructions
instructions = []
print("-- STARTING PROGRAM --")
print("-- READING AND STORING INSTRUCTIONS --")
with open(INPUT_FILE) as file_handle:
    for line in file_handle:
        instructions.append(line.strip())

file_handle.close()
# print(instructions)
print("-- DONE STORING INSTRUCTIONS --")

PREV_POSITION = 0
CURRENT_POSITION = 50
ZERO_POSITION_COUNTER = 0
ZERO_POINTED_COUNTER = 0  # For Part 2

print("---- ---- ----")
for instruction in instructions:
    print("Current position is", CURRENT_POSITION)
    print("Current instruction is", instruction)

    direction, steps = interpret_instruction(instruction)
    # print("Direction is", direction)
    # print("Step count is", steps)

    PREV_POSITION = CURRENT_POSITION

    if direction == Direction.LEFT:
        CURRENT_POSITION -= steps
    else:
        CURRENT_POSITION += steps

    print("PROVISIONAL position is", CURRENT_POSITION)

    # Part 2 solution
    # Check for number of times pointer pointed at zero here
    # Taking a 100 steps always ends with the dial pointing at 0 at least once
    ZERO_POINTED_COUNTER += steps // 100

    steps_modulo_100 = steps % 100
    # Handle cases where step count<100 but zero was pointed at
    # If PREV_POSITION=0, PREV_POSITION + steps_modulo_100 will never result in anything > 100
    # Also, when PREV_POSITION=0, PREV_POSITION - steps_modulo_100 won't cross -100
    # So no need to run this block when PREV_POSITION=0
    if steps_modulo_100 > 0 and PREV_POSITION != 0:
        if direction == Direction.LEFT and (PREV_POSITION - steps_modulo_100) <= 0:
            ZERO_POINTED_COUNTER += 1
        elif direction == Direction.RIGHT and (PREV_POSITION + steps_modulo_100) >= 100:
            ZERO_POINTED_COUNTER += 1

    # If -2 / -602, then real position is 98
    # If 102 / 502, then real position is 2
    CURRENT_POSITION = CURRENT_POSITION % 100
    # print("CORRECTED position to", CURRENT_POSITION)

    print("Final CORRECTED Position changed is", CURRENT_POSITION)
    print("Zero Pointed Counter now at", ZERO_POINTED_COUNTER)

    # Part 1 Solution
    if CURRENT_POSITION == 0:
        ZERO_POSITION_COUNTER += 1
        print("ZERO POSITION ALERT!")
    print("---- ---- ----")

print("-- DONE EXECUTING INSTRUCTIONS --")

print("The password for PART 1 is", ZERO_POSITION_COUNTER)
print("The password for PART 2 is", ZERO_POINTED_COUNTER)
