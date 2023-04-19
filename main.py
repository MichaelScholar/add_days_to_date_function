"""main script to test functionality"""
from add_days_to_date import add_days_to_date

if __name__ == '__main__':
    print(f'input: Date: 10.01.2008, number_of_days: 10: {add_days_to_date("10.01.2008", 10)}')
    print(f'input: Date: 29.06.2020, number_of_days: 8: {add_days_to_date("29.06.2020", 8)}')
    print(f'input: Date: 28.02.2020, number_of_days: 1: {add_days_to_date("28.02.2020", 1)}')
    print(f'input: Date: 28.02.2021, number_of_days: 1: {add_days_to_date("28.02.2022", 1)}')
