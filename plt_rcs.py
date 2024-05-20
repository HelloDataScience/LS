import seaborn as sns
import matplotlib.pyplot as plt

plt.rc(group = 'font', family = 'Gowun Batang', size = 10)
plt.rc(group = 'figure', figsize = (6, 4), dpi = 150)
plt.rc(group = 'axes', unicode_minus = False)
plt.rc(group = 'legend', frameon = True, fc = '1', ec = '0')

outlier = {
    'marker': 'o', 
    'markersize': 3, 
    'markerfacecolor': 'pink', 
    'markeredgecolor': 'red', 
    'markeredgewidth': 0.5
}