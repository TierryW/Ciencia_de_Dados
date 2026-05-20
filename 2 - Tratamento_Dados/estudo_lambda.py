import pandas as pd


# Função para calcular o cubo de um número
def eleva_cubo(x):
    return x ** 3


# Expressão de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3    # Jeito "errado" de utilizar lambda

print(eleva_cubo(5))
print(eleva_cubo_lambda(5))

df = pd.DataFrame({'Números': [1, 2, 3, 4, 5, 10]})

df['Cubo_função'] = df['Números'].apply(eleva_cubo)
df['Cubo_lambda'] = df['Números'].apply(lambda x: x ** 3)  # Lambda deve ser utilizado para cálculos pequenos

print(df)
