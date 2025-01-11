# My code generates a Bingo ticket with the following rules:
#
# 1. Each ticket is a 3x9 matrix and contains numbers between 1-90
# 2. Each column has numbers from a specified range such as 1-10, 11-20, 21-30 etc
# 3. 15 numbers from 1-90 are chosen randomly and put into the proper rows and columns based on their specific range and in ascending order from top to bottom
# 4. Columns must have at least one element and at max 3 elements
# 5. Each row cannot have more than 5 elements
# 6. All the numbers 1-90 are used only once in each set of six tickets
import random

def strategy(nums1,num_count):
    """Distribute numbers from nums1 into buckets according to num_count constraints."""
    numbers1 = list(nums1)
    random.shuffle(numbers1)
    buckets = [[] for _ in range(6)]

    for i in range(6):
        if not numbers1:
            break
        number1 = numbers1.pop()
        buckets[i].append(number1)

    while numbers1:
        number1 = numbers1.pop()
        #random.choice(buckets).append(number1)
        total_buckets = [0,1,2,3,4,5]
        available_buckets = []
        for buc in total_buckets:
            if num_count[buc] > 0:
                available_buckets.append(buc)
        temp = random.choice(available_buckets)
        buckets[temp].append(number1)
        num_count[temp] -= 1

    return buckets

num_used = set()
buckets = [[] for _ in range(6)]
nums = [
    range(1, 11), range(11, 21), range(21, 31), range(31, 41),
    range(41, 51), range(51, 61), range(61, 71), range(71, 81), range(81, 91)
]
def rerun():
    """Generate buckets and ensure they meet the validation criteria."""
    buckets = [[] for _ in range(6)]
    num_count = [6, 6, 6, 6, 6, 6]
    nums = [
        range(1, 11), range(11, 21), range(21, 31), range(31, 41),
        range(41, 51), range(51, 61), range(61, 71), range(71, 81), range(81, 91)
    ]
    for i in range(len(nums)):
        buckets_from_strategy = strategy(nums[i],num_count)
        for j in range(len(buckets)):
            buckets[j].extend(buckets_from_strategy[j])
    return buckets

def isvalid(buckets):
    """Validate the generated buckets based on constraints."""
    for bucket in buckets:
        counts = {i: 0 for i in range(9)}
        if len(bucket) == 0:
            return False
        for num in bucket:
            index = (num - 1) // 10
            if index in counts:
                counts[index] += 1
        vals = counts.values()
        max1 = max(vals)
        if max1 > 3:
            print(max1)
            return False
    return True
while(not isvalid(buckets)):
    buckets = rerun()

count = 1
for bucket in buckets:
    bucket.sort()
    print(f"Bucket {count}: {bucket}")
    count += 1


################################################################
def zeroes_col(table, col):
    count = 0
    for row in table:
        if row[col] == 0:
            count += 1
    return count


import random


def create_table(bucket):
    """Create a 3x9 table from the numbers in a bucket."""
    table = [[0 for _ in range(9)] for _ in range(3)]
    for num in bucket:
        col = (num - 1) // 10
        available_rows = []
        for r in range(3):
            if table[r][col] == 0:
                available_rows.append(r)
        row = random.choice(available_rows)
        table[row][col] = num
    return table
def row_size(table):
    l = []
    for row in table:
        row_count = 0
        for num in row:
            if num != 0:
                row_count += 1
        l.append(row_count)
    return l

def col_size(table):
    l = []
    for col_index in range(9):
        col_count = 0
        for row in table:
            if row[col_index] != 0:
                col_count += 1
        l.append(col_count)
    return l

def correct_table(table):
    """Adjust the table so each row contains exactly 5 numbers."""
    while True:
        row_counts = row_size(table)
        # row_counts = [4,5,6]
        # if row_counts == [5,5,5]:
        all_rows_are_5 = True
        for count in row_counts:
            if count != 5:
                all_rows_are_5 = False
                break
        if all_rows_are_5:
            break

        rows_over = []
        for i, count in enumerate(row_counts):
            if count > 5:
                rows_over.append(i)

        rows_under = []
        for i, count in enumerate(row_counts):
            if count < 5:
                rows_under.append(i)

        if rows_over:
            row_from = random.choice(rows_over)
            row_to = random.choice(rows_under)

            for col in range(9):
                if table[row_from][col] != 0:
                    if table[row_to][col] == 0:
                        table[row_to][col] = table[row_from][col]
                        table[row_from][col] = 0
                        break
    return table

def is_valid_table(table):
    """Ensure the table meets constraints: row and column sizes and unique numbers."""
    row_counts = row_size(table)
    col_counts = col_size(table)
    total_count = sum(row_counts)
    used_number = []
    if total_count != 15:
        return False
    for count in row_counts:
        if count != 5:
            return False
    for count in col_counts:
        if count == 0:
            return False
    for row in range(len(table)):
        for col in range(len(table[0])):
            if table[row][col] in used_number:
                pass
    return True
def sort_table(table):
    for col in range(len(table[0])):
        column_values = []

        for row in range(len(table)):
            if table[row][col] != 0:
                column_values.append(table[row][col])

        column_values.sort()
        index = 0
        for row in range(len(table)):
            if table[row][col] != 0:
                table[row][col] = column_values[index]
                index += 1
def print_table(table):
    print("+----+----+----+----+----+----+----+----+----+")
    for row in table:
        row_output = "|"
        for num in row:
            if num != 0:
                row_output += f" {num:2} |"
            else:
                row_output += "    |"
        print(row_output)
        print("+----+----+----+----+----+----+----+----+----+")
def test_buckets(buckets):
    """Generate and print tables for all buckets."""
    for bucket in buckets:
        table = create_table(bucket)
        corrected_table = correct_table(table)
        sort_table(corrected_table)
        print_table(corrected_table)

test_buckets(buckets)
