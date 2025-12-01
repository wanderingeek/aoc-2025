from enum import Enum
from locale import atoi

# INPUT_FILE = "./day1/test_input.txt"
INPUT_FILE = "./actual_inputs/d1_p1_input.txt"


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


CURRENT_POSITION = 50
ZERO_COUNTER = 0

for instruction in instructions:
    print("Current position is", CURRENT_POSITION)
    print("Current instruction is", instruction)

    direction, steps = interpret_instruction(instruction)
    print("Direction is", direction)
    print("Step count is", steps)

    if direction == Direction.LEFT:
        CURRENT_POSITION -= steps
    else:
        CURRENT_POSITION += steps

    print("PROVISIONAL position is", CURRENT_POSITION)

    # Handle special case of position<0 or >100
    # While loop for handling cases where position has values like -550 or +600
    if (CURRENT_POSITION < 0) or (CURRENT_POSITION > 99):
        # If -2, then real position is 98
        # # If 102, then real position is 2
        CURRENT_POSITION = CURRENT_POSITION % 100
        print("CORRECTED position to", CURRENT_POSITION)

    print("Final CORRECTED Position changed is", CURRENT_POSITION)

    if CURRENT_POSITION == 0:
        ZERO_COUNTER += 1
        print("ZERO POSITION ALERT!")
    print("---- ---- ----")

print("-- DONE EXECUTING INSTRUCTIONS --")

print("The password is", ZERO_COUNTER)
