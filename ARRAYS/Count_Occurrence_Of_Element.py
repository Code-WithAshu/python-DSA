# The Time Complexilty of counting the ocurrence of the element is O(n)

a=[1,2,3,4,5,2,3,2]
cnt=0
b=int(input("enter the element to be counted: "))
for i in a:
    if i == b:
        cnt+=1
print("The ocurrence of the element ",cnt)
