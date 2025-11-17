class nivel_personagem:

    def __init__(self):
        self.vida = 400
        self.sanidade = 12
        self.nen = 28

    def escolher_classe(self):

        while True:
            classe = int(input(""""
                Qual a classe do seu personagem? 
                \n
                (1) Fortificador \n
                (2) Transmutador \n
                (3) Emissor \n 
                (4) Conjurador \n
                (5) Manipulador \n
                (6) Especialista 
                        
                """))
            self.classe = classe
            
            if classe in (1,2,3,4,5,6):
                print("Carregando...")
                break
            else:
                print("Escolha uma das opções acima")

    def status(self):
        self.nivel = int(input("Qual o nivel do seu personagem? \n"))
        self.vigor = int(input("Qual o vigor do seu personagem? \n"))

    def calcular(self):   
        if self.classe == 1:
            self.Fortificador()

        if self.classe == 2:
            self.Transmutador()

        if self.classe == 3:
            self.Emissor()

        if self.classe == 4:
            self.Conjurador()

        if self.classe == 5:
            self.Manipulador()

        if self.classe == 6:
            self.Especialista()

    def Fortificador(self):

        if self.nivel <= 4 and self.classe == 1:
            self.vida = self.vida + 70
            self.sanidade = self.sanidade + 1
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 30 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 1
            self.nen = self.nen + self.nivel * 128
            
        elif self.nivel <= 9 and self.classe == 1:
            self.vida = self.vida + 140
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 30 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 1
            self.nen = self.nen + self.nivel * 128
            
        elif self.nivel <= 14 and self.classe == 1:
            self.vida = self.vida + 210
            self.sanidade = self.sanidade + 3
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 30 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 1
            self.nen = self.nen + self.nivel * 128
            
        elif self.nivel <= 19 and self.classe == 1:
            self.vida = self.vida + 380
            self.sanidade = self.sanidade + 7
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 30 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 1
            self.nen = self.nen + self.nivel * 128
            
        elif self.nivel == 20 and self.classe == 1:
            self.vida = self.vida + 550
            self.sanidade = self.sanidade + 11
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 30 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 1
            self.nen = self.nen + self.nivel * 128
            
        else: 
            print("teste")

    def Transmutador(self):

        if self.nivel <= 4 and self.classe == 2:
            self.vida = self.vida + 50
            self.sanidade = self.sanidade + 1
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 9 and self.classe == 2:
            self.vida = self.vida + 100
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 14 and self.classe == 2:
            self.vida = self.vida + 150
            self.sanidade = self.sanidade + 3
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 19 and self.classe == 2:
            self.vida = self.vida + 270
            self.sanidade = self.sanidade + 7
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel == 20 and self.classe == 2:
            self.vida = self.vida + 390
            self.sanidade = self.sanidade + 11
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        else: 
            print("teste")   
    
    def Emissor(self):

        if self.nivel <= 4 and self.classe == 3:
            self.vida = self.vida + 40
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 9 and self.classe == 3:
            self.vida = self.vida + 80
            self.sanidade = self.sanidade + 4
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 14 and self.classe == 3:
            self.vida = self.vida + 120
            self.sanidade = self.sanidade + 6
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 19 and self.classe == 3:
            self.vida = self.vida + 240
            self.sanidade = self.sanidade + 12
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        elif self.nivel == 20 and self.classe == 3:
            self.vida = self.vida + 360
            self.sanidade = self.sanidade + 18
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 128
        else: 
            print("teste")    
    
    def Conjurador(self):

        if self.nivel <= 4 and self.classe == 4:
            self.vida = self.vida + 40
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 138
        elif self.nivel <= 9 and self.classe == 4:
            self.vida = self.vida + 80
            self.sanidade = self.sanidade + 4
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 138
        elif self.nivel <= 14 and self.classe == 4:
            self.vida = self.vida + 120
            self.sanidade = self.sanidade + 6
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 138
        elif self.nivel <= 19 and self.classe == 4:
            self.vida = self.vida + 210
            self.sanidade = self.sanidade + 12
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 138
        elif self.nivel == 20 and self.classe == 4:
            self.vida = self.vida + 300
            self.sanidade = self.sanidade + 18
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 138

    def Manipulador(self):

        if self.nivel <= 4 and self.classe == 5:
            self.vida = self.vida + 40
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 3
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 9 and self.classe == 5:
            self.vida = self.vida + 80
            self.sanidade = self.sanidade + 4
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 3
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 14 and self.classe == 5:
            self.vida = self.vida + 120
            self.sanidade = self.sanidade + 6
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 3
            self.nen = self.nen + self.nivel * 128
        elif self.nivel <= 19 and self.classe == 5:
            self.vida = self.vida + 210
            self.sanidade = self.sanidade + 13
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 3
            self.nen = self.nen + self.nivel * 128
        elif self.nivel == 20 and self.classe == 5:
            self.vida = self.vida + 300
            self.sanidade = self.sanidade + 20
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 10 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 3
            self.nen = self.nen + self.nivel * 128
        else: 
            print("teste")  
    
    def Especialista(self):

        if self.nivel <= 4 and self.classe == 6:
            self.sanidade = self.sanidade + 2
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 158
        elif self.nivel <= 9 and self.classe == 6:
            self.sanidade = self.sanidade + 4
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 158
        elif self.nivel <= 14 and self.classe == 6:
            self.sanidade = self.sanidade + 6
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 158
        elif self.nivel <= 19 and self.classe == 6:
            self.sanidade = self.sanidade + 12
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 158
        elif self.nivel == 20 and self.classe == 6:
            self.sanidade = self.sanidade + 18
            self.vigor = self.vigor * self.nivel
            self.vida = self.vida + self.nivel * 20 + self.vigor
            self.sanidade = self.sanidade + self.nivel * 2
            self.nen = self.nen + self.nivel * 158
        else: 
            print("teste")

    def exibir_status(self):
            print(f"Seu nivel é {self.nivel} \n vida: {self.vida} \n sanidade: {self.sanidade} \n nen: {self.nen}")

p = nivel_personagem()

p.escolher_classe()
p.status()
p.calcular()
p.exibir_status()