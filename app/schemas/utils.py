def to_camel(string: str) -> str:
    components = string.split('_')
    words = [word.capitalize() for word in components[1:]]
    return components[0] + ''.join(words)
