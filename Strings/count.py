# Counting vowels and consonents in a given string
def replace_vowel(s):
    vowels="AEIOUaeiou"
    v=0
    c=0
    for i in s:
        if i.isalpha():
            if i in vowels:
                v+=1
            else:
                c+=1
    print(f"vowels are: {v} and consonents are: {c}")
            
s=input("Enter a string:")
print(replace_vowel(s))