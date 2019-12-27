x = "Rakesh Kumar Reddy"
#print(x.__dir__())
if not 0:
    print('rakhi')
if not False:
    print('rakesh')
print('not raakeh')
y = """multi line string 
write something intresting"""
print(x[2:5])
print(x.startswith("Ra"))
print(x.lower())
print(x.count("K"))


"""find number of 'k'in string x"""
count = 0
for i in x:
    if "k"==i:
        count +=1
print(count)

"replacing string value"
x ="rakesh kumar reddy"
x=x.replace("kumar",'sree')
print(x)

"""formating"""
print("my name is{},and age is {} ".format("rakesh kumar",24))
print(x.split(" "))
print(x.join("11111111111111"))
