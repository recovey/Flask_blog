a = '$'
b = '￥'
i = 0.16
while True:  # while True是死循环，除非遇到break，不然程序不会结束(退出)
    result = input("请输入货币类型($/￥)，输入其他退出：")  # 接收用户输入
    if result == a or result == b:  # if 判断 如果用户输入的内容和a 或者 b 相同，证明用户想要转换金额，继续往下走
        sum = float(input("请输入兑换金额："))  # 用户输入金额
        sumresult = 0  # 用来存放转换后的结果
        if result == a:  # if 判断是否想用a转换
            sumresult = sum*i
            print("换算后金额为：", sumresult)
        else:   # 上面if不成立那么用户就是想用b转换
            sumresult = sum/i
            print("换算后金额为：", sumresult)
    else:   # if 不成立走 else 退出程序
        print("谢谢使用")
        break   #终止死循环