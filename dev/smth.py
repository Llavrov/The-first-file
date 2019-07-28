import random
#value = int(random.uniform(1,100))
#random.uniform(1,100) для добавления целых чисел от 1 до 100 ,а также дробных 
#random.random() для добавления любого дробного числа не более 1 
#rendom.randint(1,6) только челые числа от 1 до 6
#random.choice(аргумент) будет выводить слова из списка , который будет выбран.
#random.choice(аргумент, weights=[шанс выпадения], k=[10 - количество аргументов] )
'''
car = list(range(1, 10)) вызывает 51 число 
random.shuffle(car)  делает каждое число рандомным
'''
car = list(range(1, 100))
stup = random.sample(car, k=6)
print(stup)