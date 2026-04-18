import pyautogui
import time
import sys

# Configurações iniciais
pyautogui.FAILSAFE = True
LARGURA, ALTURA = pyautogui.size()
CENTRO_X, CENTRO_Y = LARGURA // 2, ALTURA // 2

# Estado do mouse (False = Câmera travada/Mapeador ativo, True = Mouse livre)
mouse_livre = False

def alternar_mouse():
    global mouse_livre
    mouse_livre = not mouse_livre
    if not mouse_livre:
        pyautogui.moveTo(CENTRO_X, CENTRO_Y)
        print(">>> MODO COMBATE: Mouse travado na câmera.")
    else:
        print(">>> MODO CURSOR: Mouse liberado.")

print(f"--- CLEITIN MAPEADOR V2 ---")
print(f"Resolução detectada: {LARGURA}x{ALTURA}")
print("Pressione 'M' para simular o bloqueio de câmera (Exemplo)")

try:
    while True:
        if not mouse_livre:
            # Mantém o mouse no centro para o jogo entender o giro de câmera
            # Em um mapeador real, aqui capturaríamos o deslocamento (delta)
            pyautogui.moveTo(CENTRO_X, CENTRO_Y)
        
        # Simulação de comando via terminal para teste
        cmd = input("Comando (m = travar/destravar, s = sair): ").lower()
        
        if cmd == 'm':
            alternar_mouse()
        elif cmd == 's':
            break

except KeyboardInterrupt:
    print("\nSaindo...")
