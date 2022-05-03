
def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("7773325550799984466666")
    'real python'
    '''
# steps:
# 1. create a dictionary with the keypad
# 2. create a list to store the string
# 3. loop through the keys and add the corresponding letter to the list
# 4. if the keypad has the number, append the corresponding letter to the list
# 5. return the list

    keypad = {
            '1': '',
            '2': 'a',
            '22': 'b',
            '222': 'c',
            '3': 'd',
            '33': 'e',
            '333': 'f',
            '4': 'g',
            '44': 'h',
            '444': 'i',
            '5': 'j',
            '55': 'k',
            '555': 'l',
            '6': 'm',
            '66': 'n',
            '666': 'o',
            '7': 'p',
            '77': 'q',
            '777': 'r',
            '7777': 's',
            '8': 't',
            '88': 'u',
            '888': 'v',
            '9': 'w',
            '99': 'x',
            '999': 'y',
            '9999': 'z',
            '0': ' ',
            '': ''
    }

    str = ''
    # loop through the string
    result = []
    # if the keypad has the number, append the corresponding letter to the list

    for letter in keys:
        if len(str) > 0 and (str[-1] != letter or (str+letter) not in keypad):
            # if the last letter is not the same as the current letter remove the last letter
            result.append(keypad[str])
            # append the last letter to the result
            str = ''
            # reset the string
        str += letter
        # append the current letter to the string
    result += keypad[str]
    # return the result
    return result





            
    

        
            
            
             