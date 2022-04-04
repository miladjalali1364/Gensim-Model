
import pandas as pd
from gensim.models import word2vec

data_frame = pd.read_csv("data.csv",index_col=False)
print(data_frame.head(5))

data_frame['Maker_Model'] = data_frame['Make'] + ' ' + data_frame['Model']