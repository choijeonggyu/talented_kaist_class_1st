
def encryption(passwd,shift):
    result = ""
    for i in passwd:
        result += chr(ord(i) + shift)
    return result

def decryption(passwd,shift):
    result = ""
    for i in passwd:
        result += chr(ord(i) - shift)
    return result

n=input("Input : ")
s=int(input("shift number : "))
e=encryption(n,s)
print("암호화 : "+e)
print("복호화 : " + decryption(e,s))
