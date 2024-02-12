# Lógica do Programa
    # 1. importar a base de dados
    # 2. vizualizar a base de dados
    # 3. faturamento total por Loja    
    # 4. quantidade de produtos vendidos por loja
    # 5. ticket médio por produto em cada loja
    # 6. enviar um e-mail com o relatório

# 0.IMPORTAR AS BIBLIOTECAS
#pandas - biblioteca que trás as tabelas para dentro do Python - interagem Python com Excel - pip install pandas
import pandas as pd

# 1.IMPORTAR A BASE DE DADOS
tabela_vendas = pd.read_excel('Vendas.xlsx')

# 2.VISUALIZAR A BASE DE DADOS
#pd.set_option(opcao, valor) --> pede para mostrar todas as colunas no terminal
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows' , None)
#print(tabela_vendas) #printa a tabela

#assim que verificamos que está lendo a base de dados corretamente, começamos a fazer as nossas contas

# 3.FATURAMENTO TOTAL POR LOJA
#tabela_vendas[['ID Loja', 'Valor Final']] # - exibe a coluna ID Loja e Valor Final
#tabela_vendas.groupby('ID Loja').sum() # - agrupa e soma
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().sort_values('Valor Final', ascending=False)
print(faturamento)

# 4. QUANTIDADE DE PRODUTOS VENDIDOS POR LOJA
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum().sort_values('Quantidade', ascending=False)
print(quantidade)

# 5. TICKET MÉDIO POR PRODUTO EM CADA LOJA # --> dividir a quantidade produtos pelo valor total
ticket_medio = (faturamento['Valor Final'] / quantidade ['Quantidade']).to_frame() #to frame para virar uma tabela
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Medio'})
print(ticket_medio)

# 6. ENVIAR E-MAIL COMO UM RELATÓRIO PELO G-MAIL
import smtplib #biblioteca que permite envio de e-mail 
import email.message #biblioteca que permite envio de e-mail 

def enviar_email():  
    corpo_email = f"""
    <p>Prezado(a)s,</p>
    <p></p>
    <p>Segue o relatório de vendas por Loja.</p>
    <p><b>Faturamento:</b></p>
    <p>{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}</p>
    <p><b>Quantidade Vendida:</b></p>
    <p>{quantidade.to_html()}</p>
    <p><b>Ticket Médio dos Produtos em cada Loja:</b></p>
    <p>{ticket_medio.to_html(formatters={'Ticket Medio': 'R${:,.2f}'.format})}</p>
    <p>Fico à disposição.</p>
    <p></p>
    <p>Att.,</p>
    <p></p>
    <p>Seu Nome</p>
    <p>Seu Cargo</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Projeto Python - Relatório de Vendas por Loja"
    msg['From'] = 'rementente@gmail.com'
    msg['To'] = 'destinatario@email.com.br'
    password = '' # colocar entre as aspas a sua senha de APP do G-mail (NÃÃÃÃO é a senha que vocë usa para entrar no gmail) --> pesquisa sobre senha de APP no Google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()