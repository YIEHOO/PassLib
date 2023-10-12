from passlib.hash import pbkdf2_sha512 as sha512

def hash_password(message, salt="AZERTY", rounds=10329, lengh=128):
    
    myhash = sha512.using(salt=bytes(salt, 'utf-8'), rounds=rounds, salt_size=lengh).hash(message)
    
    return myhash

print(sha512.verify("password", hash_password("password")))
print(sha512.verify("pass", hash_password("password")))