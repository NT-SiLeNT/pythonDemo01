print('hello world')


# for bbb in 'Python':     # 第一个实例
#    print('当前字母 :',bbb,'aaaa')

# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#    print('当前水果 :', fruit)

# fruits = ['banana', 'apple',  'mango']
# for i in range(len(fruits)):
#     print('当前水果 :', fruits[i])

for num in range(20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d * %d'%(num,i,j))
            break
        else:
            print(num, '是一个质数')
            break



