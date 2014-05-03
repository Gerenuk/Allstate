from collections import Counter

from environment import *
import numpy as np


user_vars = ["state", "location", "group_size", "homeowner", "car_age", "car_value", "risk_factor", "age_oldest", "age_youngest", "married_couple", "C_previous", "duration_previous"]

ddclean = ddquote[["customer_ID"] + user_vars][:10000]

g = ddclean.groupby(["customer_ID"])
ddclean.set_index(["customer_ID"], inplace=True)

for v in user_vars:
    print(v)
    ddclean["num" + v] = g[v].aggregate(lambda x:Counter(list(x.unique())))

ddclean[ddclean["numlocation"].map(lambda x:len(x) > 1)]
