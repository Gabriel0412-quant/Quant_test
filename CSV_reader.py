import pandas as pd

gbv = pd.read_csv('Dados\serie aconcagua (2).csv', encoding='utf-8')

zeragem = pd.read_csv('Dados\serie sant (1).csv', encoding='utf-8')

gbv_retorno = gbv[['DATA_REFERENCIA', 'RETORNO_DIA']]

zeragem_retorno = zeragem[['DATA_REFERENCIA', 'RETORNO_DIA']]

gbv_retorno.rename(columns={'RETORNO_DIA' : 'RETORNO_GBV'}, inplace=True)

gbv_retorno

zeragem_retorno.rename(columns={'RETORNO_DIA' : 'RETORNO_zeragem'}, inplace=True)

zeragem_retorno

novo_df = pd.concat([gbv_retorno[['DATA_REFERENCIA', 'RETORNO_GBV']], zeragem_retorno[['DATA_REFERENCIA', 'RETORNO_zeragem']]], axis=1)

novo_df

novo_df.drop(novo_df.columns[2], axis=1, inplace=True)

retirando_NaN = novo_df.fillna(0)


retirando_NaN['RETORNO_PONDERADO'] = retirando_NaN['RETORNO_GBV'] * 0.9715 + retirando_NaN['RETORNO_zeragem'] * 0.0285

final = retirando_NaN*100

final


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(final['RETORNO_PONDERADO'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma do Retorno Ponderado')
plt.xlabel('Retorno Ponderado')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

final



remove_index = None
for i in range(len(final)):
 
    if final['RETORNO_GBV'].iloc[i:].nunique() == 1:
        remove_index = i
        break


if remove_index is not None:
    final = final.iloc[:remove_index]


print(final)


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(final['RETORNO_PONDERADO'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma do Retorno Ponderado')
plt.xlabel('Retorno Ponderado')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

final


