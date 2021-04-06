import hashlib

# 인코딩할 문자열
string = "d"

# md5 암호화
md5 = hashlib.new("md5")
md5.update(string.encode())

# sha 암호화 - 1
sha_1 = hashlib.new("sha1")
sha_1.update(string.encode())

# sha 암호화 - 224
sha_224 = hashlib.new("sha224")
sha_224.update(string.encode())

# sha 암호화 - 256
sha_256 = hashlib.new("sha256")
sha_256.update(string.encode())

# sha 암호화 - 384
sha_384 = hashlib.new("sha384")
sha_384.update(string.encode())

# sha 암호화 - 512
sha_512 = hashlib.new("sha512")
sha_512.update(string.encode())

print(md5.hexdigest())
print(sha_1.hexdigest())
print(sha_224.hexdigest())
print(sha_256.hexdigest())
print(sha_384.hexdigest())
print(sha_512.hexdigest())
