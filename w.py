
while True:
    a = int(input('请输入运费单价：'))
    b = int(input('计费重量：'))
    c = 100
    try:
        i = a * b + c
        print(f'总价：{i}')
    except:
        pass

