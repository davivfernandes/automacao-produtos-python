import pyautogui
import pandas as pd
import time
import getpass

pyautogui.PAUSE = 1

# Dados de login
email = input("fulano@gmail.com")
senha = getpass.getpass("1234feijaonoprato")

# Link do sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Abrir o site
pyautogui.hotkey("ctrl", "l")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Fazer login
pyautogui.click(x=638, y=474)
pyautogui.write(email)

pyautogui.press("tab")
pyautogui.write(senha)

pyautogui.press("enter")
time.sleep(4)

# Ler base de dados
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar produtos
for linha in tabela.index:

    pyautogui.click(x=666, y=321)

    # Código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observação
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    # Voltar para o topo
    pyautogui.scroll(5000)
