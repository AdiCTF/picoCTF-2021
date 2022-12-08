from Crypto.Util.number import inverse, long_to_bytes


# prime factors of n
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473
# The given e
e = 65537
# The given c - what we want to decrypt
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667

phi = (p - 1) * (q - 1)
d  = inverse(e, phi)
# inverse is logically equivalent to:
# for d in range(phi + 1):
#     if d * e % phi == 1:
#         break

n = p * q
num_integer = pow(c, d, n)
# logically equivalent to:
# num_integer = (c ^ d) % n

print(long_to_bytes(num_integer))