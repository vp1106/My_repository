#       QS7
str1,str2,str3,str4 = input("Enter 4 strings separated by a -").split("-")
words=[str1,str2,str3,str4]
result=" ".join(words)
print(result)

print(result.upper())

reversed_sentence = " ".join(reversed(result.split()))
print(reversed_sentence)

reversed_each_word = " ".join([word[::-1] for word in result.split("-")])
print(reversed_each_word)


