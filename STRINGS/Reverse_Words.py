# The Code has Time and Space Complexity of O(n)
def reverse_word(s):

    words = s.split()
    words.reverse()
    return ' '.join(words)

a = "Ashu is Goat"
b = reverse_word(a)
print("The Words after Reversal:", b)
