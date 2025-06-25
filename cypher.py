
def encrypt(text: str, shift: int = 1):
    result = ''

    for ch in text:
        result += chr(ord(ch) + shift)
    return result

def match(encrypted: str, plain: str, shift:int = 1):
    for index, ch in enumerate(encrypted):
        if(ord(ch) == (ord(plain[index]) + shift)):
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    print("Up and running CYPHER")