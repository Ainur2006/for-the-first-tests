def capitalize(text: str) -> str:
    if text == '':
        return ''
    first_char = text[0].upper()
    line = text[1:]
    return f"{first_char}{line}"


