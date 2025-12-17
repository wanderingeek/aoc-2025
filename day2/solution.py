## IMPORTANT INFO
## looking for any ID which is made only of some sequence of digits repeated twice
## Emphasis on ONLY
## 13134 is not invalid despite 13 being repeated twice. Becasue there is an extra 4 there.
## This is why 101 is a valid ID, despite the 1 being repeated twice.

# Ignore all numbers whose string lengths are odd

# INPUT_FILE = "./day2/test_input.txt"
INPUT_FILE = "./actual_inputs/d2_input.txt"


# Function that returns the start and end ids of the id range
def get_start_end_range(id_range: str) -> tuple[int, int]:
    range_start = int(id_range.split("-")[0])
    range_end = int(id_range.split("-")[1])
    return range_start, range_end


# List of ranges received from the input file
id_ranges: list[str] = list()
invalid_ids_sum = 0

# Read all the ranges from the input file
with open(INPUT_FILE) as file_handle:
    # Entire input is one line
    id_ranges = file_handle.read().split(",")

# We have the ranges
# Now lets go through them and sym up the invalid IDs
print("--- ---- ---")
for id_range in id_ranges:
    range_start, range_end = get_start_end_range(id_range)
    print(f"Range start is {range_start}, Range end is {range_end}")

    for id in range(range_start, range_end + 1):
        id_str = str(id)

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
            print("Invalid ID detected =>", id_str)
            invalid_ids_sum += id

print("--- ---- ---")
print("Invalid IDs sum is", invalid_ids_sum)
print("--- ---- ---")
