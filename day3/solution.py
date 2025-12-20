from functools import reduce
from itertools import combinations

battery_banks = []

INPUT_FILE = "./day3/test_input.txt"
# INPUT_FILE = "./actual_inputs/d3_input.txt"

with open(INPUT_FILE) as file_handle:
    for line in file_handle:
        battery_bank = []
        for num_char in list(line.strip()):
            battery_bank.append(int(num_char))
        battery_banks.append(battery_bank)

# print(battery_banks)

total_output_joltage = 0

for battery_bank in battery_banks:
    # This is how we'll go about this
    # To get the max battery joltage possible
    # we take each battery joltage in the list, and then get the max joltage of all the batteries that come after it
    # And then we combine these two numbers and get the max joltage for that battery bank

    # Max joltage for current battery bank
    max_joltage = 0
    for i in range(len(battery_bank) - 1):
        max_joltage = max(
            10 * battery_bank[i] + max(battery_bank[i + 1 :]), max_joltage
        )
    total_output_joltage += max_joltage

print("Part 1 Total Output Joltage =>", total_output_joltage)


# Part 2 is essentially finding the best 12-sequence Combination
# Like from Permutations and Combinations.
# In combinations, the order of selection matters
# which is perfect for us

print("---- PART 2 BEGINS ----")

part2_total_output_joltage = 0

# TODO: Multithreading?
for battery_bank in battery_banks:
    # Get all possible 12-digit combinations
    max_joltage_number = -1

    # Below statement will cause OOM issues
    # joltage_12_combo_list = list(combinations(battery_bank, 12))
    # Use it as a generator instead and check them one by one and avoid OOM issues
    for joltage_12_combo in combinations(battery_bank, 12):
        # convert each digit into str, concatenate to a string
        # and then convert to an integer and append to the list

        # Below is not very efficient
        # joltage_number = int("".join([str(x) for x in joltage_12_combo]))
        # More efficient way of doing this. Thanks Gemini
        joltage_number = reduce(
            lambda accumulator, battery_joltage_digit: 10 * accumulator
            + battery_joltage_digit,
            joltage_12_combo,
        )

        if joltage_number > max_joltage_number:
            max_joltage_number = joltage_number

    print(
        "For battery bank",
        battery_bank,
        "the max joltage is",
        max_joltage_number,
    )
    part2_total_output_joltage += max_joltage_number

print("Part 2 Total Output Joltage =>", part2_total_output_joltage)

print("---- PART 2 ENDS ----")
