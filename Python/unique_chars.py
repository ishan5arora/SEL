def is_char_unique(x=None, case_sensitivity=True):
    """
    Checks if the string has unique characters.
    Example:
        is_char_unique(x="abcABC")
        is_char_unique(x=abcABC, case_sensitivity=False)

    :param str x:
        **REQUIRED** Input string.
    :param bool case_sensitivity:
        *OPTIONAL* Pass True if you want to treat "A" and "a" equally and so on.
    :return: Returns True or False
    :rtype: bool
    """
    if x is None:
        raise Exception("String Cannot by NULL")

    bit_array = [0] * 256

    for character in list(x):
        if bit_array[ord(character)] == 1:
            return False
        bit_array[ord(character)] = 1
        if case_sensitivity is False:
            if ord(character) >= 65 and ord(character)<=90:
                bit_array[ord(character)+32] = 1
            elif ord(character) >= 97 and ord(character)<=122:
                bit_array[ord(character)-32] = 1

    return True



#This function is using bitwise opertaions where no exra space is used (except 1 int)
#Assuming input character, range from 'a' to 'z'
def is_char_unique_bitwise(x=None):
    """
    Checks if the string has unique characters.
    Example:
        is_char_unique_bitwise(x="abca")

    :param str x:
        **REQUIRED** Input string.
    :return: Returns True or False
    :rtype: bool
    """
    if x is None:
        raise Exception("String Cannot by NULL")

    flag = 0

    for character in list(x):
        value = ord(character) - ord('a')
        if flag & (1<<value) != 0:
            return False
        flag = flag | (1<<value)

    return True





if __name__ == '__main__':

    #This will return True
    print(is_char_unique(x="abcABC"))

    #This will return False, will treat "a" and "A" equally.
    print(is_char_unique(x="abcABC", case_sensitivity=False))

    #This will return True
    print(is_char_unique_bitwise(x="abcd"))

    #This will return False
    print(is_char_unique_bitwise(x="abca"))
