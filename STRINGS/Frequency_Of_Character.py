def sample(a):
    alphabet = {}                 
    for i in a:                   
        if i.isspace() == False:  
            if i not in alphabet: 
                alphabet[i] = 1   
            else:
                alphabet[i] += 1  
    return alphabet 
print(sample("Hello World"))    

