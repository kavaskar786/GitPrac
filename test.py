
# butterfly
for i in range(1, 4): 
    print("*"*i + " "*(6-i*2) + "*"*i)
for i in range(2,0,-1): 
    print("*"*i + " "*(6-i*2) + "*"*i)



#square
print("----------------------------------- SQUARE -----------------------------------")
for i in range(4):
    if i ==1 or i == 2:
        print("*"+ " "* 2+ "*")
    else:
        print("****")
    

print("-------------------------------------ROMBUS------------------------------------")

#ROMBUS
for i in range(1,5):
    print(" "*(4-i)+i*"*"+(i-1)*"*")
for i in range(3,0,-1):
    print(" "*(4-i)+i*"*"+(i-1)*"*")