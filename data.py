import random
sometext = "0sSXy3GPrAoxXPsvF%jQ[QwATJAH92YE-h3dMNWj5dWYwZegD[96-C0Dnz55X48H2nK9W3yAGY074A1Pp6kJNfzwF8z3=GP9-Edh[OzIoPswZiB5WAX`vZLdNBGZS7g9O2654Zx72YzsZwE80O-pOo1Z7YsuIZ[JElSxP7ZItlg"
strength = 0 # Get the correct number (1-50) :)
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUNWXYZ0123456789 "
extra_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUNWXYZ0123456789`-=[];',./~!@#$%^&*()_+{}|:<>? "
increase_amount = 0 # Get the correct number (1-50) :)
v = {}
k = {}
zz = 0
z = 0
test = 0
t2 = 0
for zzz in range(len(extra_char)):
    if zzz + increase_amount >= len(extra_char):
        if test == 0:
            test += 1
            k[extra_char[zzz]] = extra_char[(len(extra_char) - zzz)]
            zz += 1
        else:
            t2 += 1
            k[extra_char[zzz]] = extra_char[t2 + increase_amount]
            zz += 1
    else:
        k[extra_char[zzz]] = extra_char[zzz - increase_amount]
def decrypt_double(word, char, strength, data):
    text = ""
    end = ""
    length = len(word)
    l = length
    l /= (strength + 1)
    l = int(l)
    for y in range(len(word)):
        end += word[len(word) - y - 1]
    for i in range(l):
        text += end[i * (strength + 1)]
    decrypt_extra(data, text, strength, char)
def decrypt_extra(data, secret_word, power, char):
    secret = ""
    for i in range(len(secret_word)):
        secret += k[secret_word[i]]
    print("Your decrypted password is: " + secret)
decrypt_double(sometext, extra_char, strength, k)