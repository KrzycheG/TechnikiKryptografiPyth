import hashlib
def cipher_sha256(file_name=r"ubuntu-22.04.2-desktop-amd64 .iso"):
    with open(file_name,"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)
        #return readable_hash
cipher_sha256()