import hashlib


def hash_file(filename, algorithm='sha256'):

    hasher = hashlib.new(algorithm)

    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)


    return hasher.hexdigest()

filename = "ubuntu-22.04.2-desktop-amd64 .iso"

print(hash_file(filename))