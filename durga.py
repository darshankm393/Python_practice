#for loops
"""str="darshan"
count=0
for i in str:
    count+=1
    print(i, )
print("num of char:",count)"""

#print the index of the string
"""str=input("enter any string:")
x=0
for i in str:
    print(i,x)
    x+=1"""
#print hello 10 times
"""str="darshan"
x=0
for i in range(10):
    print(str,x)
    x+=1"""
#display 0-20 only odd num
"""for i in range(20):
    if i%2!=0:
        print("it is odd num:",i)"""
#print 10-1 in decending order
"""for i in range(10,0,-1):
    print(i)"""
#sum of the num in the list
"""list=[10,20,30,40]
sum=0
for i in list:
    sum=sum+i
print(sum)"""

#while loop
"""x=20
while x<=40:
    if x%2==0:
     print(x)
    x+=1"""
#print sum of 1st 20 num
#this is for loop
"""sum=0
for i in range(21):
    sum+=i
print(sum)"""
#while loop

"""sum=0
i=1
while  i<=20:
    sum+=i
    i+=1
print(sum)"""

"""name=""
while name!="darshan":
    name=input("enter your name:")
print("thanks for conformation")"""
#enter name and pwd
"""name=""
pwd=""
while name!="darshan" or pwd!="1234":
    name=input("enter  name:")
    pwd=input("enter password:")
print("congrats darshan")"""
#nested for loop
"""for i in range(4):
    for j in range(4):
        print("i is=:",i, "j is:",j)"""

#num of stars u enter that much * u need to get
"""n=int(input("enter num of rows"))
for i in range(1,n+1):# i represents no of rows

    for j in range(i):# j represents no of columns

       print("*",end=" ")
    print()"""

"""n=int(input("enter num of rows"))
for i in range(1,n+1):# i represents no of rows

    for j in range(i):# j represents no of columns
        end=""
        print()
        for k in range(i):
           print("*",end=" ")"""

"""n=int(input("enter num of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""    #or
"""n=int(input("enter num of rows"))
for i in range(n-1,1):
    print("* "*i)
"""
#Transfer statements
#Break
#continue
#pass

#BREAK
"""for i in range(10):
    if i==8:
        print("end ")
        break
    print(i)"""

"""cart=[10,20,30,40,500,80]
for i in cart:
    if i>=400:
        print("out of range")
        break
    print(i)"""
#continue
"""cart=[10,20,30,500,60,80]
for i in cart:
    if i>=300:
        print("300 is huge")
        continue
    print(i)"""

"""for i in range(10):
    if i%2==0:
        continue
    print(i)
"""

#loops with else

"""cart=[10,20,30,60,80] #if num is more than 400 then it breaks there
for i in cart:
    if i>=400:
        print("400 is huge")
        break
else:
    print("congrajulationd no error")
"""
#for and while
#excute the body for every itemin the given sequence==> for loop
#excute body as long as condition is true(dont know num of iteration in advance then)==> while loop










