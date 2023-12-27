# data_manager.py

import pandas as pd

class DataManager:
    def __init__(self):
        self.data = pd.DataFrame(columns=['이름'])

    def save_to_excel(self, filename):
        try:
            self.data.to_excel(filename, index=False, engine='openpyxl')

        except Exception as e:
            print(f'Error saving data to {filename}: {e}')

    def load_from_excel(self, filename):
        try:
            self.data = pd.read_excel(filename, engine='openpyxl')

        except (FileNotFoundError, pd.errors.EmptyDataError) as e:
            self.data = pd.DataFrame(columns=['이름'])

    def add_data(self, name, number):
        try:
            if '이름' not in self.data.columns:
                self.data['이름'] = [name]
                new_data = pd.DataFrame({'이름': [name], number: 0, number+'all':0})
                self.data = pd.concat([self.data, new_data], ignore_index=True)  

            elif name not in self.data['이름'].tolist():
                new_data = pd.DataFrame({'이름': [name], number: 0, number+'all':0})
                self.data = pd.concat([self.data, new_data], ignore_index=True)  

        except ValueError:
            print("Invalid number. Please enter a valid integer.")

    def fix_data_win(self, number):
        self.data[number] = self.data[number] + 1
        self.data[number+ 'all'] = self.data[number+ 'all'] + 1

    def fix_data_lose(self, number):
        self.data[number+ 'all'] = self.data[number+ 'all'] + 1

    def show_data(self, name, number):
        value_1 = self.data.loc[self.data['이름'] == number, name].values[0]
        value_2 = self.data.loc[self.data['이름'] == number, name + 'all'].values[0]

        if not pd.isnull(value_1) and not pd.isnull(value_2):
            value = int((value_1 / value_2) * 100)
            return value
        else:
            return 0

