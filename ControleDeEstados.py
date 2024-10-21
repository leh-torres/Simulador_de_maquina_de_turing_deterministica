from typing import Any

class ControleDeEstados():
    def __init__(self, conjunto_de_estados, estado_atual, estados_de_parada):
        self.conjunto_de_estados = conjunto_de_estados
        self.estado_atual = estado_atual
        self.estados_de_parada = estados_de_parada

    def get_conjunto_de_estados(self):
        return self.conjunto_de_estados
    
    def get_estado_atual(self):
        return self.estado_atual
    
    def get_estados_de_parada(self):
        return self.estados_de_parada
    
    def set_estado_atual(self, estado):
        self.estado_atual = estado
    
    def print_controle_de_estado(self):
        print(' Conjunto de estados: ', self.conjunto_de_estados)
        print(' Estado atual: ', self.estado_atual)
        print(' Estados de parada: ', self.estados_de_parada)