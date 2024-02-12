# Projeto coletar informações sobre faturamento de uma Loja e enviar por e-mail (G-mail) 

Resumo do que foi utilizado:
- Linguagem: Python
- Bibliotecas: pandas, smtplib e email.message

### Como usar?

Instalar o Python, caso não tenha, faça download no site oficial:
[Download Python](https://www.python.org/downloads/)

Com o Python instalado, faça download ou clone esse repositório (precisa ter o git configurado) em algum local do seu computador com o seguinte comando no terminal:

```
git clone https://github.com/rlippi/FaturamentoPorEmailGmail.git
```

Abra o projeto no seu editor de código, e instale a biblioteca pandas.
Como sugestão, pode criar um ambiente virtual para o projeto, embora não seja obrigatório. Para isso, é necessário abrir o terminal estando dentro da pasta do projeto. 
Veja como criar um ambiente virtual no Windows (rode uma linha de código por vez):

```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

Instalando a biblioteca:

```
pip install pandas
```

### Como funciona?

- Adicione nas linhas:
    - 59: troque 'Seu Nome' pelo seu nome;
    - 60: troque 'Seu Cargo' pelo seu cargo;
    - 65: troque 'remetente@gmail.com' pelo seu e-mail Gmail (precisa ser um e-mail do G-mail);
    - 66: troque 'destinatario@email.com.br' pelo destinatario desejado (não precisa ser e-mail do Gmail);
    - 67: adicione dentro de ' ' a sua SENHA DE APP do G-mail. Atenção esta não é a sua senha de usuário do Google, pesquise "senha de app no G-mail".

- Pronto, agora que já tem o projeto e a(s) biblioteca(s) na sua máquina, você pode executar o programa rodando o arquivo _**"FaturamentoPorEmailGmail.py"**_.


### Resultado
Pronto! Seu e-mail foi enviado com as tabelas solicitadas.

### Este projeto foi criado com base na Aula:
- Escola: Hashtag Programação (MiniCurso Gratuito Python)
- Link: https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_UBLgxgSjECwlink


# Fim
