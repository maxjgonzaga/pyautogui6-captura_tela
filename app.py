import subprocess
import pyautogui
import time

# Abrir o Bloco de Notas
subprocess.Popen('notepad.exe')

# Aguardar um pouco para que o Bloco de Notas tenha tempo de abrir completamente
pyautogui.sleep(2)

# Capturar um print da tela
screenshot = pyautogui.screenshot(region=(874,141,429,600))

# Salvar o screenshot como um arquivo PNG
screenshot.save('screenshot.png')

print("Screenshot capturado e salvo como 'screenshot.png'")