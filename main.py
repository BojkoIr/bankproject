import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
data_path = 'Customer-Churn-Records.csv'
data = pd.read_csv(data_path)

# Создание интерфейса
st.title('Анализ оттока клиентов банка')

# Фильтры
geography = st.sidebar.multiselect('Выберите регион:', options=data['Geography'].unique(), default=data['Geography'].unique())
gender = st.sidebar.radio('Выберите пол:', options=['All', 'Male', 'Female'], index=0)
age = st.sidebar.slider('Выберите диапазон возраста:', min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))

# Фильтрация данных
filtered_data = data[(data['Geography'].isin(geography)) & (data['Age'].between(age[0], age[1]))]
if gender != 'All':
    filtered_data = filtered_data[filtered_data['Gender'] == gender]

# Выбор категории данных и типа графика
category = st.sidebar.selectbox('Выберите категорию для анализа:', options=['Balance', 'EstimatedSalary', 'CreditScore', 'NumOfProducts', 'Point Earned'])
chart_type = st.sidebar.selectbox('Выберите тип графика:', options=['Histogram', 'Boxplot'])

# Построение графика
if chart_type == 'Histogram':
    fig, ax = plt.subplots()
    sns.histplot(filtered_data[category], kde=True, ax=ax)
    st.pyplot(fig)
elif chart_type == 'Boxplot':
    fig, ax = plt.subplots()
    sns.boxplot(x=filtered_data[category], ax=ax)
    st.pyplot(fig)

# Показываем данные
st.write(filtered_data)
