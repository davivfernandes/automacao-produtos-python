import pyautogui
import time
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=455, y=924)
pyautogui.press("enter") 
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=638, y=474)
pyautogui.write("davifernandes150410@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
time.sleep(4)
#base de dados cabulosa
import pandas as pd
import openpyxl
tabela = pd.read_csv(r"C:\Users\davif\Downloads\produtos (1).csv")
print(tabela)
#cadastrar produto
for linha in tabela.index:
    #codigo
    pyautogui.click(x=666, y=321)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs!= "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.press("enter")
    pyautogui.scroll(5000)
         
   