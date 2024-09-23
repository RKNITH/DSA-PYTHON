# a =[-3,-1,0,3,5,9]
# b =[]
# def sorted_array(arr):
#     if len(arr) <=1:
#         return arr
#     for i in arr:
#         b.append(i**2)
#     return sorted(b)    

# print(sorted_array(a))

#  second ways

# def sorted_arr(arr):
#     n=len(arr)
#     i =0
#     j=n-1
#     ar =[0]*n
    
#     for k in reversed(range(n)):
#         if arr[i]**2 >arr[j]**2:
#             ar[k]=arr[i]**2
#             i+=1
#         else:
#             ar[k]=arr[j]**2
#             j -=1
#     return ar
# print(sorted_arr(a))



# monotonous array
# a =[-1,-2,-3]
# b =[0,1,2]
# c=[1,1,1]
# d=[1]
# e=[]
# f=[1,4,3,5]

# def monotonous_array(arr):
#     if len(arr)<=1:
#         return True
    
#     monotonic_incr =True
#     monotonic_decr =True

#     for i in range(0, len(arr)-2):
#         if arr[i] > arr[i+1]:
#             monotonic_incr =False
#         if arr[i] < arr[i+1]:
#             monotonic_decr =False

#     return monotonic_decr or monotonic_incr

# print(monotonous_array(a))        
# print(monotonous_array(b))        
# print(monotonous_array(c))        
# print(monotonous_array(d))        
# print(monotonous_array(e))        
# print(monotonous_array(f))        



#  RECURSION START:

# FIBONACCI SERIES

# ITERATIVE WAY
# def fibonacci(n):
#     fibo =[0,1]

#     for i in range(2, n):
#         fibo.append(fibo[-1]+fibo[-2])
#     return fibo[:n]    
    
# print(fibonacci(10))

#  RECURSIVE WAY:

# def fibo(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         fib_sequence = fibo(n - 1)
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         return fib_sequence

# print(fibo(10))



#   k-th symbol in grammar:


# def finding(n, k):
#     if n==1:
#         return 0
#     else:
#         previous_term = 2**(n-2)

#         if k <= previous_term:
#             return finding(n-1, k)
#         else:
#             return 1-finding(n-1, k-len(previous_term))


# JOSEPHUS PROBLEM:

#  RECURSIVE APPROACH
# def winner(n, k):
#     a =[i+1 for i in range(n)]
   
#     def helper(a):
#         if len(a)==1:
#             return a[0]

#         remove_index =(k-1)%len(a)
#         del a[remove_index]
#         a =a[remove_index:] +a[:remove_index]
#         return helper(a)
#     return helper(a)
            
    
# print(winner(5, 3))
            
# ITERATIVE APPROACH

# def winner(n, k):
#     a=0
#     for i in range(2, n+1):
#         a =(a+k)%i
#     return a+1

# print(winner(5, 3))    


# TOWER OF HONOI

# def toh(N, fromm, to, aux): 
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


# POWER SUM:
# a=[2,3,[4,1,2]]
# b =[[[2]]]

# def poerSum(a, power=1):
#     sum =0

#     for i in a:
#         if type(i)==list:
#             sum +=poerSum(i, power+1)
#         else:
#             sum += i    
#     return sum**power
# print(poerSum(a))
# print(poerSum(b))





# BACKTRACKING

#  FIND ALL PERMUTATION OF [1,2,3]

# from itertools import permutations
# a=[1,2,3]
# b=permutations(a)
# print(list(b))

# def permutaion(a):
#     result =[]
#     def backtrack(start, end):
#         if start == end:
#             result.append(a[:])
#         for i in range(start, end):
#             a[start], a[i] =a[i], a[start]
#             backtrack(start+1, end)  
#             a[start], a[i] =a[i], a[start]
#     backtrack(0, len(a))     
#     return result
# print(permutaion(a))     
        


# #  FIND ALL PERMUTAION OF [1,2,2]

# def permutaion(b):
#     result =[]

#     def backtrack(start, end):
#         if start == end:
#             if b[:] not in result:
#                 result.append(b[:])

#         for i in range(start, end):
#             b[start], b[i] =b[i], b[start]

#             backtrack(start+1, end)
#             b[start], b[i] =b[i], b[start]

#     backtrack(0, len(b))
#     return result

# b=[1,2,2]
# print(permutaion(b))


# ******************************************************************************88

# sum =0
# for i in range(101):
#     sum +=i
# print(sum)    



# a =1234
# print(len(str(a)))


# sum =0
# a=123
# for i in str(a):
#     sum +=int(i)
# print(sum)    



# def check_palindrone(str):
#     return str ==str[::-1] 



# print(check_palindrone('121'))
# print(check_palindrone('123'))


# def fibonacci(n):
#    fibo=[]

#    for i in range(11):
#       if i ==0:
#          fibo.append(0)
#       elif i==1:
#          fibo.append(1)
#       else:
#          fibo.append(fibo[-1]+fibo[-2]) 
#    return fibo            

# print(fibonacci(10))


# a=[-3,-1,0,2,3]
# b =[]
# def sorted_array(a):
#     for i in a:
#         b.append(abs(i))

#     c = sorted(b)
#     d=[]
#     for i in c:
#         d.append(i**2)
#     return d
# print(sorted_array(a))    



# def monotonic_array(a):
#     if len(a)<=1:
#         return a
    
#     increasing =decreasing =True
#     for i in range(1, len(a)):
#         if a[i] > a[i-1]:
#             decreasing =False
#         if a[i] < a[i-1]:
#             increasing =False
#     return increasing or decreasing

# a=[-1,2,3,2]
# print(monotonic_array(a))



# def kth_symbol(n, k):
#     if n==1:
#         return 0
#     length_of_previous_row =2**(n-2):

#     if k<length_of_previous_row:
#         return kth_symbol(n-1, k)
#     else:
#         return 1-kth_symbol(n-1, k-length_of_previous_row)
    
# print()    


# def findWinner(n,k):
#    a=0
#    for i in range(2, n+1):
#       a =(a+k)%i
#    return a+1


# ******************************************************

# Printing natural number

# def natural(n):
#     if n>100:
#         return
#     print(n)
#     natural(n+1)    
   
# natural(1)

#  factorial of a number

# def fact(n):
#     if n<=1:
#         return 1
#     return n* fact(n-1)
# print(fact(5))


#  PRINTING 321123 PATTERN

# def pattern(n):
#     if n==0:
#         return 
#     print(n, end='')
#     pattern(n-1)
#     print(n, end='')
# pattern(3)    


# FIBONACCI SERIES:

# iteratively:

# fibo =[]

# def fibonacci(n):
#     for i in range(n+1):
#         if i==0:
#             fibo.append(0)
#         elif i==1:
#             fibo.append(1)
#         else:
#             fibo.append(fibo[-1] + fibo[-2])         
    
#     return fibo

# print(fibonacci(10))


#  recursively:


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# def print_fibo(n):
#     for i in range(n+1):
#         print(fibonacci(i), end=' ')    
        
    
# print_fibo(10)    




#  SUM OF NATURAL NUMBER USING RECURSION:

# def sum_natural(current, n):
#     if current ==n:
#         return n
#     return current + sum_natural(current+1, n)

# print(sum_natural(0, 100))



# KTH-SYMBOL PATTERN:

# def generate_pattern(n):
#     if n == 1:
#         return "0"
#     previous_pattern = generate_pattern(n - 1)
#     new_pattern = ""
#     for char in previous_pattern:
#         if char == '0':
#             new_pattern += "01"
#         else:
#             new_pattern += "10"
    
#     return new_pattern

# # Function to print the pattern line by line
# def print_pattern(lines):
#     for i in range(1, lines + 1):
#         print(generate_pattern(i))

# # Example: Print the first 4 lines of the pattern
# print_pattern(4)


#  KTH-SYMBOL IN GRAMMAR:

# def kth(n, k):
#     if n==1:
#         return 0
#     previous_term =2**(n-2)
#     if previous_term > k:
#         return kth(n-1, k)
#     if previous_term < k:
#         return 1-kth(n-1, k-previous_term)
    
# print(4, 3)    



# JOSPHUS PROBLEM:

# iteratively:

# def joshephus(n, k):
#     a =0
#     for i in range(2,n+1):
#         a =(a+k) % i

#     return a+1

# print(joshephus(5, 3))   

#  recursively: methhod: 1

# def joshef(n, k):
#     a =[i+1 for i in range(n)]
#     def helper(a):
#         if(len(a)==1):
#             return a[0]
#         remove_index =(k-1) %len(a)
#         del a[remove_index]
#         a =a[remove_index:]+a[:remove_index]
#         return helper(a)
#     return helper(a)

# print(joshef(5, 3))

#  recursively : method : 2

# def josephus(n,k):
#     def helper(n):
#         if n==1:
#             return 0
#         return (helper((n-1)+k)) % k
#     return helper(n)+1






# TOWER OF HONOI PROBLEM:

# def toh(N, fromm, to, aux):
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



#  POWER SUM:

# n =[1,[2,3]]
# def power_sum(n, power =1):
#     sum =0
#     for i in n:
#         if type(i)==list:
#             sum +=power_sum(i, power+1)
#         else:
#             sum +=i

#     return sum **power     
        
# print(power_sum(n))        


# PERMUTATION OF STRING:

# METHODS 1
# str ='abc'
# from itertools import permutations
# a =permutations(str)
# b =list(a)
# print(b)

#  METHOD 2:

# def permutation(strs):
#     result =[]
#     def helper(start, end):
#         if start == end:
#             result.append(strs[:])
#         for i in range(start, end):
#             strs[start], strs[i] =strs[i], strs[start]
#             helper(start+1, end)
#             strs[start], strs[i] =strs[i], strs[start]

#     helper(0, len(strs))  
#     return result   


# a=[1,2,3]
# print(permutation(a))  


# find all permutaion of [1,2,2]

# METHODS 1
# def perm(n):
#     result =[]
#     def helper(start, end):
#         if start == end:
#             if n[:] not in result:
#                     result.append(n[:])
#         for i in range(start, end):
#              n[start], n[i] =n[i], n[start]
#              helper(start+1, end)
#              n[start], n[i] =n[i], n[start]
#     helper(0, len(n))
#     return result

# n =[1,2,2]
# print(perm(n))


# METHODS 2

# def permuteUnique(nums):
#     def backtrack(path):
#         if len(path) == len(nums):
#             results.append(path[:])
#             return
#         for num in frequency:
#             if frequency[num] > 0:
#                 path.append(num)
#                 frequency[num] -= 1

#                 backtrack(path)

#                 # Backtrack
#                 path.pop()
#                 frequency[num] += 1

#     # Frequency dictionary setup
#     frequency = {}
#     for num in nums:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1

#     # Initialize results list
#     results = []
#     backtrack([])
#     return results

        

#  POWER SET OF [1,2,3]

#  METHOD 1

# from itertools import combinations
# my_list =[1,2,3]

# power_set =[]
# for i in range(len(my_list)+1):
#     subsets =combinations(my_list, i)
#     power_set.extend(subsets)

# power_set =[list(subset) for subset in power_set]

# print(power_set)

#  METHOD 2:

# def backtrack(start, path, nums, result):
#     result.append(path.copy())  # Add the current path (subset) to result

#     # Explore all elements starting from 'start'
#     for i in range(start, len(nums)):
#         path.append(nums[i])      # Include the current element in the subset
#         backtrack(i + 1, path, nums, result)  # Recur for the next elements
#         path.pop()                # Backtrack, remove the current element

# def power_set(nums):
#     result = []
#     backtrack(0, [], nums, result)
#     return result

# nums = [1, 2, 3]
# print(power_set(nums))


#  FIND ALL POWER SET OF [1,2,2]

# def find_power_set(nums):
#     def backtrack(start, path):
#         result.append(path[:])  # Append a copy of the current subset
#         for i in range(start, len(nums)):
#             # Skip duplicates
#             if i > start and nums[i] == nums[i - 1]:
#                 continue
#             # Include nums[i] in the subset
#             path.append(nums[i])
#             # Move on to the next element
#             backtrack(i + 1, path)
#             # Exclude nums[i] from the subset
#             path.pop()
    
#     nums.sort()  # Sort the array to handle duplicates
#     result = []
#     backtrack(0, [])
#     return result

# nums = [1, 2, 2]
# print(find_power_set(nums))


#  FIND ALL POSSIBLE COMBINATIONS OF K NUMBERS CHOSEN FROM [1, N]
#  

# METHODS 1

# from itertools import combinations
# a =[1,2,3,4]
# b =combinations(a,3)
# print(list(b))

#  METHODS 2:

# def combinations(n, k):
#     result =[]
#     def backtrack(start, path):
#         if len(path) ==k:
#             result.append(path[:])
#             return
#         for i in range(start, n+1):
#             path.append(i)
#             backtrack(i+1, path)
#             path.pop()
#     backtrack(1, [])    
#     return result
# print(combinations(4,2))    

#  optimise above code:

# def combinations(n, k):
#     result =[]
#     def backtrack(start, path):
#         if len(path) ==k:
#             result.append(path[:])
#             return
#         need = k-len(path)
#         for i in range(start,n-(need-1)+1):
#             path.append(i)
#             backtrack(i+1, path)
#             path.pop()
#     backtrack(1, [])    
#     return result
# print(combinations(4,2)) 


# 
# def combinationSum(candidates, target):
#     result = []

#     def backtrack(remaining, path, start):
#         if remaining == 0:
#             result.append(path[:])
#             return
#         for i in range(start, len(candidates)):
#             candidate = candidates[i]
#             if candidate > remaining:
#                 continue
#             path.append(candidate)
#             backtrack(remaining - candidate, path, i)  # Allow the same candidate to be used again
#             path.pop()

#     backtrack(target, [], 0)
#     return result

# candidates = [1, 2, 3, 4]
# target = 7
# print(combinationSum(candidates, target))





# *********************************************************************************************************




#  SORTED OF ARRAY-SQUARE

# def sorted_square(array):
#     a =[]
#     for i in array:
#         a.append(i**2)

#     b = sorted(a)
#     return b

# array=[-3,-1,0,4,5]
# print(sorted_square(array))        

#  SECOND APPROACH:

# def sorted_square(array):
#     n =len(array)
#     a =[]
#     for i in array:
#         a.append(abs(i))
   
#     b=[]    
#     for i in sorted(a):
#         b.append(i**2)
#     return b

# array=[-3,-1,0,4,5]
# print(sorted_square(array))  

#  THIRD APPROACH:

# def sorted_square(array):
#     j=len(array)-1
#     i=0
#     n=len(array)
#     res =[0]*n
  
#     for k in reversed(range(n)):
#         if array[i]**2 > array[j]**2:
#             res[k] =array[i]**2
#             i+=1
#         else:
#             res[k]=array[j]**2
#             j -=1
#     return res
# array=[-3,-1,0,4,5]
# print(sorted_square(array))
            


#  MONOTONIC ARRAY:


# def monotonic_array(array):
#     if len(array) <=1:
#         return True
    
#     increasing=decreasing =True

#     for i in range(1, len(array)):
#         if array[i] > array[i-1] :
#             decreasing=False
#         if array[i] < array[i-1]:
#             increasing =False    
#     return increasing or decreasing



# a=[1,2,3]
# b=[-1,-1,2,0]
# print(monotonic_array(b))




#  RECURSION START:

#  factorial

# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))    
    

#  PRINTING 43211234

# def pattern(n):
#     if n==0:
#         return
#     print(n, end='')
#     pattern(n-1)
#     print(n, end='')
# pattern(5)       


#  FIBONACCI PATTERN

#  ITERATIVE 
# def fibo(n):
#     a,b= 0, 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b =b,a+b
# fibo(10)       


#  RECURSIVE 

# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# # Example usage:
# n = 10  # Number of terms to print
# for i in range(n):
#     print(fibonacci_recursive(i), end=" ")



    

#  KTH- SYMBOL IN GRAMMAR:

# def kth_symbol(n, k):
#     if n <=1:
#         return n
    
#     length_of_prev_row =2**(n-2)
#     if(k<=length_of_prev_row):
#         return kth_symbol(n-1, k)
#     else:
#         return 1-kth_symbol(n-1, k-length_of_prev_row)

        




#  JOSEPHOUS PROBLEM:


#  M-1
# def findTheWinner(n,k):
#     a =[]
#     for i in range(n):
#         a.append(i+1)

#     def helper(a, start_index):
#         if(len(a)==1):
#             return a[0]
#         removed_index =(start_index +k-1)%len(a)

#         del a[removed_index]

#         return helper(a, removed_index)  
#     return helper(a, 0)

# print(findTheWinner(4,3))


#  M-2

# def find_The_Winner(n,k):
#     a =[i+1 for i in range(n)]

#     def helper(a):
#         if len(a)==1:
#             return a[0]
#         removed_index =(k-1) %len(a)
#         del a[removed_index]

#         a =a[removed_index:] + a[:removed_index]

#         return helper(a)
#     return helper(a)


# M-3:

# def find_The_Winner(n,k):
#    def helper(n):
#       if n==1:
#          return 0
#       return (helper(n-1)+k)%n
#    return helper(n)+1



#  M-4:
# def find_The_Winner(n,k):
#     a=0
#     for i in range(2, n+1):
#         a =(a+k)%i
#     return a+1    


#  TOH:


# def toh(N, fromm, to, aux):
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




#  POWER SUM:

# def power_sum(array, power=1):
#     sum =0
#     for i in array:
#         if type(i)==list:
#             sum += power_sum(i, power+1)
#         else:
#             sum += i
#     return sum **power



# ALL PERMUTATION OF 'ABC'

# METHODS-1

# from itertools import permutations
# a =permutations('abc')
# b =list(a)
# print(b)

# METHOD-2

# def permuation(arr):
#     result =[]
#     n =len(arr)

#     def permuation(start, end):
#         if start == end:
#             result.append(arr[:])
#         for i in range(start, end):
#             arr[start], arr[i] =arr[i], arr[start]

#             permuation(start +1, end)
#             arr[start], arr[i] =arr[i], arr[start]
#     permuation(0, n)
#     return result 

    

# all unique permutaions of [1, 1, 2]

#  METHODS-1

# def permutaion(arr):
#     result =[]
#     n =len(arr)

#     def permutaion(start, end):
#         if arr[:] not in result:
#             result.append(arr[:])
#         for i in range(start, end):
#             arr[start], arr[i] =arr[i], arr[start]

#             permutaion(start +1, end)
#             arr[start], arr[i] =arr[i], arr[start]
#     permutaion(0, n)
#     return result    
#          

#  M-2

# def permuteUnique(nums):
#     frequency ={}
#     result =[]

#     def backtrack(path):
#         if len(path) == len(nums):
#             result.append(path[:])
#             return
        
#         for num in frequency:
#             if frequency[num]>0:
#                 path.append(num)
#                 frequency[num] -=1
#                 backtrack(path)

#                 path.pop()

#                 frequency[num] +=1

#     for num in nums:
#         if num in frequency:
#             frequency[num] +=1
#         else:
#             frequency[num] =1

#     backtrack([])
#     return result   
# 
# 
# 
#                      

# >>>>>>>>>>>>>>>>>>

# def permutateUnique(arr):
#     result =[]
#     frequency ={}

#     def backtrack(path):
#         if len(path) == len(arr):
#             result.append(path[:])
#             return
        
#         for num in frequency:
#             if frequency[num] >0:
#                 path.append(num)
#                 frequency[num] -=1

#                 backtrack(path)

#                 path.pop()
#                 frequency[num] +=1
#     for n in arr:
#         if n in frequency:
#             frequency[n] +=1
#         else:
#             frequency[n] =1    

#     backtrack([])
#     return result        





#  FIND ALL POWERSET:

# from itertools import combinations

# lis =[1,2,3]
# result =[]

# for i in range(len(lis)+1):
#     a = combinations(lis, i)
#     result.extend(a)

# result =[list(i) for i in result]

# print(result)



#  MEHTODS-2


