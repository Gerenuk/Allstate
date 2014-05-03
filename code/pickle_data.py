import pickle

from constants import train_csv_filename
from environment import *
import pandas as pd


dd0 = pd.DataFrame.from_csv(getfile(r"external\{}".format(train_csv_filename)))
dd0.reset_index(inplace=True)
pickle.dump(dd0, open(getfile(r"data input\dd0.pickle"), "wb"))
