import turtle


class Forma:
    def __init__(self, tartaruga):
        self.tartaruga = tartaruga

    def desenhar(self):
        pass


class Circulo(Forma):
    def desenhar(self):
        self.tartaruga.penup()
        self.tartaruga.goto(0, -50)
        self.tartaruga.pendown()
        self.tartaruga.circle(50)


class Quadrado(Forma):
    def desenhar(self):
        self.tartaruga.penup()
        self.tartaruga.goto(-50, 50)
        self.tartaruga.pendown()

        for _ in range(4):
            self.tartaruga.forward(100)
            self.tartaruga.right(90)


def main(tela, t):
    contagem = 0
    while True:
        opcao = int(input('Digite 1 para desenhar um círculo e 2 para desenhar um quadrado: '))

        if opcao == 1:
            contagem += 1
            tela.title("Círculo com Turtle")
            circulo = Circulo(t)
            circulo.desenhar()
        elif opcao == 2:
            contagem += 1
            tela.title("Quadrado com Turtle")
            quadrado = Quadrado(t)
            quadrado.desenhar()
        else:
            print("Opção inválida. Tente novamente.")
            continue

        t.penup()
        t.goto(0, 0)
        while True:
            continuar = input('Deseja continuar? [s/n]: ').lower().strip()
            if continuar == 'n':
                tela.bye()
                return contagem
            elif continuar == 's':
                t.clear()
                t.reset()
                break
            else:
                print('Comando Inválido. Tente novamente.')


if __name__ == "__main__":
    tela = turtle.Screen()
    t = turtle.Turtle()
    main(tela, t)
