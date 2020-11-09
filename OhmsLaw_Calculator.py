#Sandbox test code for implementation for the real calculator

import numpy as np

R = input("Enter the Resistanc value (if uknown enter 0): ")
V = input("Enter the Voltage value (if uknown enter 0): ")
I = input("Enter the Current value (if uknown enter 0): ")
#P = input("Enter the Power value(if uknown enter 0): ")

if float(R) == 0:
	Calc_R = float(V) / float(I)
	print("The Resistance value is: %f " %Calc_R)

if float(V) == 0:
	Calc_V = float(R) * float(I)
	print("The Voltage value is: %f " %Calc_V)

if float(I) == 0:
	Calc_I = float(V) / float(R)
	print("The Current value is: %f " %Calc_I)

print("Calculation is done")