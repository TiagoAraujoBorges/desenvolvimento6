# import da biblioteca datetime para gerar ano e data atual
import datetime 

# aqui iniciamos o loop
while True:
    try:
        nome_completo = input("Digite seu nome completo: ")
        ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise ValueError("Ano de nascimento inválido.")
        break
    except ValueError as error:
        print(error)
        
# aqui fazemos o calculo de idade caso nenhum erro seja capturado acima
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

# aqui imprimimos o nome completo e a idade do usuário
print("Nome completo:", nome_completo)
print("Idade atual:", idade, "anos")