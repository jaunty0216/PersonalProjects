import random

def generate_hex_random(length):
    hex_digits = '0123456789abcdef'
    return ''.join(random.choice(hex_digits) for _ in range(length))

# 生成16個字符長度的十六進制亂數
random_hex = generate_hex_random(16)
print(random_hex)