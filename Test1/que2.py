#write a program to calculate simple intrest based on Principal, Rate and time(SI=P*R*T/100)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)