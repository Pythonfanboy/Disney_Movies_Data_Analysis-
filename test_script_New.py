"""
Created on Sat Nov 05 04:35:43 2023

@author: Dhruvin Modi
This function creates a helper data to test the sample script created for 
the sample solution to the Python Programming for Data Science project.
"""
from python_function import currency_to_int
import pandas as pd

def test_currency_to_int():

# Sample data and write test for the function
    data = {
        'movie_title': [
            'Snow White and the Seven Dwarfs',
            'Pinocchio',
            'Fantasia',
            'Song of the South',
            'Cinderella'],
        'release_date': ['21-Dec-37', '9-Feb-40', '13-Nov-40', '12-Nov-46', '15-Feb-50'],
        'genre': ['Musical', 'Adventure', 'Musical', 'Adventure', 'Drama'],
        'MPAA_rating': ['G', 'G', 'G', 'G', 'G'],
        'total_gross': ['$184,925,485', '$84,300,000', '$83,320,000', '$65,000,000', '$85,000,000'],
        'inflation_adjusted_gross': ['$5,228,953,251', '$2,188,229,052', '$2,187,090,808', '1,078,510,579',
                                '920,608,730']}

    sample_data = pd.DataFrame(data)
    
    # Test case 1: Check if the input argument is a DataFrame
    df = pd.DataFrame({'total_gross': ['$184,925,485', '$84,300,000']})
    try:
        currency_to_int('sample_data', 'total_gross')
    except TypeError as e:
        assert str(e) == 'The data argument is not of type DataFrame'
    
    # Test case 2: Check if white spaces and "$" signs are removed
    df = pd.DataFrame({'total_gross': ['$184,925,485', '$84,300,000']})
    result = currency_to_int(df, "total_gross")
    expected_result = pd.DataFrame({'total_gross': [184925485, 84300000]})
    assert result.equals(expected_result)

test_currency_to_int()
