#Codigo produzido na aula de 2019-08-30
# 8o Periodo de Ciencia da Computacao do UNIFEG
#---------------------------------------
# Fazer o processamento de uma Perceptron Simples
# ou seja usar um neuronio para resolver a porta OR
#---------------------------------------
# legenda
# vt_ -> vetor
# vl_ -> valor
# --| criacao das estruturas de dados para processamento

# dataset com os valor de entrada do neuronio
# e saida esperada para cada amostra
dataset = [
 #   b   x1  x2  d
    [1,  0,  0,  0], # amostra 1
    [1,  0,  1,  1], # amostra 2
    [1,  1,  0,  1], # amostra 3
    [1,  1,  1,  1]  # amostra 4
]

# vetor peso
#     w0   w1   w2
vt_w = [1.0, 0.8, 0.9]

# taxa de aprendizado
vl_ta = 0.7

# funcao de soma
# referente a primeira parte do processamento do neuronio
# v_amostra -> vetor com as amostras origem do dataset
# v_peso -> vetor peso
def soma (vt_amostra, vt_peso):
    vl_total = 0 # variavel que tera o valor da soma
    # i -> idx da posicao processada do v_peso
    # v -> valor da posicao processada do v_peso
    for i, v in enumerate(vt_peso):
        vl_total += v * vt_amostra[i]

    return vl_total

# funcao de ativacao do neuronio
# esta a ser utilizado uma funcao degrau
# vl_soma -> valor da soma das entradas do neuronio
def funcao_ativacao(vl_soma):
    if vl_soma >= 0:
        return 1
    else:
        return 0

# funcao que calcula o erro da saida do neuronio
# vl_y -> eh a saida do neuronio
# vl_d -> eh a saida desejada pela rede
# ATENCAO!!!!!--> vl_d = len(vt_amostra) -1
def calcula_erro(vl_y, vl_d):
    return vl_d - vl_y

# funcao que faz a correcao dos pesos da rede
# vt_amostra -> vetor com as amostras de entrada
# vt_peso -> vetor com os pesos a serem corrigidos
# vl_erro -> valor do erro
# vl_taxa -> valor da taxa de aprendizado
def corrige_pesos(vt_amostra, vt_peso, vl_erro, vl_taxa):
    for i, v in enumerate(vt_peso):
        vt_peso[i] = v + (vt_amostra[i] * vl_erro * vl_taxa)

# bloco principal da rede

# laco principal que eh executado para processar uma epoca
# TODO o laco atual processa uma unica epoca, ou seja, nao
#      faz o treino a rede
#      FACA a correcao deste laco
for a in dataset:
    print (a)
    tmp_p = len(a) - 1
    tmp_soma = soma(a, vt_w)
    tmp_y    = funcao_ativacao(tmp_soma)
    tmp_erro = calcula_erro(tmp_y, a[tmp_p])

    print(vt_w)
    if (tmp_erro != 0):
        corrige_pesos(a, vt_w, tmp_erro, vl_ta)
        print (vt_w)



print('..| fim da aplicacao')
