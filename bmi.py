length = input("你的身高是多高:")
length_float = float(length)
weight = input("你的体重是多少:")
weight_float = float(weight)
BMI = weight_float/length_float**2
print("你的BMI为：",BMI)
