def tokenizer(string : str):
    
    return string.split()

def purify(string : str):

    result = string
    remove = []
    for char in string:
        if char != " " and not char.isalpha():
            remove.append(char)
    for char in remove:
        result = result.replace(char, "")
    return result


x = "Hi ! my na^^^me  &* i;s"
print(tokenizer(purify(x)))
