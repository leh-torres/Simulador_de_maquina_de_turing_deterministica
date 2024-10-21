'''
MÁQUINA DE TURING DETERMINÍSTICA

(K, E, F, s, H)

K - conjunto de estados finitos
E - alfabeto
F - Função de transição
s - estado inicial
H - conjunto de estados de parada


Entrada: Máquina, palavra

configuração: (@#w)
@ -> marcador de inicio de fita
# -> espaço em branco

Máquina de exemplo:
Rb
K - {q0, q1}
E -  {@, B, a}
F - {q0, @Ba, e} |- {q0, @BaB, e}
    {q0, @Ba, a} |- {q0, @Baa, e}
    {q0, @BaB, e} |- {q1, @BaB, e}

     q0, a |- q0, ->
     q0, B |- h(q1), B
s - {q0}
H - {q1}
'''

from MT_deterministica import *

#funcao_de_trancisao[('q0', '#')][0]
funcao_de_trancisao_m1 = {
    ('q0', '@'): ('q0', '@', 'D'),
    ('q0', '#'): ('q1', '#', '_'),
    ('q0', 'a'): ('q0', 'a', 'D')
}

Maquina1 = MT_deterministica(['q0','q1'], ['@', '#', 'a'], funcao_de_trancisao_m1, 'q0', ['q1'], 0)
Maquina1.init_fita('@#aaa#')
Maquina1.init_maquina()

funcao_de_trancisao_m2 = {
    ('q0', '@'): ('q0', '@', 'D'),
    ('q0', '#'): ('q1', '#', '_'),
    ('q0', 'a'): ('q0', 'a', 'L')
}

#Maquina2 = MT_deterministica(['q0','q1'], ['@', '#', 'a'], funcao_de_trancisao_m2, 'q0', ['q1'])
#Maquina2.init_fita('@#aaa#')
#Maquina2.print_fita()
#Maquina2.init_maquina()

funcao_de_trancisao_m3 = {
    ('q0', '@'): ('q0', '@', 'D'),
    ('q0', '#'): ('q0', '#', 'D'),
    ('q0', 'a'): ('q1', 'a', '_')
}

#Maquina3 = MT_deterministica(['q0','q1'], ['@', '#', 'a'], funcao_de_trancisao_m3, 'q0', ['q1'])
#Maquina3.init_fita('@#####aaa#')
#Maquina3.init_maquina()

funcao_de_trancisao_m4 = {
    ('q0', '@'): ('q0', '@', 'D'),
    ('q0', '#'): ('q0', '#', 'L'),
    ('q0', 'a'): ('q1', 'a', '_')
}

#Maquina4 = MT_deterministica(['q0','q1'], ['@', '#', 'a'], funcao_de_trancisao_m4, 'q0', ['q1'])
#Maquina4.init_fita('@#aaa#####')
#Maquina4.init_maquina()

funcao_de_trancisao_copia = {

   ('q0', '#') : ('q1', '#', 'L'),
   
   ('q1', '@') : ('q1', '@', 'D'),
   
   ('q1', 'a') : ('q2', '#', 'D'),
   ('q2', 'a') : ('q2', 'a', 'D'),
   ('q2', '#') : ('q5', '#', 'D'),

   ('q5', 'a') : ('q5', 'a', 'D'),
   ('q5', '#') : ('q6', '#', '_'),

   ('q6', '#') : ('q7', 'a', 'L'),
   
   ('q7', 'a') : ('q7', 'a', 'L'),
   ('q7', '#') : ('q8', '#', 'L'),
   ('q8', 'a') : ('q8', 'a', 'L'),
   ('q8', '#') : ('q9', '#', '_'),

   ('q9', '#') : ('q1', 'a', 'L'),

   ('q1', '#') : ('q3', '#', 'D'),
   ('q3', 'a') : ('q3', 'a', 'D'),
   ('q3', '#') : ('q4', '#', '_'),
}

#Maquina5 = MT_deterministica(['q0','q1', 'q2', 'q3', 'q4', 'q5', 'q6'], ['@', '#', 'a'], funcao_de_trancisao_copia, 'q0', ['q4'])
#Maquina5.init_fita('@#aaa#')
#Maquina5.init_maquina()

funcao_de_trancisao_tab = {

   ('q0', '#') : ('q1', '#', 'L'),
   
   ('q1', '@') : ('q1', '@', 'D'),
   
   ('q1', 'a') : ('q2', '#', 'D'),
   ('q2', 'a') : ('q2', 'a', 'D'),
   ('q2', '#') : ('q5', '#', 'D'),

   ('q5', 'a') : ('q5', 'a', 'D'),
   ('q5', '#') : ('q6', '#', '_'),

   ('q6', '#') : ('q7', 'a', 'L'),
   
   ('q7', 'a') : ('q7', 'a', 'L'),
   ('q7', '#') : ('q8', '#', 'L'),
   ('q8', 'a') : ('q8', 'a', 'L'),
   ('q8', '#') : ('q9', '#', '_'),

   ('q9', '#') : ('q1', '#', 'L'),

   ('q1', '#') : ('q3', '#', 'D'),
   ('q3', 'a') : ('q3', 'a', 'D'),
   ('q3', '#') : ('q4', '#', '_'),
}

#Maquina6 = MT_deterministica(['q0','q1', 'q2', 'q3', 'q4', 'q5', 'q6'], ['@', '#', 'a'], funcao_de_trancisao_tab, 'q0', ['q4'])
#Maquina6.init_fita('@#aaa#')
#Maquina6.init_maquina()

funcao_de_trancisao_8 = {

   ('q0', '#'): ('q0', 'a', '_'),
   ('q0', 'a'): ('q0', '#', '_')
}

#Maquina8 = MT_deterministica(['q0'], ['@', '#', 'a'], funcao_de_trancisao_8, 'q0', [], 2)
#Maquina8.init_fita('@#aaa#')
#Maquina8.init_maquina()