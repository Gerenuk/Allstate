from environment import *

dd = dd0.copy()
dd.reset_index(inplace=True)
dd.customer_ID = dd.customer_ID.astype(int)
# dd.set_index(["customer_ID"], inplace=True)

dd["quote"] = dd.A.map(str) + dd.B.map(str) + dd.C.map(str) + dd.D.map(str) + dd.E.map(str) + dd.F.map(str) + dd.G.map(str)

ddpurch = dd[dd.record_type == 1]
del ddpurch["record_type"]
del ddpurch["shopping_pt"]

ddshop = dd[dd.record_type == 0]
del ddshop["record_type"]
# ddshop.set_index("shopping_pt", append=True, inplace=True)

ddshop = pd.merge(ddshop, ddpurch[["customer_ID", "quote", "cost"]], left_on=["customer_ID"], right_on=["customer_ID"], suffixes=("", "purch"))
ddshop["chosenquote"] = ddshop.quote == ddshop.quotepurch
ddshop["chosen"] = ddshop.chosenquote & (ddshop.cost == ddshop.costpurch)

g = dd.groupby("customer_ID")

