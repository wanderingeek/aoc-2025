from functools import reduce
from itertools import combinations
from multiprocessing import Pool
from os import cpu_count


def get_max_joltage(battery_bank: list[int]) -> int:
    # Get all possible 12-digit combinations
    max_joltage_number = -1

    # Below statement will cause OOM issues
    # joltage_12_combo_list = list(combinations(battery_bank, 12))
    # Use it as a generator instead and check them one by one and avoid OOM issues
    print("Checking combos for battery bank", battery_bank)
    for joltage_12_combo in combinations(battery_bank, 12):
        # convert each digit into str, concatenate to a string
        # and then convert to an integer and append to the list

        # Below is not very efficient
        # joltage_number = int("".join([str(x) for x in joltage_12_combo]))
        # More efficient way of doing this. Thanks Gemini
        joltage_number = reduce(
            lambda accumulator, battery_bank_digit: 10 * accumulator
            + battery_bank_digit,
            joltage_12_combo,
        )

        if joltage_number > max_joltage_number:
            # print(
            #     "Joltage number",
            #     joltage_number,
            #     "is bigger than max",
            #     max_joltage_number,
            #     ". Setting NEW MAX JOLTAGE",
            # )
            max_joltage_number = joltage_number
        # else:
        #     print(
        #         "Joltage number",
        #         joltage_number,
        #         "not bigger than max",
        #         max_joltage_number,
        #     )

    print(
        "For battery bank",
        battery_bank,
        "the max joltage is",
        max_joltage_number,
    )
    return max_joltage_number


# Since we are using multiprocessing pools
if __name__ == "__main__":
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
    # We find the best sub-sequence of length 12 from the given list
    # for which itertools.combinations is perfect

    print("---- PART 2 BEGINS ----")

    # Implement multiprocessing to make this faster

    # Use total threads - 2. Leave 2 threads for the OS
    # Make sure there is at least one worker
    system_cpu_count = cpu_count()
    num_workers = 1
    if system_cpu_count is not None:
        num_workers = max(1, system_cpu_count - 2)

    part2_total_output_joltage = 0

    with Pool(num_workers) as pool:
        max_joltage_list = pool.map(get_max_joltage, battery_banks)

    part2_total_output_joltage = sum(max_joltage_list)

    print("Part 2 Total Output Joltage =>", part2_total_output_joltage)

    print("---- PART 2 ENDS ----")


# # Multiprocessing?
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
