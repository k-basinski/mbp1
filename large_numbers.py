# %%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %%

r = np.array([])

df_list = []
for step in range(1, 1001):
    r = np.append(r, np.random.randint(1, 7))
    red = np.zeros(r.shape)
    red[-1] = 1
    mean = r.mean()
    print(r)
    print(step)
    print()
    df_list.append(pd.DataFrame({
        "step": step, 
        "r": r,
        'red': red,
        'mean': mean
        }))


ddf = pd.concat(df_list)
# %%
# steps to plot
sel = list(range(1,11)) + [15, 20, 30, 40, 60, 100]

df = ddf[ddf.step.isin(sel)]

g = sns.FacetGrid(df, col='step', col_wrap=8, aspect=.4)
g.map_dataframe(sns.swarmplot, y='r', alpha=1, hue='red', palette={0:'black', 1:'blue'}, size=4)
g.map_dataframe(sns.pointplot, y='r', errorbar='sd', color='red')
g.refline(y=3.5)
plt.savefig('img/large_numbers_1.png', dpi=300)
# %%
# steps to plot
sel = list(range(100, 1001, 100))

df = ddf[ddf.step.isin(sel)]

g = sns.FacetGrid(df, col='step', col_wrap=6, aspect=.4)
g.map_dataframe(sns.swarmplot, y='r', alpha=1, hue='red', palette={0:'black', 1:'blue'}, size=.5)
g.map_dataframe(sns.pointplot, y='r', errorbar='sd', color='red')
g.refline(y=3.5)
plt.savefig('img/large_numbers_2.png', dpi=300)
# %%
# %%
r = np.array([])

df_list = []
for step in range(1, 1001):
    r = np.append(r, np.random.rand() + 36.1)
    red = np.zeros(r.shape)
    red[-1] = 1
    mean = r.mean()
    print(r)
    print(step)
    print()
    df_list.append(pd.DataFrame({
        "pomiar": step, 
        "temp": r,
        'red': red,
        'mean': mean
        }))


ddf = pd.concat(df_list)
# steps to plot
sel = list(range(1,11)) + [15, 20, 30, 40, 60, 100]

df = ddf[ddf.pomiar.isin(sel)]

g = sns.FacetGrid(df, col='pomiar', col_wrap=8, aspect=.4)
g.map_dataframe(sns.stripplot, y='temp', alpha=1, hue='red', palette={0:'black', 1:'blue'}, size=3)
g.map_dataframe(sns.pointplot, y='temp', errorbar='sd', color='red')
# g.refline(y=3.5)
plt.savefig('img/large_numbers_3.png', dpi=300)
# %%
