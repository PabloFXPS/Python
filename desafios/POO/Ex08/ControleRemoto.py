#Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples(canal(</>), volume(-/+), (@)liga e desliga)
from rich import print
from rich.panel import Panel

class Controle:
    def __init__(self):
        self.ligada = False
        self.canal_atual = 1
        self.volume_atual = 1

    def tv(self):
        if not self.ligada:
            painel = Panel("canal = ❌\nvolume = ❌",title="TV (DESLIGADA)",border_style="red",width=20)
        else:
            self.ligada = True
            painel = Panel(
                f"canal = [yellow]{self.canal_atual}[/yellow]\n"
                f"volume = [yellow]{self.volume_atual}[/yellow]",title="TV (LIGADA)",border_style="green",width=20)
        print(painel)

    def ligar(self):
        if self.ligada:
            self.ligada = False
            print("TV DESLIGADA")
        else:
            self.ligada = True
            print("TV LIGADA")

    def canais(self,comando):
        if not self.ligada:
            print("A tv esta desligada")
            return

        if comando == "<":
            self.canal_atual -= 1
            if self.canal_atual < 1:
                self.canal_atual = 1
                print("Limite atingido, voltando para o canal 1")

        if comando == ">":
            self.canal_atual += 1
            if self.canal_atual > 5:
                self.canal_atual = 5
                print("Limite atingido, voltando para o canal 5")

    def volume(self,comando):
        if not self.ligada:
            print("Tv desligada.")
            return

        if comando == "-":
            self.volume_atual -= 1
            if self.volume_atual < 1:
                self.volume_atual = 1
                print("Limite atingido, voltando para o volume 1")

        if comando == "+":
            self.volume_atual += 1
            if self.volume_atual > 5:
                self.volume_atual = 5
                print("Limite atingido, voltando para o volume 5")

tv = Controle()
while True:
    tv.tv()
    comandos = str(input("@ Liga e Desliga | < > Avança e retorna canais\n- + Aumenta e diminui o volume | s Sair\nComando:"))

    match comandos.lower():
        case "@":
            tv.ligar()
        case "<" | ">":
            tv.canais(comandos)
        case "+" | "-":
            tv.volume(comandos)
        case "s":
            print("Saindo..")
            break
