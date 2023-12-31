def ofb(word):
    list_of_letters = list(word)
    xs = [] #list of decimal plaintexts
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    
    #Affine Encryption with OFB mode
    iv = int("0XAA", 16) #in decimal
    key = int("0X08", 16)
    ss = []
    ys = []
    s0 = (key + 11 * iv) % 256
    y0 = hex(xs[0] & s0)
    ss.append(s0)
    ys.append(y0)

    for i in range(1, len(xs)):
        si = (key + 11 * ss[i - 1]) % 256
        ss.append(si)
        yi = hex(xs[i] ^ ss[i])
        ys.append(yi)
    return xs, ys

def main():
    word_ofb = "smocks"
    xs_ofb, ys_ofb = ofb(word_ofb)

    print("\nOFB plaintext", xs_ofb)
    print("OFB Mode ciphertext in hex =", ys_ofb)

main()