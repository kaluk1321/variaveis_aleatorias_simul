import random # Import da biblioteca random para ter acesso a randomização de números


"""
    Classe que define os atributos da primeira marca de Rolamentos:
    life -> Vida util do rolamento
    number -> Numero aleatorio que define os indices dos vetores acima
    index -> Definido com base no numero aleatorio
    getIndex() -> Funcao para obter o indice com base no numero aleatorio,
    definindo a probabilidade de cada indice
"""
class RolamentoA:
    def __init__(self,number):
        self.life = [1000,1100,1200,1300,1400,1500,1600,1700,1800,1900]
        self.number = number
        self.index = None
        self.getIndex()
    
    def getIndex(self):
        n = self.number
        if n <= 9:
            self.index = 0
        elif n <= 22:
            self.index = 1
        elif n <= 47:
            self.index = 2
        elif n <= 60:
            self.index = 3
        elif n <= 69:
            self.index = 4
        elif n <= 81:
            self.index = 5
        elif n <= 83:
            self.index = 6
        elif n <= 89:
            self.index = 7
        elif n <= 94:
            self.index = 8
        else:
            self.index = 9


"""
    Classe que define os atributos da segunda marca de Rolamentos:
    life -> Vida util do rolamento
    number -> Numero aleatorio que define os indices dos vetores acima
    index -> Definido com base no numero aleatorio
    getIndex() -> Funcao para obter o indice com base no numero aleatorio
"""
class RolamentoB:
    def __init__(self,number):
        self.life = [1400,1500,1600,1700,1800,1900,2000,1700,1800,1900]
        self.number = number
        self.index = None
        self.getIndex()
    
    def getIndex(self):
        n = self.number
        if n <= 6:
            self.index = 0
        elif n <= 13:
            self.index = 1
        elif n <= 21:
            self.index = 2
        elif n <= 27:
            self.index = 3
        elif n <= 35:
            self.index = 4
        elif n <= 40:
            self.index = 5
        elif n <= 49:
            self.index = 6
        elif n <= 64:
            self.index = 7
        elif n <= 75:
            self.index = 8
        else:
            self.index = 9


"""
    Classe que define os atributos do Mecânico
    wait -> Tempo de espera
    number -> Numero aleatorio que define os indices dos vetores acima
    index -> Definido com base no numero aleatorio
    getIndex() -> Funcao para obter o indice com base no numero aleatorio,
    definindo a probabilidade de cada indice
"""
class Mecanico:
    def __init__(self,number):
        self.number = number
        self.wait = [4,8,18]
        self.index = None
        self.getIndex()
    
    def getIndex(self):
        n = self.number
        if n <= 40:
            self.index = 0
        elif n <= 75:
            self.index = 1
        else:
            self.index = 2

# Define o número de rolamentos
rolamentos = 2

"""
    Código de simulação para o Rolamento A
    É gerado um número aleatório para o RolamentoA e para o Mecânico
    Com base nesse número é puxado os índices da classe referentes a
    vida útil e o tempo de espera do mecânico.
    Após o fim da simulação é adicionado em uma estrutura o tempo total
    de espera e as sequências de simulação.
"""
simulWaitTimesA = []
simulLastSequencesA = []

for x in range(1,rolamentos + 1): #somado + 1 devido ao range comecar em 1
    simulVec = []
    total_life = 0
    i = 1
    while total_life < 20000:
        r = RolamentoA(random.randint(0,99))
        m = Mecanico(random.randint(0,99))
        total_life += r.life[r.index]
        simulStep = { 
            "sequence": i,
            "rol_numb": r.number,
            "life": r.life[r.index],
            "total_life": total_life,
            "mec_numb": m.number,
            "wait": m.wait[m.index]
        }
        i += 1
        # Descomente a linha abaixo para ver as simulações
        print("[Marca A] " + "[Rolamento:" + str(x) + "] " + "[Passo:" + str(i) + "]:" + str(simulStep))
        simulVec.append(simulStep)

    totalWaitTime = 0
    for item in simulVec:
        totalWaitTime += item['wait']
    simulWaitTimesA.append(totalWaitTime)
    simulLastSequencesA.append(simulVec[-1:][0]['sequence'])
print("")
"""
    Código de simulação para o Rolamento B
    É gerado um número aleatório para o RolamentoB e para o Mecânico
    Com base nesse número é puxado os índices da classe referentes a
    vida útil e o tempo de espera do mecânico.
    Após o fim da simulação é adicionado em uma estrutura o tempo total
    de espera e as sequências de simulação.
"""
simulWaitTimesB = []
simulLastSequencesB = []
for x in range(1,rolamentos + 1): #somado + 1 devido ao range comecar em 1
    simulVec = []
    total_life = 0
    i = 1
    while total_life < 20000:
        r = RolamentoB(random.randint(0,99))
        m = Mecanico(random.randint(0,99))
        total_life += r.life[r.index]
        simulStep = { 
            "sequence": i,
            "rol_numb": r.number,
            "life": r.life[r.index],
            "total_life": total_life,
            "mec_numb": m.number,
            "wait": m.wait[m.index]
        }
        i += 1
        # Descomente a linha abaixo para ver as simulações
        print("[Marca B] " + "[Rolamento:" + str(x) + "] " + "[Passo:" + str(i) + "]:" + str(simulStep))
        simulVec.append(simulStep)

    totalWaitTime = 0
    for item in simulVec:
        totalWaitTime += item['wait']
    simulWaitTimesB.append(totalWaitTime)
    simulLastSequencesB.append(simulVec[-1:][0]['sequence'])

"""
    Realiza a soma de todos os tempos de espera e sequências
    para os rolamentos A e B
"""
totalSumOfWaitTimesA = 0
totalSumOfLastSequencesA = 0
for item in simulWaitTimesA:
    totalSumOfWaitTimesA += item
for item in simulLastSequencesA:
    totalSumOfLastSequencesA += item

totalSumOfWaitTimesB = 0
totalSumOfLastSequencesB = 0
for item in simulWaitTimesB:
    totalSumOfWaitTimesB += item
for item in simulLastSequencesB:
    totalSumOfLastSequencesB += item

"""
    Calcula os custos com base no modelo para os 
    rolamentos A e B
"""
rolCostA = totalSumOfLastSequencesA * 20
waitMecA = totalSumOfWaitTimesA * 5
waitRolA = totalSumOfLastSequencesA * 20 * 5
mecCostA = totalSumOfLastSequencesA * 20 * 1

rolCostB = totalSumOfLastSequencesB * 20
waitMecB = totalSumOfWaitTimesB * 5
waitRolB = totalSumOfLastSequencesB * 20 * 5
mecCostB = totalSumOfLastSequencesB * 20 * 1

"""
    Imprime o resultado para os 
    rolamentos A e B
"""
print("\n[Rolamento A] Custo dos rolamentos: $" + str(rolCostA))
print("[Rolamento A] Custo da máquina parada esperando pelo mecânico: $" + str(waitMecA))
print("[Rolamento A] Custo da máquina parada trocando rolamento: $" + str(waitRolA))
print("[Rolamento A] Custo do mecânico: $" + str(mecCostA))
print("[Rolamento A] Custo Total: $" + str(rolCostA + waitMecA + waitRolA + mecCostA))

print("\n[Rolamento B] Custo dos rolamentos: $" + str(rolCostB))
print("[Rolamento B] Custo da máquina parada esperando pelo mecânico: $" + str(waitMecB))
print("[Rolamento B] Custo da máquina parada trocando rolamento: $" + str(waitRolB))
print("[Rolamento B] Custo do mecânico: $" + str(mecCostB))
print("[Rolamento B] Custo Total: $" + str(rolCostB + waitMecB + waitRolB + mecCostB))