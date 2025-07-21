import pandas as pd 


def extract_data_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        if df.empty:
            print("empyt file")
        else:
         with open("tic.txt", "w") as file:
             file.write(str(df))
             return df
    except Exception as e:
        print(f"An error {e}")
    return None
excepath = "/home/my/Downloads/Python/tie1.xlsx"
data = extract_data_from_excel(excepath)

print(data)
