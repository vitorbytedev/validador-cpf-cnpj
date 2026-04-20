def limpar_entrada(entrada):
    return ''.join(char for char in entrada if char.isdigit())

def validar_cpf(cpf):
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(len(cpf)))
        digito = (soma * 10) % 11
        return '0' if digito == 10 else str(digito)

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    return cpf[-2:] == digito1 + digito2

def validar_cnpj(cnpj):
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calcular_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        digito = soma % 11
        return '0' if digito < 2 else str(11 - digito)

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    digito1 = calcular_digito(cnpj[:12], pesos1)
    digito2 = calcular_digito(cnpj[:13], pesos2)

    return cnpj[-2:] == digito1 + digito2


if __name__ == "__main__":
    entrada = input("Escreva CPF ou CNPJ: ")
    entrada = limpar_entrada(entrada)

    if len(entrada) == 11:
        print("CPF")
        print("Válido" if validar_cpf(entrada) else "Inválido")

    elif len(entrada) == 14:
        print("CNPJ")
        print("Válido" if validar_cnpj(entrada) else "Inválido")

    else:
        print("Número inválido")