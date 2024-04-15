tuple1= ("leo","cancer","gemini","scorpio","Taurus","aries")
tuple2= (1,4,6,9,3,12,10,7)

print (tuple1[2])
print(tuple1[-6:-1])
print(tuple1[-1])
print(tuple1[1: ])

y=list(tuple1)
y[3]= "virgo"
tuple1 = tuple(y)
print(tuple1)

x= tuple1 + tuple2
print(x)

fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits

print(a)
print(b)
print(c)

for a in fruits:
    print(a)
    
for i in range(len(tuple1)):
    print(tuple1[i])
    
    
age= (20,21,22,23,24,25,26)
i= 0
while i< len(age):
    print(age[i])
    i=i+1
    
fruits2= fruits*2
print(fruits2)