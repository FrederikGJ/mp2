import streamlit as st
import pandas as pd

def load_data(file_path, label):
    # Load the Excel file, setting the second row (index 1) as the header
    df = pd.read_excel(file_path, header=1)
    # Add a new column for wine type
    df['Type'] = label
    return df

def main():
    st.title('Wine Data Aggregator')

    # Specify the file paths (adjust these paths if your files are in a different directory)
    red_wine_file_path = 'red_wine.xlsx'
    white_wine_file_path = 'white_wine.xlsx'

    # Load and label the data
    red_wine_data = load_data(red_wine_file_path, 'Red')
    white_wine_data = load_data(white_wine_file_path, 'White')

    # Combine the dataframes
    combined_data = pd.concat([red_wine_data, white_wine_data], ignore_index=True)

    # Display the aggregated DataFrame
    st.write("Aggregated Wine Data:")
    st.dataframe(combined_data)

    # Get the shape of the combined DataFrame
    num_rows, num_cols = combined_data.shape
    st.write(f"Number of rows in the dataset: {num_rows}")
    st.write(f"Number of columns in the dataset: {num_cols}")

    # Display the descriptive statistics
    st.write("Descriptive Statistics:")
    st.dataframe(combined_data.describe())

if __name__ == "__main__":
    main()
