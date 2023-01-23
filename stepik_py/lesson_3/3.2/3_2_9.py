
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


if __name__ == '__main__':
    FS = 'some_text'
    S = 'some'
    test_substring(FS, S)

