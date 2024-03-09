import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
n = int(input('Introdusing numers of new passwords: '))
length = int(input('Introduce length of password: '))
add_digit = input('Introduce digits? (y = yes, n = not) ').strip()
add_lowercase = input('Introduce upperrcase? (y = yes, n = not) ').strip()
add_uppercase = input('Introduce lowercase? (y = yes, n = not) ').strip()
add_punctuation = input('Introducing such simbols as: !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Excluding casefold? (y = yes, n = not)').strip()


if add_digit.lower() == 'д':
    chars += digits
if add_lowercase.lower() == 'д':
    chars += lowercase_letters
if add_uppercase.lower() == 'д':
    chars += uppercase_letters
if add_punctuation.lower() == 'д':
    chars += punctuation
if remove_badsymbols.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    print(generate_password(length, chars))