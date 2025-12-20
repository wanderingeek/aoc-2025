from functools import reduce


# Implement Monotonic stack idea. Courtesy: Gemini 3 Flash
def get_max_joltage(battery_bank: list[int]) -> int:
    max_joltage_number = -1

    # No of elements in list
    n = len(battery_bank)
    # Target length of subsequence
    k = 12
    # max discards aka stack pops at any given time
    max_discards = n - k

    print("Battery Bank =>", battery_bank)

    monotonic_stack = []
    for i in range(n):
        # Check we still have discards left and if stack is non-empty(for popping)
        # and most importantly, check if stack top <= digit we encountered
        print("Digit", battery_bank[i])
        # print("Monotonic Stack=>", monotonic_stack)
        # print("Max Discards=>", max_discards)
        while (
            max_discards > 0
            and monotonic_stack
            and monotonic_stack[-1] < battery_bank[i]
        ):
            print("Popping", monotonic_stack[-1], "from stack")
            monotonic_stack.pop()
            max_discards -= 1
            print("Monotonic Stack=>", monotonic_stack)
            print("Max Discards=>", max_discards)
        # Add the new digit to the stack
        print("Adding", battery_bank[i], "to stack")
        monotonic_stack.append(battery_bank[i])
        print("Monotonic Stack=>", monotonic_stack)
        print("Max Discards=>", max_discards)

        # Sequence length reached. Check if the joltage is highee than max joltage number
        if len(monotonic_stack) == k:
            print("Monotonic Stack length is k=", k)
            joltage_number = reduce(
                lambda accumulator, battery_bank_digit: 10 * accumulator
                + battery_bank_digit,
                monotonic_stack,
            )
            if joltage_number > max_joltage_number:
                print("Setting new MAX JOLTAGE =>", joltage_number)
                max_joltage_number = joltage_number

            # Below part not necessary
            # print(
            #     "Monotic stack length k=",
            #     k,
            #     "so popping",
            #     monotonic_stack[-1],
            #     "from stack",
            # )
            # monotonic_stack.pop()
            # max_discards = min(max_discards + 1, n - k)
            # print("Monotonic Stack=>", monotonic_stack)
            # print("Max Discards=>", max_discards)

    return max_joltage_number


battery_banks = []

# INPUT_FILE = "./day3/test_input.txt"
INPUT_FILE = "./actual_inputs/d3_input.txt"

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
# We find the best sub-sequence of length 12 from the given list
# for which itertools.combinations is perfect

print("---- PART 2 BEGINS ----")

part2_total_output_joltage = 0
max_joltage_list = []

for battery_bank in battery_banks:
    max_joltage = get_max_joltage(battery_bank)
    print("Max joltage for battery bank", battery_bank, "is", max_joltage)
    max_joltage_list.append(max_joltage)

part2_total_output_joltage = sum(max_joltage_list)

print("Part 2 Total Output Joltage =>", part2_total_output_joltage)

print("---- PART 2 ENDS ----")


# # Combination brute-force logic. TOO SLOW!
# for battery_bank in battery_banks:
#     # Get all possible 12-digit combinations
#     max_joltage_number = -1

#     # Below statement will cause OOM issues
#     # joltage_12_combo_list = list(combinations(battery_bank, 12))
#     # Use it as a generator instead and check them one by one and avoid OOM issues
#     print("Checking combos for battery bank", battery_bank)
#     for joltage_12_combo in combinations(battery_bank, 12):
#         # convert each digit into str, concatenate to a string
#         # and then convert to an integer and append to the list

#         # Below is not very efficient
#         # joltage_number = int("".join([str(x) for x in joltage_12_combo]))
#         # More efficient way of doing this. Thanks Gemini
#         joltage_number = reduce(
#             lambda accumulator, battery_bank_digit: 10 * accumulator
#             + battery_bank_digit,
#             joltage_12_combo,
#         )

#         if joltage_number > max_joltage_number:
#             # print(
#             #     "Joltage number",
#             #     joltage_number,
#             #     "is bigger than max",
#             #     max_joltage_number,
#             #     ". Setting NEW MAX JOLTAGE",
#             # )
#             max_joltage_number = joltage_number
#         # else:
#         #     print(
#         #         "Joltage number",
#         #         joltage_number,
#         #         "not bigger than max",
#         #         max_joltage_number,
#         #     )

#     print(
#         "For battery bank",
#         battery_bank,
#         "the max joltage is",
#         max_joltage_number,
#     )
#     part2_total_output_joltage += max_joltage_number
