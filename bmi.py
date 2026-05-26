def calculate_bmi(height,weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight / (height * weight)
    return bmi
    
weight = calculate_bmi(weight=57,height=1.73)
if weight > 25 :
    print("Over Weight")
elif weight >= 18.5 and weight <= 25:
    print("Normal Weight")
elif weight < 18.5:
    print("Under Weight")