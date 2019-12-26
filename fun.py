print("somthin intersting")

def find_value(tosearch,target):
    for i,value in enumerate(tosearch):
        if value ==target:
            return i
    return -1
print(find_value([1,2,3,4],4))

for i, j in enumerate([1,2,3,4]):
    if j== 3:
        print(i,j)

