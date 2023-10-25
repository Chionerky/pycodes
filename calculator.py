while True:
    print("\n------------------------------------\n")
    
    ent1 = input("Enter a number, or Type STOP to End calculator: ")
    if ent1 == 'STOP':
        break
    elif not ent1.isdigit():
        print("Invalid entry, Only Numbers")
        continue
    else:
        num1 = int(ent1)
        
    cal = input("Enter an operator (+,-,*,/,%): ")
    
    ent2 = input("Enter a number: ")
    if not ent2.isdigit():
        print("Invalid entry, Only Numbers")
        continue
    else:
        num2 = int(ent2)
        
    if cal == '+':
        ans = num1 + num2
    elif cal == '-':
        ans = num1 - num2
    elif cal == '*':
        ans = num1 * num2
    elif cal == "/":
        ans = num1 / num2
    elif cal == "%":
        ans = num1 % num2
    elif cal == '**':
        ans = num1 ** num2
    else:
        print("Invalid input, Operators only!!!")
    print(num1, cal, num2, "=", ans)