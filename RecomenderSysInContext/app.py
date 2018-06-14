import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('/Users/kailukowiak/Scotchly/scotch.csv')
df = df.dropna()
df = df.rename(columns={'Unnamed: 0': "Distillary", 'Unnamed: 1': "Brand"})

df = pd.get_dummies(df, columns=['Unnamed: 74', 'Unnamed: 75'])
names = df.iloc[:, 0:2]
df = df.iloc[:, 2:]
df = df.apply(pd.to_numeric, errors='ignore')

#x = cosine_similarity(df.iloc[0, 2:], df.iloc[1:, 2:])


def wiskyNames(names):
    
    for i in names:
        

def vectorMean(vecDF):
    '''Computes the mean for each colomn of two vectors 
    and returns their names.'''
    averages = vecDF.mean()
    
    pass


pd.DataFrame()
