import pydirectinput
from pynput import keyboard
import threading

# --- CONFIGURAÇÕES DO HUD (X, Y) ---
# Ajuste esses números de acordo com a posição dos botões na sua tela
HUD = {
    'space': (1800, 700),  # Pular
    'r': (1700, 900),      # Recarregar
    'f': (1500, 400),      # Pegar loot
    'q': (300, 300),       # Trocar arma
}

print("=== CLEITIN MAPEADOR ATIVO ===")
print("Pressione ESC para fechar o mapeador")

def ao_pressionar(tecla):
    try:
        # Converte a tecla pressionada para texto
        char = tecla.char.lower()
        
        if char in HUD:
            x, y = HUD[char]
            # Usa pydirectinput para ser aceito pelo jogo (DirectX)
            pydirectinput.click(x, y)
            print(f"[!] Tecla {char}: Clicando em ({x}, {y})")
            
    except AttributeError:
        # Trata teclas especiais (como space)
        nome_tecla = str(tecla).replace('Key.', '')
        if nome_tecla in HUD:
            x, y = HUD[nome_tecla]
            pydirectinput.click(x, y)
            print(f"[!] Tecla {nome_tecla}: Clicando em ({x}, {y})")

def ao_soltar(tecla):
    if tecla == keyboard.Key.esc:
        # Para o mapeador
        return False

# Inicia o "ouvinte" do teclado em segundo plano
with keyboard.Listener(on_press=ao_pressionar, on_release=ao_soltar) as listener:
    listener.join()
