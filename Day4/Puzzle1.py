import numpy as np

with open('numbers_drawn.txt', 'r') as f:
    numbers_drawn = f.read().split(',')
numbers_drawn = [int(number) for number in numbers_drawn]

with open('tables.txt', 'r') as f:
    tables = f.read()
print(tables)
print(tables.split('\n\n'))


class Table:
    def __init__(self, table_values: np.array):
        self._values = table_values
        self._numbers_drawn = np.zeros(self._values.shape)

    def check_drawn_number(self, number):
        index = np.where(self._values == number)
        self._numbers_drawn[index] = 1

    def check_table_won(self):
        column_sum = np.sum(self._numbers_drawn, axis=0)
        row_sum = np.sum(self._numbers_drawn, axis=1)

        return (np.where(column_sum == 5)[0].size != 0) or (np.where(row_sum == 5)[0].size != 0)

    def compute_score(self, number):
        score = np.sum(self._values[np.where(self._numbers_drawn == 0)])
        score = score * number
        return score


def table_parser(tables_string: str):
    tables = []
    for table_string in tables_string.split('\n\n'):
        table = []
        for line in table_string.split('\n'):
            line = line.replace('  ', ' ').lstrip()
            table.append([int(number) for number in line.split(' ')])

        tables.append(Table(np.array([np.array(xi) for xi in table])))

    return tables


tables_list = table_parser(tables)


def get_first_winning_score(numbers_drawn, tables_list):
    for number_drawn in numbers_drawn:
        for table in tables_list:
            table.check_drawn_number(number_drawn)
            if table.check_table_won():
                return table.compute_score(number_drawn)


print(get_first_winning_score(numbers_drawn, tables_list))


def get_last_winning_score(numbers_drawn, tables_list):
    score = 0
    for number_drawn in numbers_drawn:
        tables_to_remove = []
        for table in tables_list:
            table.check_drawn_number(number_drawn)
            if table.check_table_won():
                score = table.compute_score(number_drawn)
                tables_to_remove.append(table)

        for table in tables_to_remove:
            tables_list.remove(table)

    return score

print(get_last_winning_score(numbers_drawn, tables_list))