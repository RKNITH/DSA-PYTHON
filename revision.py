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



    



