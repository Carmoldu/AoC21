with open('input.txt', 'r') as f:
    diagnostic_report = f.read().splitlines()
print(diagnostic_report)


def evaluate(reports, condition):
    not_found = True
    current_bit = 0

    outcome = reports
    while not_found:
        ones = 0
        for report in outcome:
            ones += int(report[current_bit])

        zeros = len(outcome) - ones

        if condition == 'most common bit':
            condition_result = 1 if ones >= zeros else 0
        else:
            condition_result = 0 if ones >= zeros else 1

        outcome = [report for report in outcome if int(report[current_bit]) == condition_result]

        if len(outcome) == 1:
            not_found = False

        current_bit += 1
    return outcome[0]


oxygen_generator_rating = evaluate(diagnostic_report, 'most common bit')
CO2_scrubber_rating = evaluate(diagnostic_report, 'least common bit')

oxygen_generator_rating = int("".join(oxygen_generator_rating), 2)
CO2_scrubber_rating = int("".join(CO2_scrubber_rating), 2)

print(oxygen_generator_rating * CO2_scrubber_rating)