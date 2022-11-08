# 1)print Amstrong num from 1-1000
# for i in range(1001):
#     num=i
#     n=len(str(i))
#     result=0
#     while i!=0:
#         digit=i%10
#         result=result+digit**n
#         i=i//10
#     if num==result:
#         print("number is Amstrong:",num)

 # 2)print 1
 #         12
 #         123
 #         1234
 #         12345
# n=int(input("enter the num of rows:"))
# for i in range(1,n+1):   # rows
#     for j in range(1,i+1):  #columns (1,i+1)=> 1 for 1sr row and i+1=> increase column 12
#         print(j,end="")
#     print()


# 3) print
# n=int(input("enter the no of rows needed:"))
# for row in range (n):
#     for col in range(n):
#         if col==0 or row==(n-1) or row==col:
#             print("*", end="")
#
#         else:
#             print(end="")
#     print()

#print factorial numbers
# n=int(input("enter the num"))
# len=len(str(n))
# for i in range(n):
#     while i!=0:
#         digit=n*(len(n-1))
#         print(digit)

# by in built function
# import math
# n=int(input("enter the num"))
# result=math.factorial(n)
# print(result)

"""def fact(n):
    if n==0:
        return 1
    else:
        return(n*fact(n))
n=int(input("enter num:"))
result=fact(n)
print(n,result)"""










