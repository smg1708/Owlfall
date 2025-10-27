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

        bonus_por_nivel = {
            1:  (100, 3, 128),
            2:  (30, 1, 128),
            3:  (30, 1, 128),
            4:  (30, 1, 128),
            5:  (100, 3, 128),
            6:  (30, 1, 128),
            7:  (30, 1, 128),
            8:  (30, 1, 128),
            9:  (30, 1, 128),
            10: (100, 3, 128),
            11: (30, 1, 128),
            12: (30, 1, 128),
            13: (30, 1, 128),
            14: (30, 1, 128),
            15: (200, 6, 128),
            16: (30, 1, 128),
            17: (30, 1, 128),
            18: (30, 1, 128),
            19: (30, 1, 128),
            20: (200, 6, 128)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor

    def Transmutador(self):

        bonus_por_nivel = {
            1:  (70, 3, 128),
            2:  (20, 2, 128),
            3:  (20, 2, 128),
            4:  (20, 2, 128),
            5:  (70, 3, 128),
            6:  (20, 2, 128),
            7:  (20, 2, 128),
            8:  (20, 2, 128),
            9:  (20, 2, 128),
            10: (70, 3, 128),
            11: (20, 2, 128),
            12: (20, 2, 128),
            13: (20, 2, 128),
            14: (20, 2, 128),
            15: (140, 6, 128),
            16: (20, 2, 128),
            17: (20, 2, 128),
            18: (20, 2, 128),
            19: (20, 2, 128),
            20: (140, 6, 128)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor 
    
    def Emissor(self):

        bonus_por_nivel = {
            1:  (60, 4, 128),
            2:  (20, 2, 128),
            3:  (20, 2, 128),
            4:  (20, 2, 128),
            5:  (60, 4, 128),
            6:  (20, 2, 128),
            7:  (20, 2, 128),
            8:  (20, 2, 128),
            9:  (20, 2, 128),
            10: (60, 4, 128),
            11: (20, 2, 128),
            12: (20, 2, 128),
            13: (20, 2, 128),
            14: (20, 2, 128),
            15: (120, 8, 128),
            16: (20, 2, 128),
            17: (20, 2, 128),
            18: (20, 2, 128),
            19: (20, 2, 128),
            20: (120, 8, 128)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor   
    
    def Conjurador(self):

        bonus_por_nivel = {
            1:  (50, 4, 138),
            2:  (10, 2, 138),
            3:  (10, 2, 138),
            4:  (10, 2, 138),
            5:  (50, 4, 138),
            6:  (10, 2, 138),
            7:  (10, 2, 138),
            8:  (10, 2, 138),
            9:  (10, 2, 138),
            10: (50, 4, 138),
            11: (10, 2, 138),
            12: (10, 2, 138),
            13: (10, 2, 138),
            14: (10, 2, 138),
            15: (100, 8, 138),
            16: (10, 2, 138),
            17: (10, 2, 138),
            18: (10, 2, 138),
            19: (10, 2, 138),
            20: (100, 8, 138)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor

    def Manipulador(self):

        bonus_por_nivel = {
            1:  (50, 5, 128),
            2:  (10, 3, 128),
            3:  (10, 3, 128),
            4:  (10, 3, 128),
            5:  (50, 5, 128),
            6:  (10, 3, 128),
            7:  (10, 3, 128),
            8:  (10, 3, 128),
            9:  (10, 3, 128),
            10: (50, 5, 128),
            11: (10, 3, 128),
            12: (10, 3, 128),
            13: (10, 3, 128),
            14: (10, 3, 128),
            15: (100, 10, 128),
            16: (10, 3, 128),
            17: (10, 3, 128),
            18: (10, 3, 128),
            19: (10, 3, 128),
            20: (100, 10, 128)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor  
    
    def Especialista(self):

        bonus_por_nivel = {
            1:  (20, 4, 158),
            2:  (20, 2, 158),
            3:  (20, 2, 158),
            4:  (20, 2, 158),
            5:  (20, 4, 158),
            6:  (20, 2, 158),
            7:  (20, 2, 158),
            8:  (20, 2, 158),
            9:  (20, 2, 158),
            10: (20, 4, 158),
            11: (20, 2, 158),
            12: (20, 2, 158),
            13: (20, 2, 158),
            14: (20, 2, 158),
            15: (40, 8, 158),
            16: (20, 2, 158),
            17: (20, 2, 158),
            18: (20, 2, 158),
            19: (20, 2, 158),
            20: (40, 8, 158)
        }

        vida_ganha = 0
        san_ganha = 0
        nen_ganho = 0

        for lvl in range(1, self.nivel + 1):
            vd, san, nen = bonus_por_nivel[lvl]
            vida_ganha += vd
            san_ganha += san
            nen_ganho += nen

        self.vida += vida_ganha
        self.sanidade += san_ganha
        self.nen += nen_ganho

        self.vida += self.vigor
        self.sanidade += self.vigor  

    def exibir_status(self):
            print(f"Seu nivel é {self.nivel} \n vida: {self.vida} \n sanidade: {self.sanidade} \n nen: {self.nen}")

p = nivel_personagem()

p.escolher_classe()
p.status()
p.calcular()
p.exibir_status()