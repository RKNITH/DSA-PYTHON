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















#????????????  ARRAY START->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Q  29: 
# Given an array, rotate the array to the right by k steps, where k is non-negative.


#  method-1:
# def rotate_array(array, k):
#     n =len(array)
#     k =k%n

#     return array[-k:] + array[:-k]

# print(rotate_array( [1, 2, 3, 4, 5, 6, 7], 3))



#  METHOD -2 : CONSTANT SPACE:

# def reverse(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1

# def rotate_array(arr, k):
#     n = len(arr)
#     if n==0:
#         return arr
#     k = k % n  # Handle case when k is greater than n
#     reverse(arr, 0, n - 1)  # Reverse the entire array
#     reverse(arr, 0, k - 1)  # Reverse the first k elements
#     reverse(arr, k, n - 1)  # Reverse the remaining elements
#     return arr  # Return the modified array

# # Example usage
# print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]




#  Q 30:
# Container with most water
# Container with most Water - You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water(depth is constant across containers). Return the area(that the 2 lines and the X axis make) of container which can store the max amount of water. Notice that you may not slant the container.


# def max_area(height):
#     left =0
#     right =len(height) -1
#     max_water =0
#     while left < right:
#         width =right-left
#         current_height =min(height[left], height[right])
#         current_area =width * current_height

#         max_water =max(max_water, current_area)

#         if height[left] < height[right]:
#             left +=1
#         else:
#             right -=1
#     return max_water            

        

#  HASH TABLE START

# Q 30:
# Coding Exercise: Two Sum

# Two Sum - You are given an array of Integers and another integer targetValue. Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.

# def two_sum(nums, target):
#     # Create a dictionary to store the values and their indices
#     hash_table = {}
    
#     # Loop through the array
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         # Check if the complement exists in the hash table
#         if complement in hash_table:
#             return [hash_table[complement], i]
        
#         # If not, store the current number with its index
#         hash_table[num] = i
    
#     # If no solution is found
#     return []
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]





#  Q 31:

#  Isomorphic Strings - Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. s and t consist of any valid ascii character.

# def isomorphic_strings(s, t):
#     if len(s) != len(t):
#         return False
    
#     # Dictionaries to store mappings of s -> t and t -> s
#     map_s_to_t = {}
#     map_t_to_s = {}
    
#     for i in range(len(s)):
#         char_s = s[i]
#         char_t = t[i]
        
#         # Check if there is an existing mapping from s -> t
#         if char_s in map_s_to_t:
#             if map_s_to_t[char_s] != char_t:
#                 return False  # If the mapping is not consistent
#         else:
#             map_s_to_t[char_s] = char_t
        
#         # Check if there is an existing mapping from t -> s
#         if char_t in map_t_to_s:
#             if map_t_to_s[char_t] != char_s:
#                 return False  # If the mapping is not consistent
#         else:
#             map_t_to_s[char_t] = char_s
    
#     return True









#  Q 32>

# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



# Example:

# Input: prices = [9,1,5,3,7,5]

# Output: 6


#  SOLUTION>>>>>>>>>>>>


# def maxProfit(prices):
#     left =0
#     max_profit =0

#     for right in range(1, len(prices)):
#         if prices[right] < prices[left]:
#             left =right
#         else:
#             profit =max(max_profit, prices[right]-prices[left])    

#     return max_profit






#  Q 33>

# Two Sum II
# 
# Given a 1-indexed array of integer numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# 
# Return the indices of the two numbers, index1 and index2, array [index1, index2] of length 2.
# 
# It is guaranteed that there is exactly one solution. You may not use the same element twice.
# 
# Your solution must use only constant extra space.
# 
# 
# 
# Example: Input: numbers = [1,3,4], target = 5; Output: [1,3]


#  SOLUTION >>>>>>>>>>>>>>>

# def twoSum(numbers, target):
#     # Initialize the two pointers
#     start = 0
#     end = len(numbers) - 1

#     # Iterate until the two pointers meet
#     while start < end:
#         # Calculate the sum of the elements at start and end
#         current_sum = numbers[start] + numbers[end]
        
#         # If the sum is greater than the target, move the end pointer left
#         if current_sum > target:
#             end -= 1
#         # If the sum is less than the target, move the start pointer right
#         elif current_sum < target:
#             start += 1
#         # If the sum is equal to the target, return the 1-indexed positions
#         else:
#             return [start + 1, end + 1]





# 


#  Q 34 >


# 3 Sum
# 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# Example:
# 
# Input: nums = [-2,0,2,1,-1,-3]
# 
# Output: [[-2,0,2],[0,1,-1],[2,1,-3]]
# 
# 
# 
# Input: nums = [-1,2,6,-1,1]
# 
# Output: [[-1,2,-1]]
# 


#  SOLUTION >

def threeSum(nums):
    # Sort the input array
    nums.sort()
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through each element in the array (excluding the last two for triplet)
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set the two pointers
        left, right = i + 1, len(nums) - 1
        
        # Use the two-pointer technique to find valid triplets
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Move the left pointer and skip duplicates
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                # Move the right pointer and skip duplicates
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            # If the current sum is less than zero, move the left pointer to the right
            elif current_sum < 0:
                left += 1
            
            # If the current sum is greater than zero, move the right pointer to the left
            else:
                right -= 1
    
    return result








# Q 35>
# 

# Max Avg Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.
# 
# 
# 
# Example:
# 
# Input: [1,13,-6,-3,40,2], k = 4
# 
# Output: 11
# 
# 13 + -6 + -3 + 40 = 44; 44/4 = 11



#  SOLUTION:

# def findMaxAverage(nums, k):
#     current_sum =sum(nums[:k])
#     max_sum=current_sum

#     for i in range(k, len(nums)):
#         current_sum = current_sum + nums[i] -nums[i-k]
#         max_sum =max(max_sum, current_sum)
#     return max_sum /k    















#  Q 36 > 

# Repeated DNA Sequence
# Repeated DNA Sequence: 
# 
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# 
# •For example, "ACGAATTCCG" is a DNA sequence.
# 
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# 
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
# 
# Example:
# 
# Input: s = ”GAAAATCCCCGAAAATCCCCGAAAAAGGGTTT"
# 
# Output: [”GAAAACCCCC",”TCCCCGAAAA"]




#  SOLUTION>>>>>>>>>> METHOD-1

# def findRepeatedDnaSequences(s):
#     L=10
#     n=len(s)

#     seen, output =set(), set()

#     for start in range(n-L+1):
#         temp=s[start:start+L]
#         if temp in seen:
#             output.add(temp[:])

#         seen.add(temp)

#     return list(output)        



#  SOLUTION:   METHOD-2 

# def findRepeatedDnaSequence(s):
#     L=10
#     n=len(s)
#     if n <=L :return []

#     to_int ={'A':0, 'C':1, 'G':2, 'T':3}

#     nums =[to_int.get(s[i]) for i in range(n)]

#     a =4
#     aL=pow(a, L)

#     h=0
#     seen=set()
#     output =set()

#     for start in range(n-L+1):
#         if start !=0:
#             h =h*a -nums[start-1]*aL + nums[start+L-1]

#         else:
#             for i in range(L):
#                 h =h*a+ nums[i]
        
#         if h in seen:
#             output.add(s[start:start+L])

#         seen.add(h)  

#     return list(output)












# Q 37>>>>>>>>>>>>>>>>>>>

# Sliding Window Maximum
# Sliding Window Maximum
# 
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# 
# Return the max sliding window.
# 
# 
# Example:
# 
# Input: nums = [2,3,-2,-4,5,2,8,11], k = 3
# 
# Output: [3,3,5,5,8,11]


#  SOLUTION>>>

# from collections import deque
# def maxSlidingWindow(nums, k):
#     dq =deque()
#     output =[]

#     for i in range(k):
#         while dq and nums[i] >= nums[dq[-1]]:
#             dq.pop()

#         dq.append(i)

#     output.append(nums[dq[0]])

#     for i in range(k, len(nums)):
#         if dq and dq[0] == i-k:
#             dq.popleft()

#         while dq and nums[i]>= nums[dq[-1]]:
#             dq.pop()

#         dq.append(i)  
#         output.append(nums[dq[0]])

#     return output          





# 38>>>>>>>>>>>>>>>>>


# Minimum Window Substring
# Minimum Window Substring: 
# 
# Given two strings s and t of lengths m and n respectively, return the minimum window
# 
# substring
# 
# ofssuch that every character int(including duplicates) is included in the window. If there is no such substring, returnthe empty string"".
# 
# 
# 
# The testcases will be generated such that the answer is unique.
# 
# 


#   SOLUTION>>>>>>>>>>>>>>>>>>>>


# def minWindow(s, t):
#     if t =='': return ''

#     count_t ={}
#     slide_window ={}

#     for c in t:
#         count_t[c] =1 + count_t.get(c, 0)

#     need =len(count_t)

#     have =0

#     res =[-1,-1]

#     res_length =float('infinity')

#     left =0
#     for right in range(len(s)):
#         c =s[right]
#         slide_window[c] =1+ slide_window.get(c, 0)

#         if c in count_t and slide_window[c] == count_t[c]:

#             have +=1
#         while have == need:
#             if right-left +1 < res_length:
#                 res =[left, right]
#                 res_length =right-left+1

#             slide_window[s[left]] -=1
#             if s[left] in count_t and slide_window[s[left]] < count_t[s[left]]:
#                 have -=1

#             left +=1
#     left, right =res        

#     return s[left:right+1] if res_length != float('infinity') else ''






# ******* Q 39>>>>>>>>>>>>>

# Min Size Subarray Sum
# Minimum Size Subarray Sum: 
# 
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# 
# Example:
# 
# target = 15
# 
# nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
# 
# expected = 2
# 



#  ********** SOLUTION >>>>>>>>>>>>>>>>


# def minSubArrayLen(target, nums):
#     left =0
#     currentSum =0
#     length =float('infinity')

#     for right in range(len(nums)):
#         currentSum += nums[right]

#         while currentSum >=target:
#             newLength  =right-left+1
#             if newLength < length:
#                 length =newLength

#             currentSum -= nums[left]    
#             left +=1
            
#     return length if length !=float('infinity') else 0









#  Q 40:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Frequency of the Most Frequent Element
# The frequency of an element is the number of times it occurs in an array.
# 
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# 
# Return the maximum possible frequency of an element after performing at most k operations.
# 
# Example:
# 
# Input: nums = [2,3,5], k = 5
# 
# Output: 3

# def maxFrequency(nums, k):
#     nums.sort()

#     left =0
#     total =0
#     res =0

#     for right in range(len(nums)):
#         total += nums[right]
#         while  nums[right]*(right-left+1) > total +k:
#             total -= nums[left]
#             left +=1
#         res =max(res, right-left+1)   
#     return res    
























# ################    STRING ###############################


#  Q 41:

# First Non Repeating Character
# Question:
# 
# Non repeating character - You are given a string consisting of only lower case and upper-case English Alphabets and integers 0 to 9. Write a function that will take this string as Input and return the index of the first character that is non-repeating.
# 
# 
# 
# Try to optimise your solution:
# 
# Brute Force method : 
# T=O(n^2), S=O(1)
# 
# 
# 
# Optimal Solution:
# T=O(n), S=O(1)



#  SOLUTION:


#  METHODS---1
# s ='abc121eab'

# def first_non_repeating_character_brute_force(s):
#     n = len(s)
#     for i in range(n):
#         is_repeating = False
#         for j in range(n):
#             if i != j and s[i] == s[j]:
#                 is_repeating = True
#                 break
#         # If the character is not repeating, return its index
#         if not is_repeating:
#             return i
#     return -1  # If no non-repeating character is found

# # Example usage
# input_str = 'abc121eab'
# result = first_non_repeating_character_brute_force(input_str)
# print(f"The index of the first non-repeating character is: {result}")




#  methods-2

# def first_non_repeating_character(s):
#     # Step 1: Create a frequency dictionary
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1

#     # Step 2: Find the first non-repeating character
#     for index, char in enumerate(s):
#         if frequency[char] == 1:
#             return index

#     return -1  # If no non-repeating character is found

# # Example usage
# input_str = 'abc121eab'
# result = first_non_repeating_character(input_str)
# print(f"The index of the first non-repeating character is: {result}")







#   42:


# Palindrome-You are given a string. Write a function to check whether the string is a palindrome or not.
# 
# 
# 
# Try:
# 
# To optimise your solution. We will discuss 3 solutions with the following Time and Space complexities
# 
# Solution 1:
# 
# T=O(n^2) , S=O(n)
# 
# Solution 2:
# 
# T=O(n) , S=O(n)
# 
# Solution 3:
# 
# T=O(n) , S=O(1)





#   solution::::::


#  METHODS -1

# def is_palindrome_brute_force(s):
#     # Create a reversed version of the string and compare
#     reversed_str = s[::-1]
#     return s == reversed_str

# # Example usage
# input_str = "madam"
# print(f"Is '{input_str}' a palindrome? {is_palindrome_brute_force(input_str)}")



#  METHODS-2

# def is_palindrome_recursive(s):
#     # Base case: If the string is empty or has one character, it's a palindrome
#     if len(s) <= 1:
#         return True
#     # Compare the first and last characters
#     if s[0] == s[-1]:
#         # Check the substring excluding the first and last characters
#         return is_palindrome_recursive(s[1:-1])
#     else:
#         return False

# # Example usage
# input_str = "racecar"
# print(f"Is '{input_str}' a palindrome? {is_palindrome_recursive(input_str)}")



#  METHODS -3

# def is_palindrome_optimized(s):
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         # Compare characters at left and right pointers
#         if s[left] != s[right]:
#             return False
#         # Move pointers inward
#         left += 1
#         right -= 1

#     return True

# # Example usage
# input_str = "A man a plan a canal Panama".replace(" ", "").lower()  # Normalizing string (ignoring spaces and case)
# print(f"Is '{input_str}' a palindrome? {is_palindrome_optimized(input_str)}")










#  **************** Q 43:


# Coding Exercise: Longest Sub string with Unique characters
# Question:
# 
# Longest Unique char Substring - Given a string s, find the length of the longest substring without repeating characters.


# def length_of_longest_substring(s):
#     # Set to store characters in the current window
#     char_set = set()
#     left = 0  # Left pointer for the sliding window
#     max_length = 0  # Variable to store the maximum length of substring

#     # Traverse the string with the right pointer
#     for right in range(len(s)):
#         # If the character is already in the set, move the left pointer
#         while s[right] in char_set:
#             # Remove the character at the left pointer and move the pointer to the right
#             char_set.remove(s[left])
#             left += 1
        
#         # Add the character at the right pointer to the set
#         char_set.add(s[right])
#         # Update max_length if the current window length is greater
#         max_length = max(max_length, right - left + 1)

#     return max_length

# # Example usage
# input_str = "abcabcbb"
# print(f"The length of the longest substring without repeating characters is: {length_of_longest_substring(input_str)}")








#  Q 44 >>>>

# Group Anagrams
# Question:
# 
# Group Anagrams - Given an array of strings consisting of lower case English letters, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.



#  SOLUTION >>>>>>>>>>>>>>>>>>>


#  METHODS-1

# from collections import defaultdict

# def group_anagrams(strs):
#     # Initialize a default dictionary where each value is a list.
#     anagrams = defaultdict(list)

#     # Traverse each word in the given list.
#     for word in strs:
#         # Sort the word and use it as the key.
#         sorted_word = ''.join(sorted(word))
        
#         # Add the original word to the list of its sorted version.
#         anagrams[sorted_word].append(word)
    
#     # Return all grouped anagrams as a list of lists.
#     return list(anagrams.values())

# # Test with the provided example
# input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output = group_anagrams(input_strs)
# print(output)



#  METHODS----2:

# def group_anagram(strings):
#     if len(strings) ==0:
#         return []
    
#     sorted_string =[''.join(sorted(i) for i in strings)]
#     hash ={}

#     for i in range(len(sorted_string)):
#         if sorted_string[i] in hash:
#             hash[sorted_string[i]].append(strings[i])
#         else:
#             hash[sorted_string[i]] =[strings[i]]
#     return list(hash.values())        








#  Q 45.............................

#  ................. BINARY SEARCH ...................


#  Q 45 >.............

# Binary Search Algorithm
# Question:
# 
# Binary Search - Given an array of integers which is sorted in ascending order, and a target integer, write a function to search for whether the target integer is there in the given array. If it is there then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.
# 



# def binary_search(arr, target):
#     # Initialize pointers
#     left, right = 0, len(arr) - 1
    
#     # While there is a search space
#     while left <= right:
#         # Find the middle element
#         mid = (left + right) // 2
        
#         # Check if the target is found
#         if arr[mid] == target:
#             return mid
        
#         # If target is smaller, narrow down to left half
#         elif arr[mid] > target:
#             right = mid - 1
        
#         # If target is larger, narrow down to right half
#         else:
#             left = mid + 1
    
#     # If target is not found, return -1
#     return -1

# # Test the iterative approach
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target = 7
# result = binary_search(arr, target)
# print(f"Target {target} found at index: {result}")  # Output: Target 7 found at index: 3







#   Q 46>>>>>>>>>>>>>>>>

# Search in rotated sorted array
# Question:
# 
# Search in Rotated Sorted array- You are given an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given an integer target, return the index of target if it is in the array, else return -1. You must write an algorithm with O(log n) runtime complexity.



#  SOLUTION>>>>>>>>>>>>

# def search_rotated_sorted_array(nums,target):
#     left =0
#     right =len(nums)-1

#     while left <= right:
#         mid =(left+right)//2

#         if nums[mid] ==target:
#             return mid
        
#         if nums[left] <=nums[mid]:
#             if target >=nums[left] and target < nums[mid]:
#                 right =mid-1
#             else:
#                 left = mid+1
#         else:
#             if target <=nums[right] and target > nums[mid]:
#                 left =mid+1
#             else:
#                 right =mid-1
#     return -1            













#  Q 47 >>>>>>>>>>>>>>

# Search for range
# Question:
# 
# Find First and Last Position of Element in Sorted Array-You are given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.
# 
# Try:
# 
# Try to write both the iterative solution and recursive solution



#  METHODS---1............... ITERATIVE APPROACH

# def search_for_range(array,target):

#     #  HELPER TO FIND FIRST OCCURANCE
#     def find_first_position(array, target):
#         left, right=0, len(array)-1
#         first_pos =-1

#         while left <=right:
#             mid =(left+right) //2

#             if array[mid] == target:
#                 first_pos =mid
#                 right =mid-1
#             elif array[mid] < target:
#                 left =mid+1
#             else:
#                 right =mid-1
#         return first_pos     


#             #    HELPER TO FIND LAST OCCURANCE

#     def find_last_occurance(array, target):
#         left, right =0, len(array)-1
#         last_pos =-1
#         while left<=right:
#             mid =(left+right)//2
#             if array[mid] ==target:
#                 last_pos =mid
#                 left =mid+1
#             elif array[mid] <target:
#                 left =mid+1
#             else:
#                 right =mid-1
#         return last_pos

#     first_pos =find_first_position(array, target)
#     last_pos =find_last_occurance(array, target)    

#     return [first_pos, last_pos]                    



# #  METHODS -2    RECURSIVE 

# def search_for_range_recursive(array, target):
#     # Recursive helper function to find the first position
#     def find_first_position(left, right):
#         if left > right:
#             return -1
#         mid = (left + right) // 2
#         if array[mid] == target:
#             # If mid is the target and it's either the first element or the previous element is not the target
#             if mid == 0 or array[mid - 1] != target:
#                 return mid
#             else:
#                 return find_first_position(left, mid - 1)
#         elif array[mid] < target:
#             return find_first_position(mid + 1, right)
#         else:
#             return find_first_position(left, mid - 1)

#     # Recursive helper function to find the last position
#     def find_last_position(left, right):
#         if left > right:
#             return -1
#         mid = (left + right) // 2
#         if array[mid] == target:
#             # If mid is the target and it's either the last element or the next element is not the target
#             if mid == len(array) - 1 or array[mid + 1] != target:
#                 return mid
#             else:
#                 return find_last_position(mid + 1, right)
#         elif array[mid] < target:
#             return find_last_position(mid + 1, right)
#         else:
#             return find_last_position(left, mid - 1)

#     # Find the first and last positions
#     first_pos = find_first_position(0, len(array) - 1)
#     last_pos = find_last_position(0, len(array) - 1)

#     return [first_pos, last_pos]

# # Example Usage
# array = [5, 7, 7, 8, 8, 10]
# target = 8
# print(search_for_range_recursive(array, target))  # Output: [3, 4]














#  Q 48>>>>>>>>>>>>>>>>>>>>>>>


# Search in Matrix
# Question:
# 
# Search in 2D Array-Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# 
# The first integer of each row is greater than the last integer of the previous row.
# 
# If the value is there in the matrix return true, else false.
# 
# 
# 
# Try :
# 
# Try to write the solution with T=O(mn) where m and n are the number of rows and number of columns respectively





#  SOLUTION >>>>>


def search_in_matrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols =len(matrix), len(matrix[0])

    left =0
    right =rows*cols -1

    while left <= right:
        mid =(left + right)//2

        row =mid//cols
        col =mid % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < targte:
            left =mid+1
        else:
            right =mid-1
    return False            






# >>>>>>>>>>>>>>>>>>>>  BUBBLE SORT
#  Q 49

# Bubble Sort Algorithm

# Bubble Sort - You are given an array of integers. Write a function that will take this array as input and return the sorted array using Bubble sort.

#  SOLUTION
def bubble_sort(array):
    n =len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] =array[j+1], array[j]
    return array            






#  Q 50:         .. INSERTION SORT.........

# Insertion Sort Algorithm
# 
# Insertion Sort -You are given an array of integers. Write a function that will take this array as input and return the sorted array using Insertion sort.


def insertion_sort(array):
    n =len(array)
    for i in range(1, n):
        insert_index =i
        current_value =array[i]

        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                insert_index =j

        array.insert(insert_index, current_value)
    return array            







# Q 51 >>>>>>>>>>>>>>>>

# Selection Sort Algorithm
# 
# Selection Sort-You are given an array of integers. Write a function that will take this array as input and return the sorted array using Selection sort.
# 


def selection_sort(nums):
    n =len(nums)
    for i in range(n-1):
        min_index =i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index =j
        min_value =nums.pop(min_index)
        nums.insert(i, min_index)
    return nums



#    Q 52:  MERGE SORT....
# 
def merge_sort(array):
    n =len(array)
    if n<=1:
        return array
    mid =n//2
    left_half =array[:mid]
    right_half =array[mid:]

    sorted_left =merge_sort(left_half)
    sorted_right =merge_sort(right_half)

    def merge(left, right):
        result =[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j +=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result            

    return merge(sorted_left, sorted_right)




# Q 53 >>>>>>>>>
# 
#  QUICK SORT\

# Quick Sort-You are given an array of integers. Write a function that will take this array as input and return the sorted array using Quick sort.


def swap(array, i, j):
    # Swap the elements at index i and j in the array
    array[i], array[j] = array[j], array[i]

def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    # Choose the last element as the pivot
    pivot = array[end]
    # Initialize the partition index to start
    partition_index = start

    for i in range(start, end):
        # If the current element is less than or equal to the pivot
        if array[i] <= pivot:
            # Swap it with the element at partition index
            swap(array, i, partition_index)
            # Move the partition index one step to the right
            partition_index += 1

    # Swap the pivot element with the element at the partition index
    swap(array, partition_index, end)

    return partition_index

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start < end:
        # Partition the array and get the pivot index
        pivot_index = partition(array, start, end)
        # Recursively sort the elements before and after partition
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)

    return array





# SECOND APPROACH:    TC: O(NLOG(N))   SC : LOG(N)


def swap(array, i, j):
    # Swap elements at indices i and j in the array
    array[i], array[j] = array[j], array[i]

def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    # Choose the last element as the pivot
    pivot = array[end]
    partition_index = start

    # Rearrange elements based on pivot
    for i in range(start, end):
        if array[i] <= pivot:
            swap(array, i, partition_index)
            partition_index += 1

    # Swap pivot to its correct position
    swap(array, partition_index, end)
    return partition_index

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    while start < end:
        # Partition the array and get pivot index
        pivot_index = partition(array, start, end)

        # Recursively sort the smaller subarray first to reduce recursion depth
        if pivot_index - start < end - pivot_index:
            quick_sort(array, start, pivot_index - 1)
            start = pivot_index + 1  # Tail call optimization for right part
        else:
            quick_sort(array, pivot_index + 1, end)
            end = pivot_index - 1  # Tail call optimization for left part

    return array





#  Q 54............... REDIX SORT................

# Radix Sort Algorithm
# 
# Radix Sort-You are given an array of non-negative integers. Write a function that will take this array as input and return the sorted array using Radix sort.


def counting_sort(array, place):
    # Find the maximum digit value (0-9) for base 10 numbers
    max_digit = 9  
    size = len(array)
    
    # Create an output array to store sorted values
    output = [0] * size
    # Initialize count array with zero values (10 for each digit)
    count = [0] * (max_digit + 1)

    # Calculate the frequency of each digit at the given place value
    for i in range(size):
        index = (array[i] // place) % 10
        count[index] += 1

    # Compute the cumulative count
    for i in range(1, max_digit + 1):
        count[i] += count[i - 1]

    # Place elements in the output array based on the cumulative count
    i = size - 1
    while i >= 0:
        index = (array[i] // place) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back into the original array
    for i in range(size):
        array[i] = output[i]

def radix_sort(array):
    # Check if the input array is empty
    if len(array) == 0:
        return array
    
    # Find the maximum number to determine the number of digits
    max_num = max(array)
    
    # Initialize place value (1s, 10s, 100s, etc.)
    place = 1
    
    # Apply counting sort for each digit place value
    while max_num // place > 0:
        counting_sort(array, place)
        place *= 10
    
    return array

# Example usage:
array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(array)
print("Sorted array:", sorted_array)
