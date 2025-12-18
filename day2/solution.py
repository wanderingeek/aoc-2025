import re

INPUT_FILE = "./day2/test_input.txt"
# INPUT_FILE = "./actual_inputs/d2_input.txt"


# Function that returns the start and end ids of the id range
def get_start_end_range(id_range: str) -> tuple[int, int]:
    range_start = int(id_range.split("-")[0])
    range_end = int(id_range.split("-")[1])
    return range_start, range_end


# Function to check for invalid numbers for the part 2 solution
def check_part2_invalid(id: int) -> bool:
    id_str = str(id)

    # We use regular expression to check if a pattern occurs twice in the same string
    # Length of original sequence ranges from 1 to len(id)/2
    for sequence_length in range(1, len(id_str) // 2 + 1):
        sequence = id_str[:sequence_length]

        # \1+ is the key here - Capture group matched one or more times.
        # And the entire string comprised just of these
        regex_pattern = r"(\d{" + str(sequence_length) + r"})\1+"

        print("Regex pattern is", regex_pattern)

        # Now we check to see if there is a full match
        if re.fullmatch(regex_pattern, id_str):
            print(
                "Full pattern match CONFIRMED for sequence", sequence, "in id", id_str
            )
            return True
        else:
            print("Pattern match failed for sequence", sequence, "in id", id_str)
            continue

    return False


# List of ranges received from the input file
id_ranges: list[str] = list()
invalid_ids_sum = 0
part2_invalid_ids_sum = 0


# Read all the ranges from the input file
with open(INPUT_FILE) as file_handle:
    # Entire input is one line
    id_ranges = file_handle.read().split(",")

# We have the ranges
# Now lets go through them and sym up the invalid IDs
print("--- ---- ---")
for id_range in id_ranges:
    range_start, range_end = get_start_end_range(id_range)
    # print(f"Range start is {range_start}, Range end is {range_end}")

    ## IMPORTANT INFO for Part 1
    ## looking for any ID which is made only of some sequence of digits repeated twice
    ## Emphasis on ONLY
    ## 13134 is not invalid despite 13 being repeated twice. Becasue there is an extra 4 there.
    ## This is why 101 is a valid ID, despite the 1 being repeated twice.

    for id in range(range_start, range_end + 1):
        id_str = str(id)

        ## For Part 2
        print("Starting Part 2 check for id", id)
        if check_part2_invalid(id):
            part2_invalid_ids_sum += id

        # If id length is odd, then ignore and continue, as its valid
        if len(id_str) % 2 != 0:
            continue

        # Split the string into two equal parts and compare them to each other
        # If they are the same then its an invalid ID
        split_index = int(len(id_str) / 2)
        first_half = id_str[:split_index]
        second_half = id_str[split_index:]

        # Use string comparison to check if first half identical to second half
        if first_half == second_half:
            print("Part 1 Invalid ID detected =>", id_str)
            invalid_ids_sum += id

print("--- ---- ---")
print("Invalid IDs sum is", invalid_ids_sum)
print("Part 2 Invalid IDs sum is", part2_invalid_ids_sum)
print("--- ---- ---")
