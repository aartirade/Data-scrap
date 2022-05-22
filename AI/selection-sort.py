def sort(num):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if num[j]<num[minpos]:
                minpos=j
        
        temp = num[i]
        num[i]=num[minpos]
        num[minpos]= temp
    
num= [6,1,5,3,8,4]
sort(num)
print(num)