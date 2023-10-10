''' write a program to calculate emi
    where emi=si+principle_amount/no of months
    where si=p*t*r/100'''
p=int(input("Enter principal amount"))
t=int(input("Enter time period"))
r=int(input("Enter simple rate"))
si=p*r*t/100
print("si:",si)
emi=(si+p)/(12*t)
print("EMI:",emi)
