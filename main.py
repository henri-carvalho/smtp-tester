import smtplib
import getpass
import colorama
from colorama import Fore, Style

colorama.init()

def format_text(text, color=Fore.WHITE, style=Style.NORMAL):
    return f"{color}{style}{text}{Style.RESET_ALL}"

def create_title(title, symbol="#", width=100):
    left = (width - len(title) - 2) // 2
    right = width - left - len(title) - 2
    return format_text(f"{symbol * left} {title} {symbol * right}", color=Fore.BLUE, style=Style.BRIGHT)

print(create_title("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                                @
@   _____ __  __ _______ _____    _______ ______  _____ _______  @
@  / ____|  \/  |__   __|  __ \  |__   __|  ____|/ ____|__   __| @
@ | (___ | \  / |  | |  | |__) |    | |  | |__  | (___    | |    @
@  \___ \| |\/| |  | |  |  ___/     | |  |  __|  \___ \   | |    @
@  ____) | |  | |  | |  | |         | |  | |____ ____) |  | |    @
@ |_____/|_|  |_|  |_|  |_|         |_|  |______|_____/   |_|    @
@                                                                @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""))
input(format_text("\nPressione ENTER para continuar...", color=Fore.BLUE, style=Style.BRIGHT))

def create_message(user, to):
    return f"""From: {user}
To: {to}
Subject: TESTE SMTP

Email de teste de SMTP2."""

def tls_test(host, user, passwd, to):
    smtp = smtplib.SMTP(f'{host}', 587)
    smtp.starttls()
    smtp.login(user, passwd)
    try:
        smtp.sendmail(user, to, create_message(user, to))
        print("Email enviado")
    except:
        print("Não foi possível enviar o email")
    smtp.quit()

def ssl_test(host, user, passwd, to):
    smtp = smtplib.SMTP_SSL(f'{host}', 465)
    smtp.login(user, passwd)
    try:
        smtp.sendmail(user, to, create_message(user, to))
        print("Email enviado")
    except:
        print("Não foi possível enviar o email")
    smtp.quit()

def noauth_test(host, user, passwd, to):
    smtp = smtplib.SMTP(f'{host}', 25)
    try:
        smtp.sendmail(user, to, create_message(user, to))
        print("Email enviado")
    except:
        print("Não foi possível enviar o email")
    smtp.quit()
        
def main():
    # Recebe as entradas do usuário
    user = input("E-mail de envio: ")
    to = input("Para: ")
    host = input("Insira o servidor de saída: ")
    opcao = input("Opção (tls, ssl ou noauth): ")

    # Verifica a opção escolhida pelo usuário
    if opcao in ['tls', 'ssl']:
        passwd = getpass.getpass("Senha: ")
    else:
        passwd = ""

    # Chama a função de teste correspondente
    if opcao == 'tls':
        print("Testando TLS na porta 587")
        tls_test(host, user, passwd, to)
    elif opcao == 'ssl':
        print("Testando SSL na porta 465")
        ssl_test(host, user, passwd, to)
    elif opcao == 'noauth':
        print("Testando sem autenticação na porta 25")
        noauth_test(host, user, to)
    else:
        print("Opção inválida.")

main()
