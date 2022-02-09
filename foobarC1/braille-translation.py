def solution (phrase: str) -> str:
    """
    This method translates an English letters and spaces (only) string of up to 50 letters to minionish binary representation.
    phrase input: a string contains English letters and spaces, up to 50 chars.
    output: a string containing concatenation of six bin digits packs that represent the input phrase. illegal input wil return None
    note: method does not handle or report to Commander Lambda of badly formatted input
    """
    output = []
    for phrase_char in phrase:
        if phrase_char.isupper():
            output.append(braille_to_bin['cap_follows'])  
        output.append(braille_to_bin[phrase_char.lower()])
    return ''.join(output)

#Braille to bool*6 mapping dict
braille_to_bin = {
    ' ' : '000000',
    'a' : '100000',
    'b' : '110000',
    'c' : '100100',
    'd' : '100110',
    'e' : '100010',
    'f' : '110100',
    'g' : '110110',
    'h' : '110010',
    'i' : '010100',
    'j' : '010110',
    'k' : '101000',
    'l' : '111000',
    'm' : '101100',
    'n' : '101110',
    'o' : '101010',
    'p' : '111100',
    'q' : '111110',
    'r' : '111010',
    's' : '011100',
    't' : '011110',
    'u' : '101001',
    'v' : '111001',
    'w' : '010111',
    'x' : '101101',
    'y' : '101111',
    'z' : '101011',
    'cap_follows': '000001'
}
