import turtle


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def atribuir_ponto(self):
        try:
            self.x = int(input('Digite o ponto X: '))
            self.y = int(input('Digite o ponto Y: '))
        except ValueError:
            print('Digite um número inteiro!')
            return self.atribuir_ponto()


def main(tela, t):
    Ponto1 = Ponto(0, 0)
    tela.title('Ponto')

    while True:
        Ponto1.atribuir_ponto()
        t.goto(Ponto1.x, Ponto1.y)

        while True:
            option = int(input('1 - Continuar\n2 - Resetar tudo\n0 - Sair\nDigite: '))
            if option == 0:
                tela.bye()
                return
            elif option == 1:
                break
            elif option == 2:
                t.clear()
                t.reset()
                break
            else:
                print('Comando Inválido. Tente novamente.')


if __name__ == '__main__':
    tela = turtle.Screen()
    t = turtle.Turtle()
    main(tela, t)
