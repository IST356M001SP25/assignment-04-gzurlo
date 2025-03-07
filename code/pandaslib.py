'''
A Library of useful pandas helper functions
SOLUTION FILE!!!!
'''
import pandas as pd

def get_column_names(df : pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    pass # todo: replace this line and add your code


def get_columns_of_type(df : pd.DataFrame, numpy_type: any) -> list[str]:
    '''
    Return the column names of a pandas dataframe only when 
    the values in the column match the numpy_type
    '''
    pass # todo: replace this line and add your code


def get_unique_values(df : pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values of a column in a pandas dataframe
    '''
    pass # todo: replace this line and add your code

def get_file_extension(file_path : str) -> str:
    '''
    Return the file extension of a file_path for example:
    '/some/file/data.csv' -> 'csv'
    '/home/important_grades.xlsx' -> 'xlsx'
    'countries.json' -> 'json'

    '''
    pass # todo: replace this line and add your code

def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    pass # todo: replace this line and add your code

if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    cols = get_columns_of_type(df, 'object')
    print(f"Object Columns: {cols}")
    cols = get_columns_of_type(df, 'int64')
    print(f"Int64 Columns: {cols}")
    cols = get_columns_of_type(df, 'float64')
    print(f"Float64 Columns: {cols}")
    unique = get_unique_values(df, 'state')
    print(f"Unique States: {unique}")





    # solution pandaslib.py

import pandas as pd
import numpy as np
import os

def get_column_names(df: pd.DataFrame) -> list[str]:
    """
    Get all column names of a pandas DataFrame.
    
    :param df: pandas DataFrame
    :return: List of column names
    """
    return df.columns.tolist()


def get_columns_of_type(df: pd.DataFrame, numpy_type: any) -> list[str]:
    """
    Return the column names of a pandas DataFrame where the values match a specific numpy dtype.

    :param df: pandas DataFrame
    :param numpy_type: numpy data type (e.g., 'int64', 'float64', 'object')
    :return: List of column names matching the given type
    """
    return df.select_dtypes(include=[numpy_type]).columns.tolist()


def get_unique_values(df: pd.DataFrame, column_name: str) -> list:
    """
    Get a list of unique values from a specified column in a pandas DataFrame.

    :param df: pandas DataFrame
    :param column_name: Name of the column
    :return: List of unique values
    """
    if column_name in df.columns:
        return df[column_name].dropna().unique().tolist()
    return []


def get_file_extension(file_path: str) -> str:
    """
    Return the file extension of a given file path.

    :param file_path: Path to the file
    :return: File extension as a string (e.g., 'csv', 'xlsx', 'json')
    """
    return os.path.splitext(file_path)[1][1:]  # Extract extension without the dot


def load_file(file_path: str, ext: str) -> pd.DataFrame:
    """
    Load a file into a pandas DataFrame based on the file extension.

    - CSV files assume the first row is a header.
    - JSON files assume record-oriented data.
    - Excel files are loaded with the first sheet by default.

    :param file_path: Path to the file
    :param ext: File extension ('csv', 'xlsx', 'json')
    :return: Loaded pandas DataFrame
    """
    if ext == 'csv':
        return pd.read_csv(file_path)
    elif ext == 'xlsx':
        return pd.read_excel(file_path)
    elif ext == 'json':
        return pd.read_json(file_path, orient='records')
    else:
        raise ValueError("Unsupported file extension. Only CSV, XLSX, and JSON are supported.")


if __name__ == '__main__':
    # Test DataFrame
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
    })
    
    print(f"Columns: {get_column_names(df)}")
    print(f"Object Columns: {get_columns_of_type(df, 'object')}")
    print(f"Int64 Columns: {get_columns_of_type(df, 'int64')}")
    print(f"Float64 Columns: {get_columns_of_type(df, 'float64')}")
    print(f"Unique States: {get_unique_values(df, 'state')}")

