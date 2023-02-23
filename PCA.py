import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")
df.columns = [
    'sepal length in cm',
    'sepal width in cm',
    'petal length in cm',
    'petal width in cm',
    'target'     
]
X = df.drop('target', 1)
y = df['target']
print(X)


Calculo de Medias
def mean_vec(X):
mean_vec = np.mean(X, axis = 0)
return mean_vec

#mean_vec = np.mean(X, axis = 0)
M = X - mean_vec
C = M.T.dot(M) / (X.shape[0]-1)
auto_valores, auto_vetores = np.linalg.eig(C)
pares_de_autos = [
     (
        np.abs(auto_valores[i]),
        auto_vetores[:,i]
     ) for i in range(len(auto_valores))             
]
pares_de_autos.sort()
pares_de_autos.reverse()
total = sum(auto_valores)
var_exp = [
    (i / total)*100 for i in sorted(auto_valores, reverse=True)       
]
cum_var_exp = np.cumsum(var_exp)

x = ['PC %s' %i for i in range(1,len(auto_valores)+1)]
df_temp = pd.DataFrame(
    {'auto-valores': auto_valores,
     'cum_var_exp': cum_var_exp,
     'var_exp': var_exp,
     'Componente': x}
)
print(df_temp)
print()
print("Auto-vetores")
for auto_vetor in [p[1] for p in pares_de_autos]:
  print(auto_vetor)
print()
