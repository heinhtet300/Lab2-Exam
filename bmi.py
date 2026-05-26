def calculate_bmi(height,weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight / (height * weight)
    if bmi > 25 :
        value = 1
    elif weight >= 18.5 and weight <= 25:
        value = 0
    elif weight < 18.5:
        value = -1
    return value
    
weight = calculate_bmi(weight=57,height=1.73)

