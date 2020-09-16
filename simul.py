import random

class Rolamento:
    def __init__(self,number):
        self.life = [1000,1100,1200,1300,1400,1500,1600,1700,1800,1900]
        self.prob = [0.10,0.13,0.25,0.13,0.09,0.12,0.02,0.06,0.05,0.05]
        self.prob_acc = [0.10,0.23,0.48,0.61,0.70,0.82,0.84,0.90,0.95,1.00]
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

class Mecanico:
    def __init__(self,number):
        self.number = number
        self.wait = [5,10,15]
        self.prob = [0.60,0.30,0.10]
        self.index = None

        self.getIndex()
    
    def getIndex(self):
        n = self.number
        if n <= 59:
            self.index = 0
        elif n <= 89:
            self.index = 1
        elif n <= 99:
            self.index = 2

# Define o número de rolamentos
rolamentos = 3
simulWaitTimes = []
simulLastSequences = []

for x in range(0,rolamentos):
    simulVec = []
    total_life = 0
    i = 1
    while total_life < 20000:
        r = Rolamento(random.randint(0,99))
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
        #print(simulStep)
        simulVec.append(simulStep)

    totalWaitTime = 0
    for item in simulVec:
        totalWaitTime += item['wait']
    simulWaitTimes.append(totalWaitTime)
    simulLastSequences.append(simulVec[-1:][0]['sequence'])

totalSumOfSim = 0
totalSumOfLastSequences = 0
for item in simulWaitTimes:
    totalSumOfSim += item
for item in simulLastSequences:
    totalSumOfLastSequences += item

rolCost = totalSumOfLastSequences * 20
waitMec = totalSumOfSim * 5
waitRol = totalSumOfLastSequences * 20 * 5
mecCost = totalSumOfLastSequences * 20 * 1
print("Custo dos rolamentos: $" + str(rolCost))
print("Custo da máquina parada esperando pelo mecânico: $" + str(waitMec))
print("Custo da máquina parada trocando rolamento: $" + str(waitRol))
print("Custo do mecânico: $" + str(mecCost))
print("Custo Total: $" + str(rolCost + waitMec + waitRol + mecCost))