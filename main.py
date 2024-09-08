#Q:1 SUM OF ALL NATURAL NUMBER

# a = int(input("enter number "))
# sum =0
# for i in range(a+1):
#     sum += i
# print(sum)    

# Q: 2 SUM OF DIGITS OF A NUMBER:

# n= input("enter a number ")
# sum =0
# for i in n:
#     sum += int(i)
# print(sum)


# Q 3: NUMBER OF DIGIT IN A NUMBER

# n =input("enter number ")
# print(len(n))

# Q 4: CHECK PALINDROME

# n = input("enter number ")
# a =n[::-1]
# print(a)

# if n ==a:
#     print('palindrome')
# else:
#     print("not a palindrome")    


# Q 5: FIBONACCI SERIES
# def fibonacci(n):
#     fibo =[0,1]

#     for i in range(2, n+1):
#         fibo.append(fibo[-1] + fibo[-2])
#     return fibo[:n]
# print(fibonacci(10))
# 
# 
# // Q 6: MISSING NUMBER IN THE [0, N]


# a =[0,3,1]
# print(a)
# for i in range(max(a)+1):
#     if i not in a:
#         print(i)    


#Q 7 : SORTING ARRAY
# a =[1,3,5,2,0,9,7,-2]
# b =sorted(a, reverse=True)
# print(b)

#Q 8: REVERSE ARRAY

# a =[1,3,5,2,0,9,7,-2]
# print(a[::-1])

#q 9: Palindromic array

# arr=[110,222,121,13]
# def PalinArray(arr):
#     # Code here
#     def is_palindrome(n):
#         return str(n)==str(n)[::-1]
    
#     for i in arr:
#         if not is_palindrome(i):
#             return False
#     return True    
# print(PalinArray(arr)) 


#Q 10: STRING PROBLEMS

# write a function to find the longest common prefix string amongest an array of strings. if there is no common prefix, return an empty string.

# arr =['flow', 'flower', 'float', 'flight','f','a']
# b=len(arr)
# def find_longest_common_prefix(arr):
#     if len(arr)==0:
#         return ""
#     prefix=arr[0]
#     for i in range(1, b):
#         if prefix not in arr[i]:
#             prefix=prefix[0:len(prefix)-1]

#             if len(prefix)==0:
#                 return ""
#     return prefix  

# print(find_longest_common_prefix(arr))      


# seconds ways

# def find_longest_common_prefix(arr):
#     if not arr:
#         return ""

#     # Start with the first string as the prefix
#     prefix = arr[0]

#     for i in range(1, len(arr)):
#         # Compare the prefix with the next string
#         while arr[i].find(prefix) != 0:
#             # Reduce the prefix by one character each time a mismatch is found
#             prefix = prefix[:-1]
#             # If the prefix becomes empty, return an empty string
#             if not prefix:
#                 return ""

#     return prefix

# arr = ['flow', 'flower', 'float', 'flight']
# print(find_longest_common_prefix(arr))



#                 

# Q 11: FIZZBUZZ PROBLEM

# n=100
# for i in range(1, n+1):
#     if i % 3 ==0 and i % 5 ==0:
#         print('FizzBuzz')
#     elif i % 3 ==0:
#         print("Fizz")   
#     elif i % 5 ==0:
#         print('Buzz')
#     else:
#         print(i)       




# Q 12: LONGEST REPEATING CHARACTER REPLACEMENT:
# STATEMENT:  YOU ARE GIVEN A STRING S AND INTEGER K. YOU CAN CHOOSE ANY CHARACTER OF THE STRING AND CHNAGE IT TO ANY OTHER UPPERCASE ENGLISH CHARACTER. YOU CAN PERFORM THIS OPERATIONS ATMOST K TIMES.RETURN THE LENGTH OF THE LONGEST SUBSTRING CONTAINING THE SAME LETTER YOU CAN GET AFTER PERFORMING THE ABOVE OPERATIONS.

# def characterReplacement(s: str, k: int) -> int:
#     count = {}
#     max_len = 0
#     max_count = 0
#     left = 0

#     for right in range(len(s)):
#         count[s[right]] = count.get(s[right], 0) + 1
#         max_count = max(max_count, count[s[right]])

#         if (right - left + 1) - max_count > k:
#             count[s[left]] -= 1
#             left += 1

#         max_len = max(max_len, right - left + 1)

#     return max_len

# # Example usage:
# s = "AABABBA"
# k = 1
# print(characterReplacement(s, k))  # Output: 4





# Q 13: You are given an array of integers i which each subsewuesnt value is not less than the previous value. write function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

# arr =[-3, -1, 0, 2, 3, 5, 6]
# arr =[]

# new_arr =[]
# for i in arr:
#     new_arr.append(abs(i))

# new_arr =sorted(new_arr)
# squared_array =[i**2 for i in new_arr]
# print(new_arr)
# print(squared_array)

# SECOND WAYS:
# def sorted_array(array):
#     a =[]
#     if len(array) ==0:
#         return []
#     else:
#         for i in array:
#             a.append(i**2)
#         return sorted(a)
# print(sorted_array(arr))    

# THIRD WAYS:
# arr =[-3, -1, 0, 2, 3, 5, 6]
# def sorted_array(array):
#     n =len(array)
#     i, j =0, n-1
#     new_array =[0]*n
#     for k in reversed(range(n)):
#         if array[i]**2 > array[j]**2:
#             new_array[k]=array[i]**2
#             i +=1
#         else:
#             new_array[k] = array[j]**2
#             j -=1
#     return new_array
# print(sorted_array(arr))            






#  Q 14:  give an array , return true  if it is either monotone increasing or monotone decreasing.
# arr1 =[]
# arr2 =[1]
# arr3 =[1,1,1]
# arr4 =[-2,4,6,7,7]
# arr5 =[1,4,3,5]

# def check_monotonous(array):
#     if len(array) == 0 or len(array) == 1:
#         return True

#     monotonic_incr = True
#     monotonic_decr = True

#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             monotonic_incr = False
#         if array[i] < array[i + 1]:
#             monotonic_decr = False

#     return monotonic_incr or monotonic_decr

# # Test with an example array

# print(check_monotonous(arr5))  # Output will be True for a monotonically increasing array






# Q 15: K-TH SYMBOL IN GRAMMER:
#  We build a table of n rows(1-indexed). We start by writing 0 in the 1st row. Npw in every subsequent row, we look at the previous row and replace each occurance of 0 with 01, and each of 1 with 10.
# example for n=3, the first row is 0, second row is 01, third row is 0110.
#  Given two integer n, k, return the kth(1-indexed) symbol in the nth row of a table of n rows.

#  TC OF BELOW APPROACH IS: O(n)
# SC OF BELOW APPROACH IS : O(n) due to recursive call stack.
# def kth_symbol(n, k):
#     if n==1:
#         return 0
#     length_of_prev_row =2**(n-2)
#     if k<=length_of_prev_row:
#         return kth_symbol(n-1, k)
#     else:
#         return 1-kth_symbol(n-1,k-length_of_prev_row)



# Q 16:     JOSEPHUS PROBLEM:

# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend. The rules of the game are as follows: Start at the 1st friend. Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once. The last friend you counted leaves the circle and loses the game. If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat. Else, the last friend in the circle wins the game. Given the number of friends, n, and an integer k, return the winner of the game

# def findTheWinner(n, k):
#     a =[i+1 for i in range(n)]

#     def helper(a):
#         if(len(a)== 1):
#             return a[0]
#         remove_index =(k-1)%len(a)
#         del a[remove_index]
#         a = a[remove_index:] + a[:remove_index]
#         return helper(a)
#     return helper(a) 
# print(findTheWinner(5, 3))   

 # METHOD 2
# def findTheWinner(n, k):
#     def helper(n):
#         if n==1:
#             return 0
#         return (helper(n-1)+k)%n  
#     return helper(n)+1   
# print(findTheWinner(5, 3)) 
    
    ########### METHOD: 3 tc: n  sc: constant
# def findTheWinner(n, k): 
#     a =0
#     for i in range(2, n+1):
#         a = (a+ k) % i
#     return a +1
# print(findTheWinner(5, 3)) 


# Q 17: TOWER OF HONOI:
# The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.
# Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.

# def toh(N, fromm, to, aux):
#     #code below
#     # sample print statement below
#     #print("move disk " + 1 + " from rod " + 1 + " to rod " + 2)
#     #in the above statement consider we are moving disk 1 from rod 1 to rod 2
#     #remember to return number of moves as well
    
#     count =0
#     def helper(N, fromm, to, aux):
#         nonlocal count
        
#         if N==1:
#             print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
#             count +=1
#             return
#         helper(N-1, fromm, aux, to)
#         print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
#         count +=1
#         helper(N-1, aux, to, fromm)
      
#     helper(N, fromm, to, aux) 
#     return count 




# Q 18: POWER SUM: TC: O(n), n: total number of element. sc:O(d), d is maximum depth
# Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2
# def power_sum(array,power=1):
#     #write code here
#     sum =0
#     for i in array:
#         if type(i) == list:
#             sum += power_sum(i, power+1)
#         else:
#             sum +=i
#     return sum ** power   
# arr=[1,2,[3, [2, [2]]]]     
# print(power_sum(array=arr))    



# BACKTRACKING START

# 19:FIND ALL POSSIBLE PERMUTATION OF [1,2,3]

# from itertools import permutations
# a =[1,2,3]
# b =permutations(a)
# print(list(b))

#  SECOND APPROACH : USING BACKTRACKING:sc:O(n),  TC: O(n*n!), n is the lenght of input array
# def permute(nums):
#     def backtrack(start, end):
#         if start == end:
#             results.append(nums[:])
#         for i in range(start, end):
#             # Swap elements to place the current element at the start position
#             nums[start], nums[i] = nums[i], nums[start]
#             # Recurse for the next position
#             backtrack(start + 1, end)
#             # Backtrack (undo the swap)
#             nums[start], nums[i] = nums[i], nums[start]

#     results = []
#     backtrack(0, len(nums))
#     return results
# nums2 = [1, 4, 5]
# print(permute(nums2))


# Q 20: Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# examples : nums = [3,3,2], output: [[3,3,2] , [3,2,3], [2,3,3] ]

# def permuteUnique(nums):
#     def backtrack(path):
#         if len(path) == len(nums):
#             results.append(path[:])
#             return
        
#         for num in frequency:
#             if frequency[num] > 0:
#                 # Add the element to the path
#                 path.append(num)
#                 frequency[num] -= 1

#                 # Recurse
#                 backtrack(path)

#                 # Backtrack
#                 path.pop()
#                 frequency[num] += 1

#     # Manually create the frequency dictionary
#     frequency = {}
#     for num in nums:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1

#     results = []
#     backtrack([])
#     return results

# # Example
# nums = [3, 3, 2]
# print(permuteUnique(nums))  # Output: [[3, 3, 2], [3, 2, 3], [2, 3, 3]]


#  SECOND MEHTODS

# from itertools import permutations
# a =[1,3,3]
# b =permutations(a)
# c= list(b)
# d =set(c)
# print(list(b))
# print(d)

#  THIRD METHODS:

# def permute(nums):
#     def backtrack(start, end):
#         if start == end:
#             # Check if the current permutation is already in the results list
#             if nums[:] not in results:
#                 results.append(nums[:])
#         for i in range(start, end):
#             # Swap elements to place the current element at the start position
#             nums[start], nums[i] = nums[i], nums[start]
#             # Recurse for the next position
#             backtrack(start + 1, end)
#             # Backtrack (undo the swap)
#             nums[start], nums[i] = nums[i], nums[start]

#     results = []
#     backtrack(0, len(nums))
#     return results

# nums2 = [1, 4, 4]
# print(permute(nums2))



#  Q 21: Power Set - Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

# METHOD 1
# def backtrack(start,path, nums, result ):
#     result.append(path[:])
#     for i in range(start, len(nums)):
#         path.append(nums[i])
#         backtrack(i+1, path, nums, result)

#         path.pop()

# def power_set(nums):
#     result =[]
#     backtrack(0, [], nums, result)
#     return result


# nums = [1, 2, 3]
# print(power_set(nums))    
# 
# 
# METHOD 2:

# from itertools import combinations

# lis =[1,2,3]
# power_set =[]
# for r in range(len(lis)+1):
#     subsets =combinations(lis, r)
#     power_set.extend(subsets)

# power_set =[list(subset) for subset in power_set]
# print(power_set)







#  Q 22: Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# def subsetsWithDup(nums):
#     def backtrack(start, path):
#         result.append(path[:])  # Add a copy of the current subset (path) to the result
#         for i in range(start, len(nums)):
#             # If the current element is the same as the previous element, and it is not at the start of this subset, skip it
#             if i > start and nums[i] == nums[i - 1]:
#                 continue
#             # Include the current element and move forward to explore further subsets
#             path.append(nums[i])
#             backtrack(i + 1, path)
#             path.pop()  # Backtrack by removing the last element to explore other possibilities

#     nums.sort()  # Sort the input array to handle duplicates
#     result = []
#     backtrack(0, [])
#     return result


# nums = [1, 2, 2]
# print(subsetsWithDup(nums))



# Q 23: Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# METHOD 1:

# from itertools import combinations
# a=[1,2,3]
# b=combinations(a, 2)
# print(list(b))

# METHOD: 2

# def combine(n, k):
#     def backtrack(start, path):
#         # If the combination is of the right length, add it to the result
#         if len(path) == k:
#             result.append(path[:])
#             return
        
#         # Explore further by adding more elements to the current path
#         for i in range(start, n + 1):
#             path.append(i)
#             backtrack(i + 1, path)
#             path.pop()  # Backtrack by removing the last element to explore other possibilities
    
#     result = []
#     backtrack(1, [])
#     return result

# print(combine(3, 2))


# Q 24: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# (the integers in the candidates array are all non negative )

# def combinationSum(candidates, target):
#     result = []
    
#     def backtrack(remaining, path, start):
#         # Base case: if remaining target is 0, we found a combination
#         if remaining == 0:
#             result.append(path[:])
#             return
        
#         # Iterate over candidates, starting from the current index
#         for i in range(start, len(candidates)):
#             candidate = candidates[i]
            
#             # Skip if the candidate is greater than the remaining target
#             if candidate > remaining:
#                 continue
            
#             # Choose the candidate, and reduce the remaining target
#             path.append(candidate)
#             backtrack(remaining - candidate, path, i)  # not i + 1 because we can reuse the same element
#             path.pop()  # Backtrack
    
#     # Start the backtracking with an empty path and the full target
#     backtrack(target, [], 0)
#     return result

# # Example usage
# candidates = [1, 2, 3, 4]
# target = 7
# print(combinationSum(candidates, target))



# Q 25: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# def combinationSum2(candidates, target):
#     candidates.sort()
#     result =[]
#     def backtrack(remaining, path, start):
#         if remaining ==0:
#             result.append(path[:])
#             return
#         for i in range(start, len(candidates)):
#             if i > start and candidates[i] == candidates[i-1]:
#                 continue
#             candidate =candidates[i]

#             if candidate > remaining:
#                 break
#             path.append(candidate)
#             backtrack(remaining-candidate, path, i+1)
#             path.pop()
#     backtrack(target, [], 0)
#     return result
            
# candidates = [3, 5, 2, 1, 3]
# target = 7
# print(combinationSum2(candidates, target))


# Q 26: Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


# def combinationSum3(k, n):
#     result =[]
#     def backtrack(start, path, remaining):
#         if len(path) ==k and remaining ==0:
#             result.append(path[:])
#             return
#         if len(path) > k or remaining < 0:
#             return
        
#         for i in range(start,10):
#             path.append(i)
#             backtrack(i+1, path, remaining-i)
#             path.pop()
#     backtrack(1, [], n)
#     return result
        
# k = 3
# n = 6
# print(combinationSum3(k, n))

#  Q 27: SUDOKU SOLVER:

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# Each of the digits 1-9 must occur exactly once in each row.
# 
# Each of the digits 1-9 must occur exactly once in each column.
# 
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# 
# The '.' character indicates empty cells.
# 
# Constraints:
# 
# board.length == 9
# 
# board[i].length == 9
# 
# board[i][j] is a digit between 1 and 9 , inclusive or '.'.
# 
# It is guaranteed that the input board has only one solution.

# def solveSudoku(board):
#     def isValid(board, row, col, num):
#         # Check if 'num' is not in the current row
#         for i in range(9):
#             if board[row][i] == num:
#                 return False

#         # Check if 'num' is not in the current column
#         for i in range(9):
#             if board[i][col] == num:
#                 return False

#         # Check if 'num' is not in the current 3x3 sub-box
#         boxRowStart = (row // 3) * 3
#         boxColStart = (col // 3) * 3
#         for i in range(3):
#             for j in range(3):
#                 if board[boxRowStart + i][boxColStart + j] == num:
#                     return False

#         return True

#     def solve(board):
#         for row in range(9):
#             for col in range(9):
#                 if board[row][col] == '.':
#                     for num in map(str, range(1, 10)):
#                         if isValid(board, row, col, num):
#                             board[row][col] = num
#                             if solve(board):
#                                 return True
#                             board[row][col] = '.'
#                     return False
#         return True

#     solve(board)

# # Example usage:
# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]

# solveSudoku(board)

# # Print the solved board
# for row in board:
#     print(row)




# Q 28: N-QUEENS PUZZLE:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# def solveNQueens(n):
#     def isValid(board, row, col):
#         # Check if a queen is already placed in the same column
#         for i in range(row):
#             if board[i][col] == 'Q':
#                 return False

#         # Check the upper-left diagonal
#         for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#             if board[i][j] == 'Q':
#                 return False

#         # Check the upper-right diagonal
#         for i, j in zip(range(row, -1, -1), range(col, n)):
#             if board[i][j] == 'Q':
#                 return False

#         return True

#     def solve(board, row):
#         if row == n:
#             # All queens are placed, add the solution to the result
#             result.append([''.join(row) for row in board])
#             return

#         for col in range(n):
#             if isValid(board, row, col):
#                 # Place the queen
#                 board[row][col] = 'Q'
#                 # Recurse to place the rest of the queens
#                 solve(board, row + 1)
#                 # Backtrack by removing the queen
#                 board[row][col] = '.'

#     result = []
#     # Create the chessboard, initially filled with '.'
#     board = [['.' for _ in range(n)] for _ in range(n)]
#     solve(board, 0)
#     return result



# ****************** DYNAMIC PROGRAMMING START.*****************



# Q 29: FIBONACCI SEQUESNCE:

#  Solution 1: T=O(2^n) , S=O(n) : RECURSIVE APPROACH
# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# def fibo(n):
#     for i in range(n):
#         print(fibonacci(i), end=' ')

# fibo(10)

# Solution 2: T=O(n) , S=O(n)

# def fibonacci(n, memo):
#     if memo[n] is not None:
#         return memo[n]
#     if n==0:
#         memo[n] =0
#     elif n==1:
#         memo[n] =1
#     else:
#         memo[n] =fibonacci(n-1, memo)+fibonacci(n-2, memo)
#     return memo[n]

# def print_fibo(n):
#     memo=[None]*n
#     for i in range(n):
#         print(fibonacci(i, memo), end=' ')

# print_fibo(10)


# Solution 3: T=O(n) , S=O(1):

# def fibo(n):
#     if n>=0:
#         print(0, end=' ')
#     if n>=2:
#         print(1, end=' ')
#     a, b =0, 1

#     for i in range(2, n):
#         next_fib =a+b
#         print(next_fib, end=' ')
#         a,b =b,next_fib

# fibo(10)   
# 
