#骰子遊戲: 玩家輸入一個數字，隨機產生一個數字，互相退抗直到玩家輸為止
#最後會輸出玩家共營幾次平手幾次
import random
m=0
n=0
while True: 
    x=int(input())
    i=random.randint(1,6)
    print("i=",i)
    if x>6 or 0>x:
        print("請重新輸入")
        continue
    else:
        if x>i:
            print("You win!")
            m+=1
        elif x==i:
            print("Try again")
            n+=1
        else:
            print("You lose!")  
            break    
print("共贏：",m)    
print("打平：",n)