while True:
    length = input("你的身高是多高(m):")
    try:
        length_float = float(length)
        if length_float <= 0:
          print("此数据不可靠")
        else:
            break
    except ValueError:
          print("此数据无法使用，请重新输入正确数据:")
while True:
    weight = input("你的体重是多少(kg):")
    try:
        weight_float = float(weight)
        if weight_float <= 0:
          print("此数据不可靠")
        else:  
            break
    except ValueError:
          print("此数据无法使用，请重新输入正确数据:")  
BMI = weight_float/length_float**2
print(f"BMI完整值(准确值):{BMI:.2f}")
print(f"BMI:{BMI:.1f}(保留值，可能会与实际有偏差)")
if BMI < 18.5:
  print("您的体重偏瘦")
elif BMI < 24.0:
  print("您的体重正常")
elif BMI < 28.0:
  print("您属于超重范围")
else:
  print("您属于肥胖范围")
