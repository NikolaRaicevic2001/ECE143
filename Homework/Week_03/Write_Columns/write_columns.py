def write_columns(data, fname):
    '''
    The function that creates three columns to a comma-seperated file according to this formula:
    data_value, data_value**2, (data_value+data_value**2)/3.

    Args: 
        data(list): A list of integers or floats numbers.
        fname(string): A file name to save the CSV content of the output of the function formula.

    Returns:
        file: The file where the CSV content is saved

    Raises:
        AssertionError: If the input data is not a list of numbers or fname is not a string.
    '''

    # Input Validation
    assert isinstance(data, list),"The data needs to be of type list."
    assert all(isinstance(x,(int, float)) for x in data),"The values in data list must be integers of floating points."
    assert isinstance(fname, str),"A filename must be of type string."

    # Write Column Function
    with open(fname,'w') as file:
        # Write header
        # file.write('data_value,data_value_squared,average_value\n')
        
        for value in data:
            squared_value = value**2
            average_value = (value+value**2)/3
            # Format floating-point values to two decimal places
            file.write(f'{value:.2f},{squared_value:.2f},{average_value:.2f}\n')

# Example usage:
# To write the sample data to 'output.csv', you can run:
# write_columns([5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2], 'output.csv')

if __name__ == "__main__":
    # Sample data
    sample_data = [5, 4, 6, 1, 9, 0, 3, 9, 2, 7, 10, 8, 4, 7, 1, 2, 7, 6, 5, 2, 8, 2, 0, 1, 1, 1, 2, 10, 6, 2]
    test_file = 'test_output.csv'

    write_columns(sample_data, test_file)
    print(f'Test data written to {test_file}. Check the output for correctness.')
