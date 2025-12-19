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
