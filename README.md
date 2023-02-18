# SMTP Tester

SMTP Tester é um programa Python que permite testar o envio de emails usando os protocolos SMTP com autenticação TLS, SSL e sem autenticação.

## Funcionamento

O programa inicia pedindo que o usuário selecione um dos hosts pré-configurados ou que informe o endereço de um servidor SMTP. Depois, o usuário deve informar um nome de usuário e o endereço de email do destinatário do teste. Por fim, deve escolher uma das opções de teste: TLS, SSL ou sem autenticação.

### TLS

Se o usuário escolher a opção TLS, o programa usará a porta 587 para conectar-se ao servidor SMTP e enviará uma mensagem usando o protocolo STARTTLS.

### SSL

Se o usuário escolher a opção SSL, o programa usará a porta 465 para conectar-se ao servidor SMTP e enviará uma mensagem usando o protocolo SSL.

### Sem autenticação

Se o usuário escolher a opção sem autenticação, o programa usará a porta 25 para conectar-se ao servidor SMTP e enviará uma mensagem sem autenticação.

## Como usar

### Pré-requisitos

- Python 3.x
- Módulo `smtplib`
- Módulo `getpass`
- Módulo `colorama`

### Instalação

Para instalar o programa, faça o clone deste repositório ou baixe o arquivo `smtp_tester.py`.

### Execução

Para executar o programa, navegue até o diretório onde o arquivo `smtp_tester.py` foi salvo e execute o programa.

Insira o host, a conta de envio, a conta que vai receber, o metodo de criptografia e se necessário, a senha.
