from random import choice

from django.utils.baseconv import BASE64_ALPHABET


# URL_SAFE_BASE64 = ascii_uppercase + ascii_lowercase + digits + "-_"
def random_url():
    return "".join(choice(BASE64_ALPHABET) for _ in range(8))
