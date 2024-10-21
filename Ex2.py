class Motor:
    def status(self):
        return "Motor OK"


class Pneu:
    def status(self):
        return "Pneu com baixa pressão"


class Veiculo(Motor, Pneu):
    def __init__(self, modelo):
        self.modelo = modelo

    def status(self):
        motor_status = Motor.status(self)
        pneu_status = Pneu.status(self)
        return f'Status do Motor: {motor_status}\nStatus do Pneu: {pneu_status}\nStatus do Veiculo (modelo: {self.modelo})'


def main():
    modelo = input('Insira o modelo do veículo: ')
    veiculo = Veiculo(modelo)
    print(veiculo.status())

if __name__ == '__main__':
    main()
