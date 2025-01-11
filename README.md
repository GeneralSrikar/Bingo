Bingo Ticket Generator

This repository contains a Python program that generates Bingo tickets based on specific rules and constraints. Each ticket is represented as a 3x9 matrix, with the following key features:

Key Features:

3x9 Matrix: Each ticket contains 3 rows and 9 columns, with numbers between 1 and 90.

Column Range: Numbers are grouped into columns based on specified ranges, such as 1-10, 11-20, 21-30, etc.

Random Distribution: 15 numbers are randomly selected from the range 1-90 and placed in the correct rows and columns. 

Numbers are sorted in ascending order within each column.

Column Constraints: Each column must have at least one and no more than three numbers.

Row Constraints: Each row cannot have more than five numbers.

Unique Numbers: All numbers between 1-90 are used only once in a set of six tickets.

How It Works:

Buckets: The program distributes the 15 randomly selected numbers into six "buckets", ensuring they meet the column and row constraints.

Table Generation: It generates a 3x9 table and places the numbers based on the constraints.

Validation: After generating the tables, the program checks that all constraints are satisfied, adjusting the table as necessary.

Final Output: The valid Bingo tickets are displayed in a neatly formatted table with numbers sorted within each column.

