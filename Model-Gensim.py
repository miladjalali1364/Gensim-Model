
import pandas as pd
from gensim.models import Word2Vec

data_frame = pd.read_csv("data.csv",index_col=False)
print(data_frame.head(5))

data_frame['Maker_Model'] = data_frame['Make'] + ' ' + data_frame['Model']

# Select features from original dataset to form a new dataframe
data_frame1 = data_frame[['Engine Fuel Type','Transmission Type', 'Driven_Wheels',
                         'Market Category', 'Vehicle Size', 'Vehicle Style','Maker_Model']]

# For each row, combine all the columns into one column
df2 = data_frame1.apply(lambda x: ','.join(x.astype(str)), axis=1)

# Store them in a pandas dataframe
data_frame_clean = pd.DataFrame({'clean' : df2})

# Create the list of list format of the custom corpus for gensim modeling
sent = [row.split(',') for row in data_frame_clean['clean']]

# show the example of list of list format of the custom corpus for gensim modeling
print(sent[:2])

#Genism word2vec Model Training
model = Word2Vec(sent, min_count=1,vector_size=100,workers=3, window =3, sg = 1)
print(model)
print(model.wv['Toyota Camry'])

# Compute Similarities
print(model.wv.similarity('Porsche 718 Cayman', 'Nissan Van'))