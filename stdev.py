import csv
import math

with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#finding mean

def mean(data):
    n=len(data)
    total=0

    for x in data:
        total+=int(x)

    mean=total/n
    print(mean)
    return mean

#squiring and getting values

squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)
print(squared_list)
#getting the sum
sum=0
for i in squared_list:
    sum=sum+i
print(sum)
#dividing sum by total values
result=sum/(len(data)-1)
print(result)
#getting deviation by square route of result

std_deviation=math.sqrt(result)
print(std_deviation)