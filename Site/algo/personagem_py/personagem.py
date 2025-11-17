while True:

    vida = 400
    sanidade = 12
    nen = 28
    numeros = range(1,21)
    numeros_up = 1,5,10
    numeros_up_mais = 15,20
    numeros_up = [num for num in numeros if num not in numeros_up]
    numeros_up_mais = [num for num in numeros if num not in numeros_up_mais]

    classe = input(""""
        Qual a classe do seu personagem? 
        \n
        (1) Fortificador \n
        (2) Transmutador \n
        (3) Emissor \n 
        (4) Conjurador \n
        (5) Manipulador \n
        (6) Especialista 
                
        """)
    classe = int(classe)
    
    if classe in (1,2,3,4,5,6):
        print("Carregando...")
        break
    else:
        print("Escolha uma das opções acima")

nivel = int(input("Qual o nivel do seu personagem? \n"))
vigor = int(input("Qual o vigor do seu personagem? \n"))

def Fortificador():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 1:
        vida = vida + 70
        sanidade = sanidade + 1
        vigor = vigor * nivel
        vida = vida + nivel * 30 + vigor
        sanidade = sanidade + nivel * 1
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
        
    elif nivel <= 9 and classe == 1:
        vida = vida + 140
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 30 + vigor
        sanidade = sanidade + nivel * 1
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
        
    elif nivel <= 14 and classe == 1:
        vida = vida + 210
        sanidade = sanidade + 3
        vigor = vigor * nivel
        vida = vida + nivel * 30 + vigor
        sanidade = sanidade + nivel * 1
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
        
    elif nivel <= 19 and classe == 1:
        vida = vida + 380
        sanidade = sanidade + 7
        vigor = vigor * nivel
        vida = vida + nivel * 30 + vigor
        sanidade = sanidade + nivel * 1
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
        
    elif nivel == 20 and classe == 1:
        vida = vida + 550
        sanidade = sanidade + 11
        vigor = vigor * nivel
        vida = vida + nivel * 30 + vigor
        sanidade = sanidade + nivel * 1
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
        
    else: 
        print("teste")

def Transmutador():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 2:
        vida = vida + 50
        sanidade = sanidade + 1
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 9 and classe == 2:
        vida = vida + 100
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 14 and classe == 2:
        vida = vida + 150
        sanidade = sanidade + 3
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 19 and classe == 2:
        vida = vida + 270
        sanidade = sanidade + 7
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel == 20 and classe == 2:
        vida = vida + 390
        sanidade = sanidade + 11
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    else: 
        print("teste")   
  
def Emissor():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 3:
        vida = vida + 40
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 9 and classe == 3:
        vida = vida + 80
        sanidade = sanidade + 4
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 14 and classe == 3:
        vida = vida + 120
        sanidade = sanidade + 6
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 19 and classe == 3:
        vida = vida + 240
        sanidade = sanidade + 12
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel == 20 and classe == 3:
        vida = vida + 360
        sanidade = sanidade + 18
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    else: 
        print("teste")    
 
def Conjurador():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 4:
        vida = vida + 40
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 138
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 9 and classe == 4:
        vida = vida + 80
        sanidade = sanidade + 4
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 138
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 14 and classe == 4:
        vida = vida + 120
        sanidade = sanidade + 6
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 138
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 19 and classe == 4:
        vida = vida + 210
        sanidade = sanidade + 12
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 138
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel == 20 and classe == 4:
        vida = vida + 300
        sanidade = sanidade + 18
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 138
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")

def Manipulador():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 5:
        vida = vida + 40
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 3
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 9 and classe == 5:
        vida = vida + 80
        sanidade = sanidade + 4
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 3
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 14 and classe == 5:
        vida = vida + 120
        sanidade = sanidade + 6
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 3
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 19 and classe == 5:
        vida = vida + 210
        sanidade = sanidade + 13
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 3
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel == 20 and classe == 5:
        vida = vida + 300
        sanidade = sanidade + 20
        vigor = vigor * nivel
        vida = vida + nivel * 10 + vigor
        sanidade = sanidade + nivel * 3
        nen = nen + nivel * 128
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    else: 
        print("teste")  
   
def Especialista():

    global vida, sanidade, nen, vigor, nivel
    if nivel <= 4 and classe == 6:
        sanidade = sanidade + 2
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 158
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 9 and classe == 6:
        sanidade = sanidade + 4
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 158
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 14 and classe == 6:
        sanidade = sanidade + 6
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 158
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel <= 19 and classe == 6:
        sanidade = sanidade + 12
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 158
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    elif nivel == 20 and classe == 6:
        sanidade = sanidade + 18
        vigor = vigor * nivel
        vida = vida + nivel * 20 + vigor
        sanidade = sanidade + nivel * 2
        nen = nen + nivel * 158
        print(f"Seu nivel é {nivel} \n vida: {vida} \n sanidade: {sanidade} \n nen: {nen}")
    else: 
        print("teste")

if classe == 1:
    Fortificador()

if classe == 2:
    Transmutador()

if classe == 3:
    Emissor()

if classe == 4:
    Conjurador()

if classe == 5:
    Manipulador()

if classe == 6:
    Especialista()