"""
Python Problem-Solving Puzzles
----------------------------
A collection of engaging puzzles that encourage logical thinking and problem-solving.
Each puzzle includes sample inputs and expected outputs to guide students.

Puzzle 1: Shopping List Calculator
--------------------------------
You're helping a local store during a sale. Customers bring items with different
discounts, but they can only choose one discount per item - either the general
store discount or the item's special discount.

Task:
Calculate the minimum possible total after applying the best discounts.

Input Format:
- First line: store_discount (general discount applicable to any item)
- Second line: number of items
- Following lines: item_price special_discount

Example Input:
20
3
100 25
50 10
75 15

Example Output:
175.0

Explanation:
- Item 1: 100 -> Using 25% discount = 75
- Item 2: 50 -> Using 20% store discount = 40
- Item 3: 75 -> Using 20% store discount = 60
Total = 75 + 40 + 60 = 175
"""

"""
Puzzle 2: Movie Night Scheduler
-----------------------------
You're organizing a movie marathon. Each movie has a duration and must be watched
completely within the same day. You need to find how many days you need to watch
all movies if you have limited hours per day.

Task:
Calculate minimum days needed to watch all movies given maximum hours per day.

Input Format:
- First line: max_hours_per_day
- Second line: number_of_movies
- Following lines: movie_duration_in_hours

Example Input:
4
5
2.5
1.5
3
2
1.5

Example Output:
3

Explanation:
Day 1: 2.5 + 1.5 = 4 hours
Day 2: 3 hours
Day 3: 2 + 1.5 = 3.5 hours
"""

"""
Puzzle 3: Pattern Finder
-----------------------
In a grid of numbers, find how many times a specific pattern appears.
The pattern can appear horizontally, vertically, or diagonally.

Task:
Count occurrences of a number pattern in the grid.

Input Format:
- First two lines: grid dimensions (rows columns)
- Following lines: grid numbers
- Last line: pattern to find

Example Input:
4 4
1 2 3 2
2 3 2 1
3 2 1 2
2 1 2 3
2 1 2

Example Output:
4

Explanation:
Pattern "2 1 2" appears:
- Once horizontally (row 3)
- Once vertically (column 1)
- Twice diagonally
"""

"""
Puzzle 4: Package Sorter
-----------------------
At a delivery company, packages need to be sorted based on their weight and
destination. Each delivery truck has a weight limit and can only serve
certain destinations.

Task:
Determine the minimum number of trucks needed to deliver all packages.

Input Format:
- First line: number_of_packages
- Following lines: weight destination
- Last line: weight_limit_per_truck

Example Input:
6
10 North
15 South
8 North
12 South
9 North
11 South
30

Example Output:
3

Explanation:
Truck 1: North (10 + 8 = 18)
Truck 2: North (9) + South (15)
Truck 3: South (12 + 11 = 23)
"""

"""
Puzzle 5: Library Book Arranger
-----------------------------
The library needs to arrange books so that similar books are not too close
together. Books with the same category must be at least 2 shelves apart.

Task:
Determine if it's possible to arrange the books according to the rules.

Input Format:
- First line: number_of_books
- Following lines: book_category
- Last line: number_of_shelves

Example Input:
5
Fiction
Science
Fiction
History
Fiction
3

Example Output:
Impossible

Explanation:
Can't place 3 Fiction books with 2 shelves between each when only 3 shelves available
"""

"""
Puzzle 6: Restaurant Table Optimizer
----------------------------------
A restaurant needs to optimize table assignments for groups of different sizes
to maximize seating efficiency.

Task:
Find the optimal arrangement to seat all waiting groups using available tables.

Input Format:
- First line: number_of_tables
- Second line: table_sizes (separated by spaces)
- Third line: number_of_groups
- Fourth line: group_sizes (separated by spaces)

Example Input:
4
4 6 4 8
3
4 6 2

Example Output:
Possible
Table Assignments:
Group 4 -> Table 1 (4)
Group 6 -> Table 2 (6)
Group 2 -> Table 3 (4)

Explanation:
- All groups can be seated
- One table (size 8) remains empty
- Efficient use of similarly-sized tables

Problem-Solving Tips:
-------------------
1. Break down the problem:
   - Identify the input components
   - List all constraints
   - Determine what makes a valid solution

2. Solve manually first:
   - Try with small examples
   - Find patterns
   - Identify edge cases

3. Plan your approach:
   - Consider different strategies
   - Start with brute force
   - Look for optimization opportunities

4. Test your solution:
   - Use the provided example
   - Create additional test cases
   - Check edge cases
"""