#filename : coffee.py
coffee = 10

while True:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 수는 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break  #블럭을 벗어날 때 사용(vs..return 함수를 벗어날때 사용)
    
print("휴식이 길어지면 몸이 아파집니다.")
