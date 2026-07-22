def abbreviate(sentence):
    words = sentence.replace("-", " ").replace("_", " ").split()
    initials = [w[0].upper() for w in words]
    
    return "".join(initials)
