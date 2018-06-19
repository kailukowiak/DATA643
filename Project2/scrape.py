from APIKEYS import apikey
import omdb
import pandas as pd
import numpy as np
import pickle


omdb.set_default('apikey', apikey)


def niner(x):
    length = len(str(x))
    n_zeros = 7 - length  # the id number appaears to be 9 digits long with tts
    value = 'tt'+str(0)*n_zeros+str(x)
    return value


links = pd.read_csv('Project2/ml-latest-small/links.csv')
movies = pd.read_csv('Project2/ml-latest-small/movies.csv')

links['realId'] = np.vectorize(niner)(links['imdbId'])

links = links.set_index('movieId')

# print(omdb.imdbid(links.loc[0, 'realId']))

# test = []
# test.append(omdb.imdbid(links.loc[0, 'realID']))
# test.append(omdb.imdbid(links.loc[2, 'realID']))


moviesDict = {}
errors = {}
for i in links.index:
    try:
        moviesDict[i] = omdb.imdbid(links.loc[i, 'realId'], timeout=5)
        # Otherwise it takes too long
        print('success on', i)
    except:
        errors[i] = 'Failed to load'
        print('Failed on', i)
    if i % 100 == 0:
        with open('moviePlots.pickle', 'wb') as handle:
            pickle.dump(moviesDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('errors.pickle', 'wb') as handle:
            pickle.dump(errors, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('hello world')


with open('moviePlots.pickle', 'rb') as handle:
    b = pickle.load(handle)
