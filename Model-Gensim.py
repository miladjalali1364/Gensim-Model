
import pandas as pd
from gensim.models import word2vec

data_frame = pd.read_csv("data.csv",index_col=False)
print(data_frame.head(5))

data_frame['Maker_Model'] = data_frame['Make'] + ' ' + data_frame['Model']

# Select features from original dataset to form a new dataframe
data_frame1 = data_frame[['Engine Fuel Type','Transmission Type', 'Driven_Wheels',
                         'Market Category', 'Vehicle Size', 'Vehicle Style','Maker_Model']]

# For each row, combine all the columns into one column
df2 = data_frame1.apply(lambda x: ','.join(x.astype(str)), axis=1)