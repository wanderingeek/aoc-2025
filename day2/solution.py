import re

# INPUT_FILE = "./day2/test_input.txt"
INPUT_FILE = "./actual_inputs/d2_input.txt"

# Check for original capture group being repeated twice or more
PART1_REGEX_PATTERN = r"(\d+)\1"
PART2_REGEX_PATTERN = r"(\d+)\1+"


# Function that returns the start and end ids of the id range
def get_range_start_end(id_range: str) -> tuple[int, int]:
    range_start = int(id_range.split("-")[0])
    range_end = int(id_range.split("-")[1])
    return range_start, range_end


# Function to check for invalid numbers for the parts 1 and 2 solution
# Switch regex based on bool flag
def is_id_invalid(id: int, part1: bool = False) -> bool:
    id_str = str(id)

    # We use regular expression to check if a pattern occurs twice in the same string
    regex_pattern = None
    if part1:
        regex_pattern = PART1_REGEX_PATTERN
    else:
        regex_pattern = PART2_REGEX_PATTERN

    # Use re.fullmatch to apply regex pattern to entire string
    regex_match = re.fullmatch(regex_pattern, id_str)

    if regex_match:
        return True

    return False


# List of ranges received from the input file
id_ranges: list[str] = list()
part1_invalid_ids_sum = 0
part2_invalid_ids_sum = 0


# Read all the ranges from the input file
with open(INPUT_FILE) as file_handle:
    # Entire input is one line
    id_ranges = file_handle.read().split(",")

# We have the ranges
# Now lets go through them and sym up the invalid IDs
print("--- ---- ---")
for id_range in id_ranges:
    range_start, range_end = get_range_start_end(id_range)
    # print(f"Range start is {range_start}, Range end is {range_end}")

    ## IMPORTANT INFO for Part 1
    ## looking for any ID which is made only of some sequence of digits repeated twice
    ## Emphasis on ONLY
    ## 13134 is not invalid despite 13 being repeated twice. Becasue there is an extra 4 there.
    ## This is why 101 is a valid ID, despite the 1 being repeated twice.

    for id in range(range_start, range_end + 1):
        id_str = str(id)
        # Part 1
        if is_id_invalid(id, part1=True):
            print("Part 1 Invalid ID =>", id_str)
            part1_invalid_ids_sum += id
        # Part 2
        if is_id_invalid(id, part1=False):
            print("Part 2 Invalid ID =>", id_str)
            part2_invalid_ids_sum += id


print("--- ---- ---")
print("Part 1 Invalid IDs sum is", part1_invalid_ids_sum)
print("Part 2 Invalid IDs sum is", part2_invalid_ids_sum)
print("--- ---- ---")
