import time

# --- CONFIGURAÇÃO DE HUD (COORDENADAS DO FREE FIRE) ---
# Essas coordenadas (x, y) representam onde o clique vai acontecer na tela
controles = {
    "w": {"acao": "Andar Frente", "x": 200, "y": 800},
    "s": {"acao": "Andar Trás", "x": 200, "y": 900},
    "a": {"acao": "Esquerda", "x": 100, "y": 850},
    "d": {"acao": "Direita", "x": 300, "y": 850},
    "f": {"acao": "Pegar Item", "x": 1500, "y": 300},
    "space": {"acao": "Pular", "x": 1800, "y": 700},
    "r": {"acao": "Recarregar", "x": 1700, "y": 900},
    "click_esquerdo": {"acao": "ATIRAR", "x": 1600, "y": 750}
}

def executar_comando(tecla):
    """Simula a ação do mobilador"""
    if tecla in controles:
        info = controles[tecla]
        print(f"[CLEITIN-LOG] Tecla: {tecla.upper()} | Ação: {info['acao']} | Toque em: ({info['x']}, {info['y']})")
    else:
        print(f"[!] Tecla '{tecla}' não configurada.")

# --- INÍCIO DO PROGRAMA ---
print("======================================")
print("     CLEITIN MAPEADOR INICIADO       ")
print("   Status: Aguardando Periféricos    ")
print("======================================")

# Simulação de loop de jogo
try:
    while True:
        entrada = input("Simule uma tecla pressionada (ou 'sair'): ").lower()
        if entrada == 'sair':
            break
        executar_comando(entrada)
except KeyboardInterrupt:
    print("\nMapeador encerrado.")
