import pickle
import random

from constants import project_path
from filegetter import FileGetter
import pandas as pd


random.seed(1)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 20)

getfile = FileGetter(project_path)
dd0 = pickle.load(open(getfile(r"data input\dd0.pickle"), "rb"))
ddpurch = dd0[dd0.record_type == 1]
ddquote = dd0[dd0.record_type == 0]
