print("Choose one")
print("1.Meter to feet")
print("2.Feet to meter")
print("3.KM to miles")
print("4.MIL to KM")
choice = input("Enter Number: ")
def MIL_to_KM():
    km_in_miles = 1.60934
    num4 = input("Enter Miles: ")
    result4 = float(km_in_miles) * float(num4)
    print(result4)
def KM_to_MIL():
    miles_in_km = 0.621371
    num3 = input("Enter KMs: ")
    result3 = float(miles_in_km) * float(num3)
    print(result3)
def M_to_F():
    feet_in_meter = 3.28084
    num1 = input("Enter Meters: ")
    result1 = float(feet_in_meter) * float(num1)
    print(result1)
def F_to_M():
    meter_in_feet = 0.3048
    num2 = input("Enter feet: ")
    result2 = float(meter_in_feet) * float(num2)
    print(result2)
if choice == "1":
    M_to_F()
elif choice == "2":
    F_to_M()
elif choice == "3":
    KM_to_MIL()
elif choice == "4":
    MIL_to_KM()
else:
    print("Invalid")