import pandas as pd
import webbrowser

def open_urls_from_excel(excel_file):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        urls = df['URL']  # Assuming the column containing URLs is named 'URL'

        # Open each URL in the default web browser
        for url in urls:
            webbrowser.open_new_tab(url)
    except Exception as e:
        print("Error:", e)

# Provide the path to your Excel file
excel_file_path = 'C:\\Users\\shambhu nath giri\\PycharmProjects\\FirstPythonProject\\Files\\urls.xlsx'

# Call the function to open URLs from the Excel file
open_urls_from_excel(excel_file_path)
