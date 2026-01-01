# The Time Complexity  is O(n) and Space Complexity of O(1)

def Vow_Con(a):
    v_count=0
    c_count=0
    for i in a:
        if i in "aeiouAEIOU":
            v_count+=1
        elif i.isalpha() and i not in "aeiouAEIOU":
            c_count+=1
    print("The Vowel Count is: ",v_count)
    print("The Consonant count is: ",c_count)
a=input("Enter the String: ")
result=Vow_Con(a)


# Vowel and Consonant Counting using Set 

def vow_con_count(a):
    v,c=0,0
    vowel={'a','e','i','o','u'}
    for i in a :
        if i.lower() in vowel :
            v+=1
        elif i.isalpha():
            c+=1
    print(f"The Number of Vowel Count is {v}")
    print(f"The Number of consonant count is {c}")
    
a=input("Enter the String:")
vow_con_count(a)
