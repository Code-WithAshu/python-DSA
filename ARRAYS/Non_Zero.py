# Brute force Approach 
def non_zero():
    cnt=0
    for i in a :
        if i == 0:
            cnt+=1
        else:
            b.append(i)
    for i in range(cnt):
        b.append(0)


# Optimized Approach using pointers 
def Optimized():
    w=0
    for r in range (len(a)):
        if(a[r]!=0):
            a[w]=a[r]
            w+=1
    for i in range(w,len(a)):
        a[i]=0

a=[1,0,2,0,3,5]
b=[]
non_zero()
print("Brute Force Method: ",b)
Optimized()
print("optimized method: ",a)





