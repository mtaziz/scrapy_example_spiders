import pandas as pd
import StringIO
filepath = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/pandas/level3_short_column.csv'
import csv
with open (filepath, "r") as csvfile:
    reader = csv.reader(csvfile)
    reader.next() # Skip the header row
    collected = []
    for row in reader:
        collected.append(row)
    with open('level3_output.csv', 'w') as f:
        f.write(",".join(collected))
    print ",".join(collected)
#df = pd.read_csv(filepath)
#s = df['email'].str.split(',')
#saved_column = df.drop_duplicates(subset=['Blogger_Email'])
#import pandas as pd
#import json

#df = pd.read_csv('data', header=None)
#dates, df = df[0], df.iloc[:, 1:]
#df = pd.concat([df, dates.apply(lambda x: pd.Series(json.loads(x)))], axis=1,
#              ignore_index=True)
#print(df)
#df.groupby(['Date', 'Roll'], as_index=False).first() 
#df.drop_duplicates(take_last=True)
# return df.drop_duplicates(take_last=True).values
#df_clean = df.drop_duplicates(cols=['timestamp', 'user_id'])
#pd.read_csv(StringIO(filepath))
#def func(group):
#    return pd.Series(group.email.str.split(',').values[0], name='email')
#
#ser = df.groupby(level=0).apply(func)

#print s
#print len(saved_column)

import pandas as pd
foo = lambda x: pd.Series([i for i in reversed(x.split(','))])
rev = df['City, State, Country'].apply(foo)
print rev

>>> df
          A  B         C         D         E
0  a1,a2,a3  1  c1,c2,c3  d1,d2,d3  e1,e2,e3
1        a4  2        c4        d4        e4
split each column:

>>> for col in ['A', 'C', 'D']:
...     df[col] = df[col].str.split(',')
... 
>>> df
              A  B             C             D         E
0  [a1, a2, a3]  1  [c1, c2, c3]  [d1, d2, d3]  e1,e2,e3
1          [a4]  2          [c4]          [d4]        e4
define the indexers:

>>> i = df['A'].map(len)
>>> j = np.repeat(np.arange(len(df)), i)
>>> k = np.concatenate(list(map(np.arange, i)))
expand the frame:

>>> df = df.iloc[j]
>>> df
              A  B             C             D         E
0  [a1, a2, a3]  1  [c1, c2, c3]  [d1, d2, d3]  e1,e2,e3
0  [a1, a2, a3]  1  [c1, c2, c3]  [d1, d2, d3]  e1,e2,e3
0  [a1, a2, a3]  1  [c1, c2, c3]  [d1, d2, d3]  e1,e2,e3
1          [a4]  2          [c4]          [d4]        e4
take one from each list:

>>> for col in ['A', 'C', 'D']:
...     df[col] = list(map(lambda xs, i: xs[i], df[col], k))

simply you can apply the regex b,? , which means replace any value of b and , found after the b if exists

df['Column2'] = df.Column2.str.replace('b,?' , '')

Out[238]:
Column1 Column2
0   a   a,c
1   y   n,m
2   d   n,n,m
3   d   x

#############
	
You need to split each string in your list:

import  pandas as pd

df = pd.DataFrame([sub.split(",") for sub in l])
print(df)
Output:

   0         1   2               3         4               5         6
0  AN  2__AS000  26  20150826113000  -283.000  20150826120000  -283.000
1  AN   2__A000  26  20150826113000     0.000  20150826120000     0.000
2  AN  2__AE000  26  20150826113000  -269.000  20150826120000  -269.000
3  AN  2__AE000  26  20150826113000  -255.000  20150826120000  -255.000
4  AN   2__AE00  26  20150826113000  -254.000  20150826120000  -254.000
If you know how many lines to skip in your csv you can do it all with read_csv using skiprows=lines_of_metadata:

import  pandas as pd

df = pd.read_csv("in.csv",skiprows=3,header=None)
print(df)
Or if each line of the metadata starts with a certain character you can use comment:

df = pd.read_csv("in.csv",header=None,comment="#")  
If you need to specify more then one character you can combine itertools.takewhile which will drop lines starting with xxx:

import pandas as pd
from itertools import dropwhile
import csv
with open("in.csv") as f:
    f = dropwhile(lambda x: x.startswith("#!!"), f)
    r = csv.reader(f)
    df = pd.DataFrame().from_records(r)
Using your input data adding some lines starting with #!!:

#!! various
#!! metadata
#!! lines
AN,2__AS000,26,20150826113000,-283.000,20150826120000,-283.000
AN,2__A000,26,20150826113000,0.000,20150826120000,0.000
AN,2__AE000,26,20150826113000,-269.000,20150826120000,-269.000
AN,2__AE000,26,20150826113000,-255.000,20150826120000,-255.000
AN,2__AE00,26,20150826113000,-254.000,20150826120000,-254.000
Outputs:

    0         1   2               3         4               5         6
0  AN  2__AS000  26  20150826113000  -283.000  20150826120000  -283.000
1  AN   2__A000  26  20150826113000     0.000  20150826120000     0.000
2  AN  2__AE000  26  20150826113000  -269.000  20150826120000  -269.000
3  AN  2__AE000  26  20150826113000  -255.000  20150826120000  -255.000
4  AN   2__AE00  26  20150826113000  -254.000  20150826120000  -254.000
... 
