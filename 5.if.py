blood = 20 #before blood

hurt = input('You were hurt:') #were hurt
hurt = int(hurt)

blood = blood - hurt  #after hurt

if blood <=0:
    print("BOSS KO!")
    print("Player victory!")
else:
    print("Player KO!:(")
