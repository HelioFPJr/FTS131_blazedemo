from behave import *
# behave -i Compra.feature --no-capture comando pra rodar
# para usar o And ou But, basta repetir o step anterior

# TODO: "desambiguar passo com PO"


@Given('que acesso o site da Blazedemo')
@Given('que acesso o portal da Blazedemo')
def que_acesso_o_site_da_blazedemo():
    print('Passo 1 - Abriu o site')


@When('pesquiso passagens de {origem} a {destino}')
def pesquiso_passagens_de_origem_a_destino(origem, destino):
    print(f'Passo 2 - pesquisou passagem de {origem} para {destino}')


@When('seleciono o primeiro voo')
def seleciono_o_primeiro_voo():
    print('Passo 3 - Selecionou o primeiro voo')


@When('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento():
    print('Passo 4  - Preencheu os dados de pagamento')


@Then('valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida():
    print('Passo 5 - Validou se passagem foi emitida')
