import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from cobra import test


#1
"""
1. [DEF][MNO]* && [JUNDT] = D
2. [DEF][MNO]* && APA|OPI|OLK = O
3. [DEF][MNO]* && (NA|FE|HE)[CV] = N
4. [^DJNU]P[ABC] && APA|OPI|OLK = P
5. [^DJNU]P[ABC] && (NA|FE|HE)[CV] = A
6. [ICAN]* && [JUNDT] = N
7. [ICAN]* && APA|OPI|OLK = I
8. [ICAN]* && (NA|FE|HE)[CV] = C
"""


#2
df = pd.read_csv("/Users/maria/Desktop/M4135/pythonProject/data_for_task2.csv")
data = df.groupby("genus").mean()
data = data.reset_index()
formatted_df = pd.melt(
    frame = data,
    id_vars = 'genus')

sns.set(rc={'figure.figsize':(9,8)})
g = sns.barplot(x = "variable",
                y = "value",
                hue = "genus",
                data = formatted_df)

g.set_xticklabels(g.get_xticklabels(), rotation=45)

plt.show()


#3
numbers = [1,2,3,4,5,6]
my_iter = map(lambda num: (num % 3) == 0, numbers)

while True:
    try:
        print(next(my_iter))
    except StopIteration as error:
        print("Catch the end of array")
        break

"""Iterators helps to avoid memory issues. It is also very helpful when we are working 
   with array for-loops"""


#4
nums = [22, 43, 264, 1990]

for num in nums:
    print("\t")
    print(requests.get("http://numbersapi.com/" + str(num) + "/math").text)
    print(requests.get("http://numbersapi.com/" + str(num) + "/trivia").text)



#5
model = test.create_test_model("textbook") # Name: e_coli_core

model.metabolites.nadh_c.summary(fva=0.95)
model.genes.b3236.knock_out()
model.optimize()
model.metabolites.nadh_c.summary(fva=0.95)

