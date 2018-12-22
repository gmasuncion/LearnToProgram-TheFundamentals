"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    
    for i in range(len(wordlist)):
        if wordlist[i] == word:
            return True
        else:
            return False
            
        

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    
    word_row = ''
    
    for i in range(len(board[row_index])):
        word_row = word_row + board[row_index][i]
    return word_row
            

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    
    word_column = ''
    
    for item in board:
        word_column = word_column + item[column_index]
    return word_column

        

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """
    
    for i in range(len(board)):
        if word in make_str_from_row(board, i):
            return True
    
    return False
    
def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    
    column_index = 0
    while column_index < len(board[0]):
        if word in make_str_from_column(board, column_index):
            return True
        column_index += 1
    
        return False    

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)  


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    
    score = 0
    
    if len(word) < 3:
        score = 0
    elif len(word) >= 3 and len(word) <= 6:
        score = score + len(word)
    elif len(word) >= 7 and len(word) <= 9:
        score = score + 2 * len(word)
    else:
        score = score + 3 * len(word)
    
    return score
        

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    total_score = word_score(word) + player_info[1]
    no_score = player_info.pop()
    new_score = player_info.append(total_score)
    
    
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    count = 0
    
    for item in words:
        if board_contains_word_in_row(board, item) or board_contains_word_in_column(board, item):
            count += 1
            
    return count


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """

    lists = []
        
    for line in words_file:
        word = ''
        for char in line:
            if char != '\n':
                word = word + char
        lists.append(word)
    
        return lists
    

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    lists = []
             
    for line in board_file:
        sub = []
        for char in line:
            if char != '\n':
                sub.append(char)
        if sub != []:
            lists. append(sub)
            
        return lists    
