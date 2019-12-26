dic = {'name':'rakesh',"age":24,'key':'value',(1,2,3):123}
print(dic.get('val','not given'))
x=dic.values()
for i in x:
    print(i)
for i,j in dic.items():
    print(i,j)

a =[1,2,3,4]
b = [9,8,7,6]
x = {}
for i in range(len(a)-1):
    x[a[i]]=b[i]

print(x)