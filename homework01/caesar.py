def next_letter(letter):
    
    if ("A" <= letter and letter <= "Z"):
        return chr(ord("A") + (ord(letter) - ord("A") + 3) % 26)
    if ("a" <= letter and letter <= "z"):
        return chr(ord("a") + (ord(letter) - ord("a") + 3) % 26)
    else: 
        return letter

def prev_letter(letter):
    
    if ("A" <= letter and letter <= "Z"):
        return chr(ord("A") + (ord(letter) - ord("A") - 3) % 26)
    if ("a" <= letter and letter <= "z"):
        return chr(ord("a") + (ord(letter) - ord("a") - 3) % 26)
    else: 
        return letter


def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE

    ciphertext = ""

    for i in plaintext:
        ciphertext += next_letter(i)
    
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE

    plaintext = ""

    for i in ciphertext:
        plaintext += prev_letter(i)
    
    return plaintext