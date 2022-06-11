import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC62b864b1459e25048511ad4d624fd434"
# Your Auth Token from twilio.com/console
auth_token  = "545d12265afb7b7dd9a2adb5df688a67"
client = Client(account_sid, auth_token)

# pandas

# openpyxl

#twilo


# Passo a Passo  de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho' ]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+5517991278923", 
            from_="+18456585471",
            body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        print(message.sid)        








# Para cada aquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for mais que 55.000 -> Envia um SMS com o nome, o mês e as vendas do vendedor 

# Caso não seja maior do que 55.000 não quero fazer nada


