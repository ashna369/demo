x=["data analytics","data science","digital marketing","ms word","global accounting"]
y=[50000,50000,54000,8000,45000]
print(x)
print(y)
print(type(x))
print(type(y))
print(len(x))
print(len(y))
x[4]="data administration"
print(x)
y[4]=48000
print(y)
x.append("global acconting")
print(x)
y.append(46000)
print(y)
x.insert(4,"computerised accounting")
print(x)
y.insert(4,52000)
print(y)
x.extend(y)
print(x)
x.remove("ms word")
y.remove(8000)
print(x)
print(y)
x.pop()
y.pop()
print(x)
print(y)
y.sort()
print(y)
del x[2]
del y[2]
print(x)
print(y)
#print(x.split(","))
y.sort(reverse=True)
print(y)
y=x.copy()
print(x)
z=x+y
print(z)
print(x.count("data administration"))
y.clear()
print(y)