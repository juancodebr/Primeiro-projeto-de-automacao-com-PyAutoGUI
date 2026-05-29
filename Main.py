import pyautogui
import time

pyautogui.FAILSAFE = True

print("Iniciando automação...")
time.sleep(3)

# Abrir menu iniciar
pyautogui.press("win")

time.sleep(1)

# Procurar Chrome
pyautogui.write("chrome", interval=0.1)

time.sleep(1)

# Abrir Chrome
pyautogui.press("enter")

# Esperar abrir
time.sleep(3)

# Ir para barra de pesquisa/endereço
pyautogui.hotkey("ctrl", "l")

# Digitar pesquisa
pyautogui.write("Curso Python", interval=0.1)

# Pesquisar
pyautogui.press("enter")