def write_chunks_of_five(words,fname):
    '''
    The function creates a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line.
    Here are the first 10 lines of ouptut corresponding to the above sample corpus:

    the of and to a
    in for is on that
    by this with i you
    it not or be are
    from at as your all
    have new more an was
    we will home can us
    about if page my has
    search free but our one
    other do no information time

    Args: 
        words(list): List of words to be checked.
        fname(string): A file name to save the CSV content of the output.

    Returns:
        file: The file where the CSV content is saved

    Raises:
        AssertionError: If the input data is not a list of numbers or fname is not a string.

    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"
    assert isinstance(fname, str),"The file name needs to be of type string"

    with open(fname,'w') as file:
        i = 0
        for word in words:
            i += 1
            file.write(f'{word} ')
            if i == 5:
                i = 0
                file.write('\n')

if __name__ == "__main__":
    from urllib.request import urlopen 
    u = 'https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
    response = urlopen(u)
    words = [i.strip().decode('utf8') for i in response.readlines()]
    test_file = 'test_output.csv'

    write_chunks_of_five(words, test_file)
    print(f'Test data written to {test_file}. Check the output for correctness.')
