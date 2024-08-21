x=[10,15,32,"hello","hii"]
print(x)
print(type(x))
print(len(x))
print(10 in x)
print(34 in x)
print("hello" not in x)
print(34 not in x)
for i in x:
    print(i)
print(x[1])
print(x[2:4])
print(x[1:])
print(x[:5])
print(x[-1])
print(x[-4:-2])
print(x[-3:])
print(x[:-4])
x[1]=22
print(x) 
x.append("mango")
print(x)
x.insert(3,"ernakulam")
print(x)
y=["umbrella",2,6,"kannur",45]
print(y)
x.extend(y)
print(x)
x.remove("hello")
print(x)
x.pop(2)
print(x)
x.pop()
print(x)
del x[5]
print(x)
z=["apple","orange","grapes","banana"]
print(z)
z.sort()
print(z)
z.sort(reverse=True)
print(z)
x=z.copy()
print(x)
y=list(x)
print(y)
c=x+y
print(c)
print(z.count("apple"))
z.clear()
print(z)
del z
print(z)



