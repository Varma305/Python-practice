p=int(input("principal amount:"))
t=int(input("time:"))
r=int(input("rate of interest:"))

'''compound interest'''

amount=p*(1+r/100)**t
ci=amount-p
print(ci)

'''simple interest = p*t*r/100 '''

si=(p*t*r)/100
print(si)
