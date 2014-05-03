from operator import itemgetter
from pprint import pprint

from scipy import stats

from environment import *
import itertools as itoo
from plot.heatmap import heatmap


ddwork = ddpurch[:10000]
var_names = "ABCDEFG"
var_values = {v:set(ddwork[v]) for v in var_names}
fisher_results = []
for i, j in itoo.product(var_names, repeat=2):
    if i >= j:
        continue
    print(i, j)
    for v1, v2 in itoo.product(var_values[i], var_values[j]):
        crosstab = pd.crosstab(ddwork[i] == v1, ddwork[j] == v2)
        odds, pvalue = stats.fisher_exact(crosstab)
        fisher_results.append(dict(a=i, av=v1, b=j, bv=v2, pvalue=pvalue, crosstab=crosstab.values))

# pprint(fisher_results)
relevant_results = filter(lambda x:x["pvalue"] < 0.05, fisher_results)
ordered_results = ["{a}={av} {b}={bv} p={pvalue:.1%} ({crosstab})".format(**r) for r in sorted(relevant_results, key=itemgetter("pvalue"))]
pprint(ordered_results)

heatmap_data = pd.DataFrame()
for r in fisher_results:
    x = "{a}{av}".format(**r)
    y = "{b}{bv}".format(**r)
    heatmap_data.loc[x, y] = r["pvalue"]
    heatmap_data.loc[y, x] = r["pvalue"]

cutoff = 0.02
heatmap_data[heatmap_data > cutoff] = cutoff
heatmap_data.fillna(cutoff, inplace=True)
heatmap_data = heatmap_data.reindex(index=sorted(heatmap_data.index), columns=sorted(heatmap_data.columns))
heatmap(heatmap_data, cmap="YlOrRd_r")
