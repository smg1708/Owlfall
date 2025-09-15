class Personagem:
    def __init__(self, classe, nivel, vigor):
        self.classe = classe
        self.nivel = nivel
        self.vigor = vigor
        self.vida = 400
        self.sanidade = 12
        self.nen = 28

    def Fortificador(self):
        if self.classe == 1:
            if self.nivel <= 4:
                self.vida += 70
                self.sanidade += 1
            elif self.nivel <= 9:
                self.vida += 140
                self.sanidade += 2
            elif self.nivel <= 14:
                self.vida += 210
                self.sanidade += 3
            elif self.nivel <= 20:
                self.vida += 280
                self.sanidade += 4

            self.vida += self.nivel * 30 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 1
            self.nen += self.nivel * 128
            print(f"[Fortificador] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

    def Transmutador(self):
        if self.classe == 2:
            if self.nivel <= 4:
                self.vida += 50
                self.sanidade += 2
            elif self.nivel <= 9:
                self.vida += 100
                self.sanidade += 4
            elif self.nivel <= 14:
                self.vida += 150
                self.sanidade += 6
            elif self.nivel <= 20:
                self.vida += 200
                self.sanidade += 8

            self.vida += self.nivel * 25 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 2
            self.nen += self.nivel * 128
            print(f"[Transmutador] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

    def Emissor(self):
        if self.classe == 3:
            if self.nivel <= 4:
                self.vida += 60
                self.sanidade += 2
            elif self.nivel <= 9:
                self.vida += 120
                self.sanidade += 4
            elif self.nivel <= 14:
                self.vida += 180
                self.sanidade += 6
            elif self.nivel <= 20:
                self.vida += 240
                self.sanidade += 8

            self.vida += self.nivel * 28 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 2
            self.nen += self.nivel * 128
            print(f"[Emissor] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

    def Conjurador(self):
        if self.classe == 4:
            if self.nivel <= 4:
                self.vida += 40
                self.sanidade += 3
            elif self.nivel <= 9:
                self.vida += 80
                self.sanidade += 6
            elif self.nivel <= 14:
                self.vida += 120
                self.sanidade += 9
            elif self.nivel <= 20:
                self.vida += 160
                self.sanidade += 12

            self.vida += self.nivel * 20 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 3
            self.nen += self.nivel * 139
            print(f"[Conjurador] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

    def Manipulador(self):
        if self.classe == 5:
            if self.nivel <= 4:
                self.vida += 40
                self.sanidade += 4
            elif self.nivel <= 9:
                self.vida += 80
                self.sanidade += 8
            elif self.nivel <= 14:
                self.vida += 120
                self.sanidade += 12
            elif self.nivel <= 20:
                self.vida += 160
                self.sanidade += 16

            self.vida += self.nivel * 20 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 4
            self.nen += self.nivel * 128
            print(f"[Manipulador] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

    def Especialista(self):
        if self.classe == 6:
            if self.nivel <= 4:
                self.vida += 30
                self.sanidade += 3
            elif self.nivel <= 9:
                self.vida += 60
                self.sanidade += 6
            elif self.nivel <= 14:
                self.vida += 90
                self.sanidade += 9
            elif self.nivel <= 20:
                self.vida += 120
                self.sanidade += 12

            self.vida += self.nivel * 18 + (self.vigor * self.nivel)
            self.sanidade += self.nivel * 3
            self.nen += self.nivel * 159
            print(f"[Especialista] Nível: {self.nivel} | Vida: {self.vida} | Sanidade: {self.sanidade} | Nen: {self.nen}")

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
nivel = int(input("Digite o nível (1-20): "))
vigor = int(input("Digite o vigor: "))

p = Personagem(classe, nivel, vigor)

if classe == 1:
    p.Fortificador()
elif classe == 2:
    p.Transmutador()
elif classe == 3:
    p.Emissor()
elif classe == 4:
    p.Conjurador()
elif classe == 5:
    p.Manipulador()
elif classe == 6:
    p.Especialista()
else:
    print("Classe inválida!")
