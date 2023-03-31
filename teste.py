# Definindo a função para calcular o Dutching e verificar se um investimento é bom ou ruim
def verificar_investimento(cotacoes, total_a_investir):
    # Cotacoes deve ser uma lista com duas ou três cotações
    if len(cotacoes) < 2 or len(cotacoes) > 3:
        return "Por favor, insira duas ou três cotações."
    # Calculando o resultado das divisões
    resultado = sum([1/c for c in cotacoes])
    # Calculando a porcentagem para cada cotação
    porcentagens = [1/(c*resultado) for c in cotacoes]
    # Calculando o valor a ser investido em cada cotação
    valores = [total_a_investir*p for p in porcentagens]
    # Verificando se o investimento é bom ou ruim
    if resultado > 1:
        return f"Não é um bom investimento. Valor a investir em cada opção: {valores}"
    else:
        return f"É um bom investimento. Valor a investir em cada opção: {valores}"

# Exemplo de uso da função com 3 cotações e um total a investir de R$100
cotacoes = [1.5, 4.00, 8.50] # substitua essas cotações pelas cotações que você obteve
total_a_investir = 100 # substitua esse valor pelo valor que você deseja investir
print(verificar_investimento(cotacoes, total_a_investir))