import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64

# Function to plot bar plot for categorical data
def plot_categorical(data, column):
    fig, ax = plt.subplots()
    data[column].value_counts().plot(kind='bar')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Function to plot box plot for numerical data
def plot_numerical(data, column):
    fig, ax = plt.subplots()
    data.boxplot(column=column)
    st.pyplot(fig)

# Function to plot word cloud for text data
def plot_text(data, column):
    wordcloud = WordCloud(width = 800, height = 400, 
                background_color ='white', 
                stopwords = None, 
                min_font_size = 10).generate(' '.join(data[column].astype(str)))
    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis('off')
    st.pyplot(fig)

# Main function to create the Streamlit app
def main():
    st.title('Data Analytics Dashboard')
    st.sidebar.title('Upload your CSV or Excel file')
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('csv'):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('xlsx'):
                data = pd.read_excel(uploaded_file, engine='openpyxl')
            
            st.write('## Dataset')
            st.write(data)

            for column in data.columns:
                st.write(f'### {column}')
                if data[column].dtype == 'object':
                    plot_text(data, column)
                elif data[column].dtype == 'int64' or data[column].dtype == 'float64':
                    plot_numerical(data, column)
                else:
                    plot_categorical(data, column)

        except Exception as e:
            st.write('Error loading file:', e)

if __name__ == "__main__":
    main()
