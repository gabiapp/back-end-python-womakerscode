# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self):
      self.ligado = False
      self.cor = "Vermelho"
      self.modelo = 2023
      self.velocidade = 0

    def ligar(self):
      self.ligado = True

    def desligar(self):
      self.ligado = False

    def acelerar(self):
      self.velocidade += 10

    def desacelerar(self):
      self.velocidade -= 10
      
# Crie uma instância da classe carro.
carro_alison = Carro()

print("Você está em seu carro, ele está ligado, clique em 1 para acelerar ou em 0 para desacelerar")
while True:
    # Faça o carro "andar" utilizando os métodos da sua classe.
    acelerar = int(input("Acelere ou freie:\n"))

    if acelerar == 1:
        carro_alison.acelerar()
        print(f"Você está dirigindo a {carro_alison.velocidade}km por hora")
    # Faça o carro "parar" utilizando os métodos da sua classe.
    elif acelerar == 0:
        carro_alison.desacelerar()
        print(f"Você está freando e sua velocidade é de {carro_alison.velocidade}km por hora")
    else: 
        print("Digite 0 ou 1 para que sua escolha seja devidamente interpretada")

    if carro_alison.velocidade == 0:
       print("Você está parado")
       break
print("Seu carro desligou")
    
    
