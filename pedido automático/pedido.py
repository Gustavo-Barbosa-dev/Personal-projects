import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://www.natura.com.br/")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=273, y=230)
time.sleep(3)
pyautogui.click(x=322, y=285)
time.sleep(5)
pyautogui.scroll(-800)
time.sleep(2)
pyautogui.click(x=840, y=311)
time.sleep(2)
pyautogui.click(x=345, y=764)
time.sleep(2)
pyautogui.click(x=505, y=185)
time.sleep(2)
pyautogui.click(x=121, y=499)
time.sleep(2)
pyautogui.click(x=158, y=352)
time.sleep(5)
pyautogui.click(x=1598, y=280)
time.sleep(3)
pyautogui.click(x=1827, y=234)
time.sleep(2)
pyautogui.click(x=1487, y=288)

import pandas as pd

tabela = pd.read_csv("pedido.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1487, y=288)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.write(str(tabela.loc[linha, "quantidade"]))
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

