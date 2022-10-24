class ControleRemoto:

    def __init__(self, televisao: str, comodo: str):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self) -> str:
        print('Canal avançado')

    def voltar_canal(self) -> str:
        print('Voltar o canal')

    def escolher_canal(self, canal) -> str:
        print('Alterado para o canal: {}'.format(canal))

controle_sala = ControleRemoto('Samsung', 'Sala')
print(controle_sala.televisao)
print(controle_sala.comodo)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)
