import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# a = {
#     'name':['abs' , ' xyx'],
#     'marks':[87,95]

# }

df = pd.read_csv('data.csv')
st.title("Data Analysis")
# st.dataframe(df, height=300,width=800)
# st.write(df)
# st.json(a)
col1,col2,col3 = st.columns(3)
col1.metric("Year",'$3652','$3501')
col2.metric("India", '$4201')



df1 = df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'],axis='columns')
# st.write(df1)
# st.map(df1)



# if st.button('load Dataset'):
if st.sidebar.button('load Dataset'):
  st.write(df)

# if st.button('load  description'):
if st.sidebar.button('load  description'):
 st.write(df.describe())

# if st.button('Load Line Chart'):
if st.sidebar.button('Load Line Chart'):
    a = df.head(15)
    a1 = pd.DataFrame(a[['Year', 'TotalPrice']])
    st.line_chart(a1)

# if st.button('Load Bar Chart'):
if st.sidebar.button('Load Bar Chart'):
    b = df.head(20)
    fig = plt.figure(figsize=(10, 8))
    plt.bar(b['Product'], b['Qty'])
    st.pyplot(fig)

if st.sidebar.button(' Load Box Plot'):
    c = df.head(15)
    st.write("Box Plot")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Product', y='Qty', data=c)
    st.pyplot(fig)


if st.sidebar.button('  Load Scatter Plot'):
    st.write("Scatter Plot")
    c = df.head(10)
    fig, ax = plt.subplots(figsize=(10, 8))
    x = c['Year'].head(15)
    y = c['Qty'].head(15)
    plt.scatter(x, y)
    plt.xlabel('Year')
    plt.ylabel('Quantity')
    st.pyplot(fig)

   
if st.sidebar.button('  Load Pie Chart'):
    p = df.groupby('Product').sum()
    fig = plt.figure(figsize=(8, 8))
    plt.pie(p['Qty'], labels=p.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    st.pyplot(fig)
