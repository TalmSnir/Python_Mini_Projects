import math;


print("N\u03C3 cal ")
theory_value=float(input("enter the theory value: "))
theory_error=float(input("enter the theory error: "))
mes_value=float(input("enter the measurement value: "))
mes_error=float(input("enter the measurement error: "))
N_sigma=abs(theory_value-mes_value)/(math.sqrt(theory_error**2+mes_error**2))

print(f"The N\u03C3 is: {N_sigma}")

if N_sigma>3:
    print("The N\u03C3 is bad!!!")
else:
    print("The N\u03C3 is good")

instrument_res=float(input("enter the instrument res in cm: "))
instrument_error=instrument_res/math.sqrt(12)
print("the instrument error is: {} cm".format(instrument_error))

measurement=[]
number_of_mes=int(input("enter the number of measurement you have: "))
for i in range(0,number_of_mes):
    measurement.append(float(input(f"Enter {i+1} measurement: ")))

E=sum(measurement)/number_of_mes
print("the E is: {}".format(E))

sigma=0
for mes in measurement:
    sigma+=(mes-E)**2
sigma=math.sqrt(sigma/(number_of_mes-1))

print(f"the \u03C3 is: {sigma}")

total_error=math.sqrt(((sigma)/math.sqrt(number_of_mes))**2+instrument_error**2)

print()
print(f"The total error is: {total_error}")