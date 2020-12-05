import hashlib

string = input().encode('utf-8')
sha = hashlib.sha1()

sha.update(string)
print(sha.hexdigest())