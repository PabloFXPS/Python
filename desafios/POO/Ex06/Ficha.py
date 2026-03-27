#Crie a classe Gamer, onde podemos cadastrar nome,nick e jogos favoritos de uma pessoa.
#Crie também um método que permita mostrar a ficha desse gamer.

from rich.panel import Panel
from rich import print
class Gamer:
    def __init__(self,nome:str,nick:str):
        self.nome = nome
        self.nick = nick
        self.jogos=list()

    def favorito(self,jogo:str):
        self.jogos.append(jogo)
        self.jogos.sort()

    def ficha(self):
        conteudo = f"Nome real: [black on white]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos: "
        for jg in self.jogos:
            conteudo += f"\n🎮 [yellow]{jg}[/]"
        ficha = Panel(conteudo,title=f"Jogador {self.nick}",width=32)
        print(ficha)

j1 = Gamer("Joao","JLZIM")
j1.favorito("GTA V")
j1.favorito("NFS Most Wanted")
j1.ficha()