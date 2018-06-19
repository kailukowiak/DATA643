import pickle
import pandas as pd

with open('moviePlots.pickle', 'rb') as handle:
    raw = pickle.load(handle)

columns = ['plot',
           'director',
           'actors',
           'rated',
           'genre',
           'imdb_rating',
           'title']

index = raw.keys()


df = pd.DataFrame(index=index, columns=columns)


def rawExtractor(df, raw, tag):
    for i in raw.keys():
        x = raw[i][tag]
        df[tag][i] = x
    return df

# df = rawExtractor(df, raw, 'plot')
# df = rawExtractor(df, raw, 'director')

for i in df.columns:
    df = rawExtractor(df, raw, i)
#df['plot']

df['imdb_rating'] = df['imdb_rating'].apply(pd.to_numeric)

print(df.head())

df.to_csv('Project2/movieInfo.csv')
