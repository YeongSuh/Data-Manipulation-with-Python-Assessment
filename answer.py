# 1)
# Consider the Pandas DataFrame df below:

#     gh owner language      repo  stars
# 0  pandas-dev   python    pandas  17800
# 1   tidyverse        R     dplyr   2800
# 2   tidyverse        R   ggplot2   3500
# 3      has2k1   python  plotnine   1450

# Expected Output
# 0    17.80
# 1     2.80
# 2     3.50
# 3     1.45
# Name: stars, dtype: float64

#Complete the code to return the output
import pandas as pd

print(df.stars.map(lambda x: x / 1000))


# 2)
# Subset the Pandas DataFrame df to return all rows with a weight greater than 175.

     species   name  weight
0       lion  Sally     121
1      tiger  Henry     228
2       lion   Tony     177
3      tiger   Lucy     165

Expected Output
  species   name  weight
1   tiger  Henry     228
2    lion   Tony     177

# Complete the code to return the output
print(df[df['weight'] > 175])
# print(df[[('tiger','Henry'),('lion','Tony')]]) ??

# 3)
# Visualize changes in the variable order over time (day) stored in the Pandas DataFrame df.

>>df
    day  order
0     0     10
1     1     11
2     2     14
3     3      7
4     4      5
5     5     16

# Complete the code to return the output
import matplotlib.pyplot as plt
import seaborn as sns

# sns.lineplot(x='day', y='order')  --> Wrong!! 
sns.lineplot(x = 'day', y = 'order', data=df)

plt.xticks(rotation = 45)
plt.show()

# 4)
# Consider the Pandas DataFrame df below.

     gh owner language      repo  stars
0  pandas-dev   python    pandas  17800
1   tidyverse        R     dplyr   2800
2   tidyverse        R   ggplot2   3500
3      has2k1   python  plotnine   1450

Expected Output
     gh owner
0  pandas-dev
1   tidyverse
2   tidyverse
3      has2k1

# Complete the code to return the output
print(df.loc[:,["gh owner"]])

# 5) 
# The chess DataFrame contains information about the top female chess players around the world. A preview of the DataFrame is shown. Set the index of the DataFrame to be the column containing the Fide id of the players.

    Fide id Name.               Federation Year_of_birth     Title
0   700070  Polgar, Judit              HUN          1976        GM
1   8602980 Hou, Yifan                 CHN          1994        GM
2   5008123 Koneru, Humpy              IND          1987        GM
3   4147103 Goryachkina, Aleksandra    RUS          1998        GM
4   700088  Polgar, Susan              HUN          1969        GM

Expected Output
                            Name Federation  Year_of_birth Title
Fide id                                                         
700070             Polgar, Judit        HUN           1976    GM
8602980               Hou, Yifan        CHN           1994    GM
5008123            Koneru, Humpy        IND           1987    GM
4147103  Goryachkina, Aleksandra        RUS           1998    GM
700088             Polgar, Susan        HUN           1969    GM

#Complete the code to return the output
chess = chess.set_index('Fide id')

print(chess.head())

# 6)
# Below is a sample of closing prices for Amazon stock during February of 2013, contained in the DataFrame amazon. Within the DataFrame are two columns: date, which gives the day in date format, and the corresponding close price for each day. Create a line plot of this data.

      date      close
2013-02-08    261.950
2013-02-11    257.210
2013-02-12    258.700
2013-02-13    269.470
2013-02-14    269.240

# Complete the code to return the output
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(
  x='date', 
  y='close', 
  data=amazon)

plt.xticks(rotation = 45)
plt.show()

# 7)
Add the height column to the df DataFrame shown below.

     species    name  weight 
0       lion   Sally     121
1      tiger   Henry     228
2       lion    Tony     177
3      tiger    Lucy     165

Expected Output
  species   name  weight  height
0    lion  Sally     121      70
1   tiger  Henry     228     100
2    lion   Tony     177      80
3   tiger   Lucy     165      85

# Complete the code to return the output
height = [70, 100, 80, 85]

df['height'] = height 

print(df.head())

# 8)
You have collected data on the age for each of 100 shoppers in your store. Calculate the standard deviation for the age of the shoppers.

Expected Output
14.77

# Complete the code to return the output
import numpy as np

sd_age = np.std(age)

print(sd_age.round(2))

# 9)
Subset the DataFrame df to select the alignment and character columns.

  alignment     character height    location
0      Good        Batman   1.88      Gotham
1      Good  Wonder Woman   1.78  Themyscira
2      Evil    Lex Luthor   1.88  Metropolis
3      Evil     The Joker   1.85      Gotham

Expected Output
  alignment     character
0      Good        Batman
1      Good  Wonder Woman
2      Evil    Lex Luthor
3      Evil     The Joker

# Complete the code to return the output
import pandas as pd

# print(df[[:,['alignment', 'character']]) --> Wrong !!
print(df[['alignment', 'character']])

# 10)
The food DataFrame contains nutritional information about six menu items from a restaurant. Print the row index of the data.

Expected Output
Index(['waffles', 'tacos', 'lasagne', 'croissant', 'chicken salad', 'thai curry'], dtype='object', name='item')


# Complete the code to return the output
print(food.index)

# 11) 
You have collected data on the age for each of 100 shoppers in your store. Calculate the mean age and the standard deviation for the shoppers. The age is stored as a numpy array.

Expected Output
40.1
14.77

#Complete the code to return the output
import numpy as np

average_age = np.mean(age)
spread_age = np.std(age)

print(average_age)
print(spread_age.round(2))

# 12) 
As part of a salary review, HR has requested that you gather all information for employees who earn a salary_usd of 5000.

Print the corresponding records from the employee pandas DataFrame shown below.

     first_name    gender    salary_usd  
0         Linda    female          3000  
1         Steve      male          5000 
2         Henry      male         12000
3          Sara    female          5000  

Expected Output
  first_name  gender  salary_usd
1      Steve    male        5000
3       Sara  female        5000

# Complete the code to return the output
print(employee[employee['salary_usd'] == 5000])

# 13)
Return the food DataFrame, previewed below, sorted by the index value item in descending order.

               energy  protein  carbohydrate
item                                        
waffles           200     4.29         35.71
tacos             180    10.94         23.44
lasagne           188    11.76         10.59
croissant         343     5.71         58.57
chicken salad     110     5.00          8.00
thai curry        106     3.18         11.66

Expected Output
               energy  protein  carbohydrate
item                                        
waffles           200     4.29         35.71
thai curry        106     3.18         11.66
tacos             180    10.94         23.44
lasagne           188    11.76         10.59
croissant         343     5.71         58.57
chicken salad     110     5.00          8.00

# Complete the code to return the output
print(food.sort_index(level = 'item', ascending=False))

# 14)
Calculate the inter-quartile range of the age of 100 customers who have recently bought products from your website. age is a numpy array.

Expected Output
27.0

# Complete the code to return the output
from scipy import stats

iqr_age = stats.iqr(age)

print(iqr_age)
