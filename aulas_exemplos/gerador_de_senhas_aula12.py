from random import randint, choice, shuffle

def zero_nove():
    return chr(randint(48, 57))


def a_z_minusc():
    return chr(randint(97, 122))


def a_z_maiusc():
    return chr(randint(65, 90))


def caracteres_especiais():
    rand_range = [
        randint(33, 47),
        randint(58, 64)
    ]

    return chr(choice(rand_range))


def create_senha(
    length=12,
    number=True,
    upper=True,
    lower=True,
    chars=2
):
    password = []

    especial = True
    while len(password) < length:
        if especial and chars > 0:
            especial = False
            for c in range(chars):
                password.append(caracteres_especiais())
        if upper:
            password.append(a_z_maiusc())
        if lower:
            password.append(a_z_minusc())
        if number:
            password.append(zero_nove())
        
    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    
    lista_senhas = list()

    digitos = int(input('Senha de quantos dígitos: '))
    caracteres_esp = int(input('Quantos caracteres especiais deseja na senha: '))
    print()
    # VÁLIDAS
    for c in range(5):
        lista_senhas.append(create_senha(
            length= digitos,
            chars=caracteres_esp
            ))
    print()

    # SEM MAIUSCULAS
    for c in range(5):
        lista_senhas.append(create_senha(
            length= digitos,
            chars= caracteres_esp,
            upper= False
            ))
    print()

    # SEM MINUSCULAS
    for c in range(5):
        lista_senhas.append(create_senha(
            length= digitos,
            chars = caracteres_esp,
            lower= False,
            ))
    print()

    # SÓ NÚMEROS
    for c in range(5):
        lista_senhas.append(create_senha(
            length= digitos,
            chars = 0,
            lower= False,
            upper= False
            ))

    print(lista_senhas)
