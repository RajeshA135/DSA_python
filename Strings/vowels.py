# replacing vowels with *
def replace_vowel(s):
    vowels="AEIOUaeiou"
    res=""
    for i in s:
        if i in vowels:
            res+="*"
        else:
            res+=i
    print(res)
            
s=input("Enter a string:")
print(replace_vowel(s))