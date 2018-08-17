import hashlib


def hash_this(contents):
    string_contents = str(contents)
    encoded_str = string_contents.encode('utf-8')
    hashed = hashlib.sha256(encoded_str)
    hex_hash = hashed.hexdigest()
    return hex_hash