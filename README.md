# Validador de CPF e CNPJ em Python

Projeto em Python para validação de **CPF** e **CNPJ** utilizando os algoritmos oficiais de cálculo dos dígitos verificadores.

O programa aceita números **com ou sem máscara**, identifica automaticamente se é CPF ou CNPJ e informa se o valor é válido ou inválido.

---

## 📌 Funcionalidades

- Aceita CPF ou CNPJ com ou sem formatação  
- Ex: `529.982.247-25`, `04252011000110`
- Remove automaticamente caracteres não numéricos
- Valida tamanho e bloqueia números repetidos
- Calcula dígitos verificadores conforme regras oficiais
- Retorna resultado diretamente no terminal (CLI)

---

## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Nenhuma biblioteca externa (apenas Python padrão)

---

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cpf-cnpj-validator.git
```

2. Acesse a pasta do projeto:

```bash
cd cpf-cnpj-validator
```

3. Execute o programa:

```bash
python main.py
```

4. Insira um CPF ou CNPJ quando solicitado.

## 🧪 Exemplos de uso

Entrada:

```bash
529.982.247-25
```

Saída:
```bash
CPF
Válido
```

Entrada:

04.252.011/0001-10


Saída:

CNPJ
Válido


Entrada:

111.111.111-11


Saída:

CPF
Inválido