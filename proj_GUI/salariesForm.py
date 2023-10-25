salary = int(input("Enter amount of salary paid"))
def newSalary():
    return(salary)
def newTransport():
    return(salary*0.015)
def Health():
    return(salary*0.025)
def Feeding():
    return(salary*0.02)
def Clothing():
    return(salary*0.01)
def dues():
    return(salary*0.012)
def Taxes():
    return(salary*0.027)
def tot_allowance():
    return int(newTransport()+Health()+Feeding()+Clothing())

def tot_deduction():
    return int(dues() + Taxes())
netpay = int(salary + tot_allowance())
grosspay = int(salary +tot_deduction())

print(f'''
Total Allowance is {tot_allowance()}
Total Deduction is {tot_deduction()}
Netpay is {netpay}
Grosspay is {grosspay} 
''')