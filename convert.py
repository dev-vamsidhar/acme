import pandas as pd
import os

# Read the Excel file
df = pd.read_excel('fileupdate.xlsx')

# Loop through the rows of the DataFrame and rename the files in the images folder
for index, row in df.iterrows():
    filename = row[4]  # Get the filename from the fifth column
    filepath = os.path.join('images/', filename)  # Get the full filepath
    if os.path.exists(filepath):  # Check if the file exists
        new_filename = row[1] + os.path.splitext(filename)[1]  # Get the new filename from the second column
        new_filepath = os.path.join('images/', new_filename)  # Get the full new filepath
        os.rename(filepath, new_filepath)  # Rename the file

# Print a message to confirm that the filenames have been changed
print("Filenames have been updated!")
