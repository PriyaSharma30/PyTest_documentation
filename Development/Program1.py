def fact(n):
    sum=1
    for i in range(1,n+1):
        sum = i*sum
    return sum
# n=5
# res=fact(n)    


def arms_num(n1):
    sum =0
    while n1>0:
        r=n1%10
        sum = sum +r**3
        n1=n1//10
    return sum  
# n1=153
# res1=arms_num(n1)   
# print(res1)   
# if n1 == res1:
#         print("Armstome Number")
# else:
#     print("Not Arms No.")  

def add_sum(a,b):
    sum =a+b
    return sum

# a=2
# b=4
# res2=add_sum(a,b)

def pall_num(n2):
    sum =0
    while n2>0:
        r=n2%10
        sum =r+sum*10
        n2=n2//10
    return sum    

# n2=152
# res3=pall_num(n2)
# print(res3)
# if res3 == n2:
#     print("pallendrome num")
# else:
#     print("Not pallendrome")    
