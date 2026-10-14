A = 'aa01d6e727442a9ea2b445556b14392adf'
B = 'bb020001f7ce12037e8ea8aa76482e291e1bf2'
def xor_bytes(a, b):
    if len(a) != len(b):
        raise ValueError("length mismatch")
    return bytes(x ^ y for x, y in zip(a, b))
a = bytes.fromhex(A)[2:]
b = bytes.fromhex(B)[4:]
p = b"GET /hello HTTP"
s = xor_bytes(a, p)
answer = xor_bytes(b, s)
print(answer.decode())
