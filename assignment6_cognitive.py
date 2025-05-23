# -*- coding: utf-8 -*-
"""Assignment6_Cognitive_Computing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SGWmPxyg51ytKp8XR_NtnYgXGx3Q1Hcj

***Q1***
"""

import numpy as np
import matplotlib.pyplot as plt

M=float(input("Enter the value of M: "))
x=np.linspace(-10,10,200)
y1=M*x**2
y2=M*np.sin(x)

plt.plot(x, y1, 'r-', label=f'y = {M}x²')
plt.plot(x, y2, 'b--', label=f'y = {M}sin(x)')
plt.title(f'Mathematical Functions with M = {M}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

"""***Q2***"""

import pandas as pd
import seaborn as sns
import random

data = {
    'Subjects': ['Math', 'Physics', 'Chemistry', 'Computer Science', 'English']
}

df = pd.DataFrame(data)
df['Scores']=[random.randint(60,100) for i in range(5)]

sns.barplot(x='Subjects', y='Scores', data=df, palette='husl')

for i, score in enumerate(df['Scores']):
    plt.text(i, score, str(score), ha='center', va='bottom')

plt.title('Subject Scores Distribution')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.grid(True, axis='y')
plt.show()

"""***Q3***"""

import numpy as np
import matplotlib.pyplot as plt
roll_number = 102317164
np.random.seed(roll_number)
data = np.random.randn(50)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))


cumsum = np.cumsum(data)
ax1.plot(cumsum, 'b-')
ax1.set_title('Cumulative Sum')
ax1.grid(True)
ax1.set_xlabel('Index')
ax1.set_ylabel('Cumulative Sum')

noise = np.random.normal(0, 0.01, 50)
ax2.scatter(range(50), data + noise, alpha=0.6)
ax2.set_title('Scatter Plot with Noise')
ax2.grid(True)
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')

ax3.remove()
ax4.remove()

plt.show()

"""***Q4***"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')
df['total_profit']

sns.lineplot(data=df, x='month_number', y='total_profit')
plt.title('Total Profit Over Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in products:
    sns.lineplot(data=df, x='month_number', y=product, label=product)
plt.title('Product Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()

df_melted = df.melt(id_vars=['month_number'],
                    value_vars=products,
                    var_name='Product',
                    value_name='Sales')
sns.barplot(data=df_melted, x='Product', y='Sales')
plt.title('Sales Distribution by Product')
plt.ylabel('Total Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()

