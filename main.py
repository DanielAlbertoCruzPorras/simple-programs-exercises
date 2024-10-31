firstWord = input("Insert  a word: ")
secondWord = input("Insert another word: ")
len1 = len(firstWord)
len2 = len(secondWord)
if len1>len2:
    num = len1-len2
    print(f"""The word "{firstWord}" has {num} letters more than "{secondWord}" """)
elif len2>len1:
    num = len2-len1
    print(f"""The word "{secondWord}" has {num} letters more than "{secondWord}" """)
else:
    print(f"""The word "{firstWord}" is as large as "{secondWord}" """)