import pyautogui
import time

pyautogui.FAILSAFE = True

print("Automação iniciando em 3 segundos...")
time.sleep(3)

# Mover mouse até o Brave
pyautogui.moveTo(x=1255, y=1052, duration=1)

# Clicar no Brave
pyautogui.click()

# Esperar abrir
time.sleep(3)

# Ir até barra de pesquisa
pyautogui.moveTo(x=705, y=67, duration=1)

# Clicar na barra
pyautogui.click()

 #Escrever pesquisa
pyautogui.write("Curso Python", interval=0.1)

# Apertar Enter
pyautogui.press("enter")