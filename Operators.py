#Arthematic Operators
x=2
y=4
print(x+y)

print(y-x)

print(x/y)

#Assignment Operators
x=x+2
print(x)
#in shortcut way
x+=2
print(x)
x*=3
print(x)

x/=2
print(x)

a,b=5,6
print(a)
print(a+b)

#Unary Operators
n=7
print(n)

n=-n
print(n)
#Relational operetors
a=3
b=4
print(a>b)


print(a<b)
print(a==b )
#not operator
x=('true')
print(x)
print(not x)  #false

#Binary to decimal
bin(25)
print(bin(25))


print(0b0101) #5

print(oct(25)) #0o31

print(0o31) #25 zero o

print(hex(25)) #0x19

print(0x19)  #25 zero x
 #conversion to binary

print(bin(31))

print(oct(52))
print(hex(65))

print(0b10101010)

print(0o54)
print(0xa)
print(0xf)

print(0b110011010)


#swap the two numbers

a=5
b=6

temp=a
a=b
b=temp    #this is by using third variable
print('a',a)
print('b',b)

#swap without third variable

a=5
b=6

a=a+b
b=a-b
a=a-b
print('a',a)
print('b',b)
#swap by using xor(helps in not wasting the extra bit

a=5
b=6

a=a^b
b=a^b
a=a^b

print('a=',a)
print('b=',b)
#simple way to swap
a=5
b=6
a,b=b,a
print('a==',a)
print('b==',b)

#Bitwise operator
#1)Compliment Ope

print(~12)

print(~62)
print(0b111110)
#Bitwise AND oper

print(12&13)  #12

print(20&16)
"""AND both one then its one 
20=10100
16=10000
compare bitwise 
  10000
print(0b10000)"""
print(12|13) #or any one is one then its one
print(0b1101)

#XOR
print(12^13)
#when both num is different then go for one
print(0b0001)

#left Shift(<<)
print(10<<2)
print(0b101000)
print(0b10)

"""#input functions
x=input("enter 1st num") #input function acts as string so convert to integer and add
y=input("enter 2nd num")
z=x+y
print(z)

x=input("enter 1st num")
a=int(x) # converting string to integer
y=input("enter 2nd num")
b=int(y)
z=a+b
print(z)

#another way
x=int(input("enter 1st num"))
y=int(input("enter 2nd num"))
z=x+y
print(z)"""

"""ch=input("enter char")[0]
print(ch)"""

"""#evaluating in the console
res=eval(input("enter exp"))
print(res)"""

"""#if statements
x=9
r=x%2
if(r==0):
    print("even")
else:
    print("odd")"""

"""#nested if

x=2
r=x%2
if(r==0):
    print("even")
    if(x>2):
        print("greatr thn 2")
    else:
        print("lesser")
else:
    print("odd")

#ELIF statements

x=1
if(x==1):
  print("one")
elif(x==2):
  print("two")
elif(x==3):
  print("three")
else:
 print("wrong input")"""


 #Loops

"""i=1
while(i<=5):
 print("darshan")
 i=i+1
 print("##########")"""

"""i=5
while(i>=1):
  print("hello", i)
  i=i-1"""
#nested while loop
i=1

"""while(i<=5):
    print("darshan  ",end="")
    j=1
    while(j<=4):
        print("good boy  ",end="")
        j=j+1
    i=i+1
    print()"""
#FOR LOOP

x=("darshan", 29,2.9)
for i in x:
 print(x)

x=("darshan")
for i in x:
    print(i)

x=10
for i in range(10):
    print(i)

"""for i in range(11,21,2):  #starting point, end point, iteration
    print(i)

for i in range(20,11,-2):
    print(i)
    
    
#print num divide by 5 from 1-20
for i in range(1,21):
    if i%5!=0:
        print(i)

x=int(input("howmany candy you want?"))
i=1
while i<=x:

    print("candy")
    i+=1"""
"""av=5
x=int(input("how many candy you want?"))

i=1
while i<=x:
    if i>5:
        break
    print("candy")
    i+=1
print("bye")"""
"""#print num 1-100 which are divisable by 5
print("####################")
x=100
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
        i+=1
    print(i)"""
"""#print even num from 1-100
print("#################")
for i in range(1,101):
    if i%2==0:
        print(i)
        continue
print("end")"""

"""#print num 1-100 which are not odd
print("#################")
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
print("end")"""

"""#check for prime num
print("#########")
x=int(input("enter num?"))
if x>1:
    #iterate 2 to n/2
    for i in range(2,int(x/2)+1):
        if x%i==0:
            print("num is  not prime",x)
            break
    else:
     print("num is prime")
else:
 print("num is prime")"""

"""num = 11
# If given number is greater than 1
if num > 1:
# Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")"""

"""#print #### 16times


for i in range(4):
    for i in range(4):
        print("# " ,end="")
    print()"""

"""for i in range(4):
    for j in range(i+1):
      print("# ",end="")
    print()"""
"""#list divisable by 5
print("#########")
nums=[12,21,22,24,26]
for num in nums:
    if num %5==0:
       print(num)
       break
else:
    print("not found")"""
#prime num
print("$$$$$$$$$$")
"""num=7
for i in range(2,num):
    if num%i==0:
        print("its not prime num")
        break
else:
    print("its  prime ")"""





















