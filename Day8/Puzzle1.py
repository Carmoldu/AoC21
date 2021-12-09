with open('input.txt', 'r') as f:
    signals = f.read().splitlines()

outputs = [signal.split('|')[1].lstrip().split(' ') for signal in signals]
print(outputs)

count = 0
for digits in outputs:
    for digit in digits:
        if (len(digit) == 2) | (len(digit) == 3) | (len(digit) == 4) | (len(digit) == 7):
            count += 1

print(count)

