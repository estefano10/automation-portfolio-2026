def is_isogram(phrase):
    
    characters = [c for c in phrase.lower() if c.isalpha()]
    return len(set(characters)) == len(characters)
