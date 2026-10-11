def write_utf8(path, text):
    # Explicit UTF-8 and LF on Python 3.9+, including Windows.
    with path.open('w', encoding='utf-8', newline='\n') as stream:
        return stream.write(text)
