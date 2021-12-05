with open('input.txt', 'r') as f:
    diagnostic_report = f.read().splitlines()
print(diagnostic_report)

gamma_rate = ''
epsilon_rate = ''

ones_count = [0] * len(diagnostic_report[0])

for report in diagnostic_report:
    for i, bit in enumerate(report):
        if bit == "1":
            ones_count[i] += 1

most_common_bit = ['1' if num_ones > len(diagnostic_report)/2 else '0' for num_ones in ones_count]
least_common_bit = ['0' if num == '1' else '1' for num in most_common_bit]

most_common_bit_out = int("".join(most_common_bit), 2)
least_common_bit_out = int("".join(least_common_bit), 2)

print(most_common_bit_out * least_common_bit_out)