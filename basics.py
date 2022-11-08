num=[12,14,16,18,20]
print(num)
print(num[2:5])
print(num[:6])
print(num[-1])

values=[9.5,'darshan',25]
print(values)    # all type of data can be used in python

mix=[num,values]
print(mix)
values.append(45)
print(values)

num.append(60) #add the valuve at the last in the list
               # insert helps ti add the values in between
print(num)

num.pop(1)  #14 will be deleted
print(num)

num.pop()  # here last valuve will be deleted
print(num)

num.extend([13,15,17,19])    #extending the list by adding the values to the list
print(num)

#inbuilt functions
print(max(num))   #maximum num

print(min(num))   #minimum num

print(sum(num))# total num

tup=(12,14,16)  #tuple is enclosed with round brackets
print(tup)

set={12,23,34,45,56,67}   #set never follows the sequence
print(set)

#Dictionary Python

data={1:'darshan', 2:'kiran', 4:'mahesh'}
print(data[1]) #printing  according to key value
#print(data[3]) #through the error where key is not avalable
print(data[2])

#another way is
print(data.get(1))# fetch the first key value

print(data.get(3))  #in this method it will through none if the key is not available

print(data.get(3,'not found'))  #if key 3 is not there then it will print not found

# How to mearg two list into a dictionary?
keys=['darshan','kiran','mahesh']
values=['python','java', 'js']
data=dict(zip(keys,values))  #we are zip the files of keys and values, and the adding to dIctionary
print(data)

#if you want to add value

data['ambi']='cs'
print(data)
#delete the data ambi

del data['ambi']  #deleting ambi from the data
print(data)

#new dictionary which will have dictionary and list inside

prog={'js':'atom', 'cs':'vs', 'python':['paycharm','subline'],'java':{'jse':'net beam','jee':'eclipse'}}
print(prog)

print(prog['python'])
print(prog['java']['jee'])

#converting float to int
a=5.6
b=int(a)  #converting float to int
print(type(b))

print(b)

#convert to complex
k=6
c=complex(b,k)
print(c)  #o/p (5+6j)

range(10)
print(range(10))
#o/p range(0,10)

#converting range to list
range(10)
print(list(range(10)))
#doubt print(list[range(10)])
#print even num from 1-10

 #range(2,10,2)
 #list (range(2))

x=2
y=3
print(x+y)





