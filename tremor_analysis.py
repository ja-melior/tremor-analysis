import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Function to get group responses

def get_group_responses(data):
    group_data = {}
    for index, row in data.iterrows():
        group = row['group']
        response = row['response']
        if group not in group_data:
            group_data[group] = []
        group_data[group].append(response)
    return group_data

# Function to plot group responses

def plot_group_responses(group_data):
    plt.figure(figsize=(10, 6))
    for group, responses in group_data.items():
        sns.histplot(responses, label=group, kde=True)
    plt.legend()
    plt.title('Group Responses')
    plt.xlabel('Response')
    plt.ylabel('Frequency')
    plt.show()

# Function to process Excel sheet

def process_excel_sheet(file_path):
    data = pd.read_excel(file_path)
    return data

# Function to compile multiple Excel sheets

def compile_excel_sheets(file_paths):
    total_data = pd.DataFrame()
    for file_path in file_paths:
        data = process_excel_sheet(file_path)
        total_data = pd.concat([total_data, data], ignore_index=True)
    return total_data

# Streamlit application

st.title('Tremor Data Analysis')

uploaded_files = st.file_uploader('Upload Excel files', accept_multiple_files=True)
if uploaded_files:
    all_data = compile_excel_sheets([file.name for file in uploaded_files])
    group_responses = get_group_responses(all_data)
    plot_group_responses(group_responses)