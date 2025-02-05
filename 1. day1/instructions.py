

# Problem Statement:
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# TODOs:

# Understand the problem and identify edge cases (e.g., no solution, duplicate numbers).

# Implement a brute-force solution (O(n^2) time complexity).

# Optimize the solution using a hash map (O(n) time complexity).

# Test your solution with custom inputs.


# ________________________________________________________________________________

# Critical Thinking Questions:

# What happens if there are multiple pairs that sum to the target?

# How would you handle negative numbers in the array?








# ------------------------------------------------------------------------------
# Two Sum Problem Implementation Guide
#
# Problem Statement:
# ------------------
# Given an array of integers 'nums' and an integer 'target', return the indices
# of the two numbers such that they add up to target.
#
# Example:
#   Input: nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9
#
# ------------------------------------------------------------------------------
#
# TODOs:
#   [ ] Understand the problem and identify edge cases:
#         - No solution exists.
#         - Duplicate numbers.
#
#   [ ] Implement a brute-force solution (O(n^2) time complexity):
#         - Use two nested loops to check every pair.
#
#   [ ] Optimize the solution using a hash map (O(n) time complexity):
#         - Iterate through the array and use a dictionary to store seen numbers.
#
#   [ ] Test your solution with custom inputs.
#
# ------------------------------------------------------------------------------
#
# Critical Thinking Questions:
# -----------------------------
#   1. What happens if there are multiple pairs that sum to the target?
#      - Consider how the function should behave (return the first found pair or all pairs).
#
#   2. How would you handle negative numbers in the array?
#      - Ensure that the algorithm treats negative numbers correctly.
#
# ------------------------------------------------------------------------------




# ------------------------------------------------------------------------------
# Two Sum Problem Implementation Guide with Time Complexity Explanation
#
# Problem Statement:
# ------------------
# Given an array of integers 'nums' and an integer 'target', return the indices
# of the two numbers such that they add up to target.
#
# Example:
#   Input: nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9
#
# ------------------------------------------------------------------------------
#
# Time Complexity Explained:
# --------------------------
# Time complexity tells us how the running time of an algorithm changes with
# respect to the input size (n). It gives an idea of the efficiency.
#
# 1. Brute-Force Approach:
#    - Uses two nested loops to check every possible pair of numbers.
#    - The outer loop runs n times and for each iteration, the inner loop runs 
#      roughly n times, leading to about n * n iterations.
#    - Time Complexity: O(n^2)
#
# 2. Optimized Hash Map Approach:
#    - Uses a dictionary (hash map) to store numbers and their indices.
#    - In a single pass through the list, for each element, it checks if the
#      complement (target - current number) is in the dictionary.
#    - Dictionary lookups in Python are generally O(1) on average.
#    - Time Complexity: O(n)
#
# ------------------------------------------------------------------------------
#
# Additional Terms Explained:
# ---------------------------
# - **Big O Notation (e.g., O(n), O(n^2)):** A way to describe the performance 
#   or complexity of an algorithm in terms of input size.
#
# - **Hash Map / Dictionary:** A data structure that stores key-value pairs.
#   In Python, dictionaries are used, and they allow for very fast lookups.
#
# ------------------------------------------------------------------------------
#
# TODOs:
#   [ ] Understand the problem and identify edge cases:
#         - No solution exists.
#         - Duplicate numbers.
#
#   [ ] Implement a brute-force solution (O(n^2) time complexity).
#
#   [ ] Optimize the solution using a hash map (O(n) time complexity).
#
#   [ ] Test your solution with custom inputs.
#
# ------------------------------------------------------------------------------
#
# Critical Thinking Questions:
# -----------------------------
#   1. What happens if there are multiple pairs that sum to the target?
#      - Should the function return the first found pair or all pairs?
#
#   2. How would you handle negative numbers in the array?
#      - Make sure the algorithm treats negative numbers correctl