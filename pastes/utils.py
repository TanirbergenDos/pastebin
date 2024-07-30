from random import choice

from django.utils.baseconv import BASE64_ALPHABET


# URL_SAFE_BASE64 = ascii_uppercase + ascii_lowercase + digits + "-_"
def random_url(length=8):
    """Return randomly generated string in Base64"""
    return "".join(choice(BASE64_ALPHABET) for _ in range(length))


def is_less_than_1mb(text):
    """Return True if text is less than 1 MB (1_000_000 bytes)"""
    if len(text.encode('utf-8')) >= 1_000_000:
        return False
    return True


if __name__ == "__main__":
    pass
    # test_string = " \\你 （づ￣3￣）づ╭❤️～好"
    # test_string = "你"
    # print("The original string : " + str(test_string))

    # print("The length of string in bytes :", len(test_string.encode('utf-8')))
    # print("The length of string in bytes :", len(test_string.encode('utf-16')))
