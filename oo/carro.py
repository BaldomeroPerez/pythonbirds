"""Voce deve criar uma classe carro que vai possuir 2 (dois) atributos compostos por outras duas classes
1) Motor
2) Direção
O o motor tera a responsabilidade de controlar a velocidade
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a vlocidade de uma unidade
3) Método frear, que devera decrementar a velocidade em 2 (duas) unidades

A Direção terá a responsabilidade de controlar a direção.Ela oferece os
seguintes atributos:
1)Valor de direção com valores possiveis: norte, sul, leste e oeste
2)Método girar_a_direita
3)Método girar_a_esquerda
     N
   L   O
     S
        Exemplo:
        >>> # Testando motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelecar()
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
        >>> motor.frear()
        >>> motor.velocidade
        0
        >>> # Testando Direcao
        >>> direcao = Direcao()
        >>> direcao.valor
        "Norte"
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        "Leste"
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        "Sul"
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        "Oeste"
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        "Norte"
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        "Oeste"
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        "Sul"
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        "Leste"
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        "Norte"
        >>> carro = Carro(diretao,motor)
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
        >>>carro.calcular direcao()
        "Norte"
        >>>carro.girar_a_direita()
        >>>carro.calcular direcao()
        "Leste"
        >>>carro.girar_a_esquerda()
        >>>carro.calcular direcao()
        "Norte"
        >>>carro.girar_a_esquerda()
        >>>carro.calcular direcao()
        "Oeste"
"""