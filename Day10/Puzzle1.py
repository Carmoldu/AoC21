with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
illegal_characters_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_closers_points = {')': 1, ']': 2, '}': 3, '>': 4}

corrupt_lines = []
illegal_characters = []
incomplete_lines = []
incomplete_lines_missing_closers = []

for i, line in enumerate(lines):
    cumulative_openers = []

    for character in line:
        if character in brackets.keys():
            cumulative_openers.append(character)
        elif brackets[cumulative_openers[-1]] is character:
            cumulative_openers.pop()
        else:
            corrupt_lines.append(i)
            illegal_characters.append(character)
            break

    if not corrupt_lines or corrupt_lines[-1] != i:
        incomplete_lines.append(i)
        incomplete_lines_missing_closers.append([brackets[opener] for opener in cumulative_openers[::-1]])

score = sum([illegal_characters_points[illegal_character] for illegal_character in illegal_characters])
print(score)
print(incomplete_lines)
print(incomplete_lines_missing_closers)

scores = []
for missing_closers in incomplete_lines_missing_closers:
    score = 0
    for missing_closer in missing_closers:
        score = score * 5 + incomplete_closers_points[missing_closer]
    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
