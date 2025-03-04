# %%
import pandas as pd

df = pd.read_excel('listy/oceny_23-24.xls')

def skala(p):
    if p >= 90:
        return 5.0
    elif p >= 85:
        return 4.5
    elif p >= 80:
        return 4.0
    elif p >= 70:
        return 3.5
    elif p >= 60:
        return 3.0
    else:
        return 2.0

df.Suma = df['Suma'].str.replace(',', '.').astype(float)
df['ocena_koncowa'] = df.Suma.apply(skala)

df.ocena_koncowa.value_counts()

# %%
df.to_csv('listy/oceny_23-24.csv')
# %%
