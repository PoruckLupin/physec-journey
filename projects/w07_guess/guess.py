while True:
    import random
    Correct = random.randint(1,100)
    次数 = 0
    while True:
        answer = input("请输入你的猜测：")
        try:
            answer_float = float(answer)
        except ValueError:
            print("重新输入你的猜测")
            continue
        次数 = 次数 + 1
        if answer_float < Correct:
           print("你的猜测偏小，重新输入你的猜测")
           continue
        elif answer_float > Correct:
            print("你的猜测偏大，请再试一下吧")
            continue
        elif answer_float == Correct:
            break
    print("恭喜你，答对啦！")
    print("你这局的猜测次数为：",次数)
    again = input("你想再来一局吗(y/n)：")
    if again == "n":
        break     
