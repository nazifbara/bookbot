def get_chars_dict(text: str):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower();
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars
    
def get_num_words(text: str):
    words = text.split()
    return len(words)