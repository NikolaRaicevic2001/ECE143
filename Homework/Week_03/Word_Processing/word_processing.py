def get_average_word_length(words):
    '''
    The function computes the average length of the words in the words list.

    Args:
        words(list): List of words to be checked.

    Return: 
        average_word_length(float): The average length of the words.

    Raises:
        AssertionError: If the input words is not list of strings.
    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"

    # Compute average lenght of words
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words) if words else 0

    return average_length

def get_longest_word(words):
    '''
    The function computes the longest word in the words list.

    Args:
        words(list): List of words to be checked.

    Return: 
        longest_word(string): The longest word in the sequence.

    Raises:
        AssertionError: If the input words is not list of strings.
    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"

    # Compute longest word in sequence
    longest_word = max(words, key=len) if words else ""

    return longest_word

def get_longest_words_startswith(words,start):
    '''
    The function computes the longest word that starts with specific letter in the words list.

    Args:
        words(list): List of words to be checked.
        start('string'): The letter that the word should start with.

    Return: 
        longest_word_with_start(string): The longest word in the sequence.

    Raises:
        AssertionError: If the input words is not list of strings or the start is not a character.
    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"
    assert isinstance(start, str) and len(start) == 1, "Start should be a single character string."

    # Longest word that starts with letter 'start'
    start = start.lower()
    filtered_words = [word for word in words if word.startswith(start)]
    longest_word_with_start = max(filtered_words, key=len) if filtered_words else ""

    return longest_word_with_start

def get_most_common_start(words):
    '''
    Function that outputs the most common starting letter in the words list.

    Args:
        words(list): List of words to be checked.
    Return: 
        most_common_start(string): The most common starting letter.

    Raises:
        AssertionError: If the input words is not list of strings.
    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"

    from collections import Counter
    starting_letters = [word[0].lower() for word in words]
    most_common = Counter(starting_letters).most_common(1)
    
    most_common_start = most_common[0][0] if most_common else ""

    return most_common_start

def get_most_common_end(words):
    '''
    Function that outputs the most common ending letter in the words list.

    Args:
        words(list): List of words to be checked.

    Return: 
        most_common_end(string): The most common ending letter.

    Raises:
        AssertionError: If the input words is not list of strings.
    '''
    # Input Validation
    assert isinstance(words, list),"The input words need to be of type list"
    assert all(isinstance(word,str) for word in words),"All elements in the list need to be of type string"

    from collections import Counter
    starting_letters = [word[-1].lower() for word in words]
    most_common = Counter(starting_letters).most_common(1)
    
    most_common_end = most_common[0][0] if most_common else ""

    return most_common_end

if __name__ == "__main__":
    from urllib.request import urlopen 
    u = 'https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
    response = urlopen(u)
    words = [i.strip().decode('utf8') for i in response.readlines()]
    
    # Test function get_average_word_length(words)
    print(f"Average word length: {get_average_word_length(words)}")

    # Test function get_longest_word(words)
    print(f"The longest word in the sequence: {get_longest_word(words)}")

    # Test function get_longest_words_startswith(words)
    start = 'a'
    print(f"The longest word in the sequence that starts with letter {start}: {get_longest_words_startswith(words,start)}")

    # Test function get_most_common_start(words)
    print(f"The letter that most commonly appears in the start of the words in word list: {get_most_common_start(words)}")

    # Test function get_most_common_end(words)
    print(f"The letter that most commonly appears in the end of the words in word list: {get_most_common_end(words)}")





