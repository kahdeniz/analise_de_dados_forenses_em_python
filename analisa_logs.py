import pandas as pd
import matplotlib.pyplot as plt
with open("system_logs.txt", "r") as f:
 linhas = f.readlines()
falhas = [linha for linha in linhas if "Failed password" in linha]
horas = [linha.split()[2].split(":")[0] for linha in falhas]
df = pd.DataFrame(horas, columns=["hora"])
contagem = df["hora"].value_counts().sort_index()
contagem.plot(kind="bar", color="red")
plt.title("Tentativas de Login Falhas por Hora")
plt.xlabel("Hora do Dia")
plt.ylabel("Numero de Tentativas")
plt.grid(True)
plt.tight_layout()
plt.show()
