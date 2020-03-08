"""
VC deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2)Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado velocidade
2) Método Acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela ferece os
seguintes atributos:

1) Valor de direção com valores possíeis: Norte, Sul, Leste e Oeste
2) Metodo girar_a_direita
3) Metodo girar_a_esquerda

Exemplo:

>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> # Testando Direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Lest'
>>> direcao.girar_a_direita()
>>> direcao.valor
'sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Lest'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte"
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'Lest'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'

"""