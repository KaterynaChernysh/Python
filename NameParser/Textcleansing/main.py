import collecting_data
import pandas as pd

user_dict = []


if __name__ == '__main__':
    ws = pd.read_excel("data/Person_Company(1).xlsx", 'KEY_HOLDER')
    print("Opened")

    user_dict = collecting_data.parse_name_surname(ws)