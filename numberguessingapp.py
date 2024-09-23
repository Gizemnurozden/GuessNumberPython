'''

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı diyerek buldurmaya çalışın (hak = 5)
** "random modülü" için "python random" şeklinde arama yapın
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random

number = random.randint(1,10)
health = int(input("How many time do you want right?"))
right = health
counter = 0
while right > 0:
    right -= 1
    
    counter += 1
    guess = int(input( "Guess a number: "))

    if number == guess:
        print(f"Congratilations! You got it {counter}. time. Your point {100 - ((100/health)*(counter-1))}")
        break
    elif number > guess:
        print("Guess a bigger number")

    elif number < guess:
        print("Guess a smaller number ")
    
    if right == 0:
        print(f'Your guess is over. The number is {number}')





