"""
Created on Sat Nov 05 04:29:00 2023

@author: Dhruvin Modi

"""

def currency_to_int(df, column_name):
    import pandas as pd
    """
    Performs data cleaning operations on the specified column from the given data frame.

    Parameters
    ---------
    df: pandas.core.frame.DataFrame
        The data frame on which the data cleaning needs to be performed.
    col_name: str
        The name of the column on which data cleaning needs to be performed

    Returns
    -------
    pandas.core.frame.DataFrame
        a dataframe with cleaned values for the specified column

    Raises
    ------
    TypeError
        If the input argument df is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument column_name is not in the df columns

    Examples
    --------
    >>> currency_to_int(movies_gross, "total_gross")

    """

    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(df, pd.DataFrame):
     raise TypeError("The data argument is not of type DataFrame")

    # Tests that the the grouping column is in the dataframe
    assert (
        column_name in df.columns
    ), "The specified column does not exist in the dataframe"

    # create a new df that includes all columns except the one that needs to be cleaned.
    df_cleaned = df.loc[:, df.columns != column_name]

    # start cleaning process by removing white spaces and $ sign
    df_cleaned[column_name] = df[column_name].str.strip()
    df_cleaned[column_name] = df[column_name].str.strip("$")

    # Replace all ','s
    df_cleaned[column_name] = df_cleaned[column_name].str.replace(",", "")

    # convert all data to int type
    df_cleaned[column_name] = df_cleaned[column_name].astype(int)

    # return the newly created df with cleaned values for the specified column
    return df_cleaned
