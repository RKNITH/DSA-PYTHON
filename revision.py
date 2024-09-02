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
        


#  FIND ALL PERMUTAION OF [1,2,2]

def permutaion(b):
    result =[]

    def backtrack(start, end):
        if start == end:
            if b[:] not in result:
                result.append(b[:])

        for i in range(start, end):
            b[start], b[i] =b[i], b[start]

            backtrack(start+1, end)
            b[start], b[i] =b[i], b[start]

    backtrack(0, len(b))
    return result

b=[1,2,2]
print(permutaion(b))




 



