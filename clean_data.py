import pandas as pd

def clean_data(file_path):

    # Load the dataset
    df = pd.read_csv(file_path)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

   # convert numeric columns
    df["TotalDebt"] = pd.to_numeric(df["TotalDebt"])
   

    return df