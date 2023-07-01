import random

w=True
a1=0
a2=0

print("==========================================================================================")
print("#                                         ЧУВАЧІ                                         #")
print("==========================================================================================")
print(" ")
print("введіть ім'я першого гравця:")
player1=input()
print("введіть ім'я другого гравця:")
player2=input()
f1=open("предмети.txt", "r")
list=f1.readlines()
while w:
     v1=random.choice(list)
     v1=v1.strip()
     v2=random.choice(list)
     v2=v2.strip()
     print(player1, ":")
     print(v1)
     print(player2, ":")
     print(v2)
     if v1==v2:
          print("Нічія") 
          print("рахунок:", a1, "|", a2)
     elif v1=="Камінь" and v2=="Ножниці":
          a1=a1+1 
          print("Переміг:", player1) 
          print("рахунок:", a1, "|", a2)
     elif v1=="Ножниці" and v2=="Камінь": 
          a2=a2+1
          print("Переміг:", player2) 
          print("рахунок:", a1, "|", a2) 
     elif v1=="Ножниці" and v2=="Папір": 
          a1=a1+1
          print("Переміг:", player1) 
          print("рахунок:", a1, "|", a2)                
     elif v1=="Папір" and v2=="Ножниці": 
          a2=a2+1
          print("Переміг:", player2) 
          print("рахунок:", a1, "|", a2)
     elif v1=="Папір" and v2=="Камінь": 
          a1=a1+1
          print("Переміг:", player1) 
          print("рахунок:", a1, "|", a2)               
     elif v1=="Камінь" and v2=="Папір": 
          a2=a2+1
          print("Переміг:", player2) 
          print("рахунок:", a1, "|", a2)     
     else :
          print("щось не так")   
          
     n=input("Продовжити Так/Ні: ")
     if n=="Ні":
          w=False
     
     
