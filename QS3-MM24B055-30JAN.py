# Python program to demonstrate
# difference between pass and 
# continue statements

s = "numbers";

# Pass statement
for i in s:
    if i == 'b':
        print('Pass executed')
        pass
    print(i)

print()
    
# Continue statement-return control back to start of the loop
for i in s:
    if i == 'b':
        print('Continue executed')
        continue
    print(i)
