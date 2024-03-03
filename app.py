while True:
    try:
        val = int(input('단을 입력해주세요(종료: 0): '))
        if val == 0:
            print('프로그램을 종료합니다.')
            break
    except:
        print('다시 입력해주세요')
        continue
    for i in range(1, 10):
        print(f"{val} x {i} = {i * val}")