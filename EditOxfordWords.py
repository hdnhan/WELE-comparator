import numpy as np
import pandas as pd

file = open('OxfordWords.txt')
data = file.readlines()

output = []
for i,line in enumerate(data):
    word,t = " ".join(line.split()[:-1]),line.split()[-1][:-2]
    output.append([word,t])

dfoutput = pd.DataFrame(output,columns = ['word','type'])
dfoutput.to_pickle('OxfordWords.pkl')

    