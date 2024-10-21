from ControleDeEstados import *

class MT_deterministica:
    def __init__(self, conj_estados, alfabeto, fun_trans, estado_init, conj_estados_parada, cabecote):
        self.alfabeto = alfabeto
        self.fun_trans = fun_trans
        self.controle_de_estados = ControleDeEstados(conj_estados, estado_init, conj_estados_parada)
        self.cabecote = cabecote
        self.fita = []

    def init_fita(self, word):
        for s in word:
            self.fita.append(s)

    def mover_cabecote_dir(self):
        if self.cabecote not in range(1, len(self.fita)-1):
            self.fita.append('#')
            self.cabecote += 1
        else:
            self.cabecote += 1

    def mover_cabecote_esq(self):
        if self.cabecote == 0:
            self.cabecote = self.cabecote
        else:
            self.cabecote -= 1
    
    def escrever_na_fita(self, simbolo):
        if self.cabecote > 1:
            self.fita[self.cabecote] = simbolo

    def get_simbolo_fita(self):
        return self.fita[self.cabecote]    

    def print_maquina(self):
        print('Alfabeto:', self.alfabeto)
        print('Funcao de transicao:', self.fun_trans)
        print('Controle de estados')
        self.controle_de_estados.print_controle_de_estado()
        print('Cabeçote:', self.cabecote)
        print('Fita: ', self.fita)
    
    def print_fita(self):
        print(self.fita)
    
    def init_maquina(self):
        estado_atual = self.controle_de_estados.get_estado_atual()
        conj_estados_de_parada = self.controle_de_estados.get_estados_de_parada()
        print("Conj: ", conj_estados_de_parada)
        print("primeiro estado atual: ", estado_atual)

        i = 0

        while estado_atual not in conj_estados_de_parada:
            if i == 50:
                print('Deseja continuar o processamento? s/n')
                escolha = input()

                if escolha == 's':
                    continue
                else:
                    break 
            elif i == 100:
                print('Ainda quer continuar o processamento, princesa? s/n')
                escolha = input()

                if escolha == 's':
                    continue
                else:
                    break 

            estado_atual = self.controle_de_estados.get_estado_atual()
            simbolo_fita = self.get_simbolo_fita()
            estado, simbolo, dir_cabecote = self.fun_trans[(estado_atual, simbolo_fita)]

            if estado != estado_atual:
                self.controle_de_estados.set_estado_atual(estado)
                estado_atual = self.controle_de_estados.get_estado_atual()
            if simbolo != simbolo_fita:
                self.print_fita()
                self.escrever_na_fita(simbolo)
                self.print_fita()
            if dir_cabecote != '_':
                print('entrou')
                if(dir_cabecote == 'D'):
                    self.mover_cabecote_dir()
                else:
                    self.mover_cabecote_esq()
            print(self.fita)
            print(self.cabecote)
            print(estado_atual)
            print("--------")
            i += 1
        print(self.fita)
        print(self.cabecote)
        print("--------")
       