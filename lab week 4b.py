#NAMES
#Sarah Morrison

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.
import pandas as pd
import os
import numpy as np
os.chdir(r'/Users/sarahmorrison/Downloads/GitHub/')
base_path = r'/Users/sarahmorrison/Downloads/GitHub/'
og_data_path = os.path.join(base_path, 'week-4-lab/iris.csv')
iris = pd.read_csv(og_data_path)


#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.
iris.columns
iris['species'].unique()
#there are 3 types of flowers

iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].median()
iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].std()
iris[['setosa'],['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

setosa = iris[iris['species'] == 'setosa']
setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

versicolor = iris[iris['species'] == 'versicolor']
versicolor[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

virginica = iris[iris['species'] == 'virginica']
virginica[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.
iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].max()

iris[iris['sepal_length']==7.9]
iris[iris['sepal_width']==4.4]
iris[iris['petal_length']==6.9]
iris[iris['petal_width']==2.5]

iris.iloc[[131, 15, 118, 100, 109, 144]]
#3. How many of observations for each species of iris is in the data?
#50

#4. Using one line of code for each column, divide each value by the mean 
#   for that measure, and assign the result to four new columns.  How is this 
#   different from a zscore?  How would you make this a zscore instead?  What's 
#   the problem with doing this without accounting for the values in the 
#   species column?
def my_func(x):
    equation = x / x.mean()
    return equation

iris['petal_width_new'] = iris['petal_width'] / 1.199333
iris.head()
#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.
iris['petal_area'] = iris['petal_length']* iris['petal_width']

#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

