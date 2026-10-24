import os
import matplotlib.pyplot as plt

# 1. Pontos conhecidos: (temperatura, corrente)
# Ponto 1: 0 °C -> 4 mA
# Ponto 2: 100 °C -> 20 mA
x1, y1 = 0, 4
x2, y2 = 100, 20

# 2. Cálculo dos coeficientes da reta y = a * x + b
a = (y2 - y1) / (x2 - x1)  # Coeficiente angular
b = y1 - a * x1            # Coeficiente linear

print("=== CALIBRACAO DO TERMOMETRO ===")
print(f"Coeficiente a (inclinacao): {a}")
print(f"Coeficiente b (ponto inicial): {b}")
print(f"Equacao: Corrente (mA) = {a} * Temperatura (C) + {b}\n")

def avaliar_termometro(temperatura):
    """Calcula a corrente, valida os limites e classifica a temperatura."""
    corrente = a * temperatura + b

    print(f"--- Analise para {temperatura} C ---")
    print(f"Corrente calculada: {corrente:.2f} mA")

    # Aviso para limites de temperatura (0 a 100 °C)
    if temperatura < 0 or temperatura > 100:
        print("[AVISO] Temperatura fora da faixa permitida (0 C a 100 C)!")
    else:
        print("[OK] Temperatura dentro da faixa permitida (0 C a 100 C).")

    # Aviso para limites de corrente (4 a 20 mA)
    if corrente < 4 or corrente > 20:
        print("[AVISO] Corrente fora da faixa operacional (4 mA a 20 mA)!")
    else:
        print("[OK] Corrente dentro da faixa operacional (4 mA a 20 mA).")

    # Classificação da temperatura
    if temperatura <= 30:
        classificacao = "Baixa (ate 30 C)"
    elif temperatura <= 60:
        classificacao = "Media (de 30 C ate 60 C)"
    else:
        classificacao = "Alta (acima de 60 C)"

    print(f"Classificacao: {classificacao}\n")
    return corrente

# Testando com a temperatura de 50 graus
temp_teste = 50
corrente_teste = avaliar_termometro(temp_teste)

# 3. Geração do gráfico com Matplotlib (eixo x = temperatura, eixo y = corrente)
temperaturas_grafico = [0, 20, 40, 60, 80, 100]
correntes_grafico = [a * t + b for t in temperaturas_grafico]

plt.figure(figsize=(8, 5))
plt.plot(temperaturas_grafico, correntes_grafico, color="blue", marker="o", label="Curva 4-20 mA")

# Destaca o ponto testado (50 °C)
plt.plot(temp_teste, corrente_teste, marker="*", markersize=14, color="red", label=f"Ponto Teste ({temp_teste} C, {corrente_teste:.1f} mA)")

# Faixas visuais de classificação
plt.axvspan(0, 30, color="green", alpha=0.15, label="Baixa (<= 30 C)")
plt.axvspan(30, 60, color="orange", alpha=0.15, label="Media (30-60 C)")
plt.axvspan(60, 100, color="red", alpha=0.15, label="Alta (> 60 C)")

plt.title("Relacao Temperatura (C) vs Corrente Eletrica (mA)")
plt.xlabel("Temperatura (C)")
plt.ylabel("Corrente Eletrica (mA)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Salvando a imagem na pasta resultados/ conforme as regras do projeto
os.makedirs("resultados", exist_ok=True)
caminho_grafico = os.path.join("resultados", "grafico_termometro.png")
plt.savefig(caminho_grafico, dpi=300, bbox_inches="tight")
print(f"Grafico salvo com sucesso em: {caminho_grafico}")
