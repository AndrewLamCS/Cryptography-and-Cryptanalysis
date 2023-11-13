# encryption given in assignment - affine cipher
def encrypt(x, key):
    return (key+11*x)%256

# inverse of above affine cipher
def decrypt(x, key):
    return (163*(x-key))%256

# converts string to list of integers
def word_to_list(s):
    x = [] # start with empty list
    for c in s:
        x.append(ord(c)) # append ordinal value
    return x

# convert string representing hex to list of integers
def hex_string_to_list(s):
    y = []
    for i in range(len(s)//2): # there are L/2 integers
        # s[2*i:2*i+2], the colon represents a range
        # This is equivalent to s.substr(2*i,2) in C++
        y.append(int(s[2*i:2*i+2],16)) # append hex integer value
    return y

# ECB just applies the encryption
def enc_ecb(x, key):
    y = []
    for i in range(len(x)):
        y.append(encrypt(x[i],key))
    return y

def dec_ecb(y, key):
    x = []
    for i in range(len(y)):
        x.append(decrypt(y[i],key))
    return x

def enc_cfb(x, key, IV):
    IV = 0xAA
    y = [encrypt(IV,key)^x[0]] # initialise with IV
    for i in range(1,len(x)):
        y.append(encrypt(y[i-1],key)^x[i]) # apply feedback
    return y
    
def dec_cfb(y, key, IV):
    IV = 0xAA
    x = [encrypt(IV,key)^y[0]]
    for i in range(1,len(y)):
        x.append(encrypt(y[i-1],key)^y[i])
    return x

def enc_cbc(x, key, IV):
    y = [encrypt(IV^x[0],key)]
    for i in range(1,len(x)):
        y.append(encrypt(y[i-1]^x[i],key))
    return y
    
def dec_cbc(y, key, IV):
    x = [decrypt(y[0],key)^IV]
    for i in range(1,len(y)):
        x.append(decrypt(y[i],key)^y[i-1])
    return x
    
def enc_ofb(x, key, IV):
    s = [encrypt(IV,key)] # initialise s separately
    for i in range(1,len(x)):
        s.append(encrypt(s[i-1],key))
    y = []
    for i in range(len(x)):
        y.append(s[i]^x[i])
    return y

def enc_ctr(x, key, IV):
    IV = IV & 0xF8 # only first 5 bits (11111000)
    s = []
    for i in range(len(x)):
        s.append(encrypt(IV|(i%8),k)) # i%8 because last 3 bits
    y = []
    for i in range(len(x)):
        y.append(x[i]^s[i]) # using as a nonce
    return y

def printashex(word):
    for xi in word:
        # zfill makes each substring 2 long with zeros padding left
        # hex(xi)[2:] is to chop off the 0x, takes character 2 to end
        # end='' removes the line at the end of the print
        print(hex(xi)[2:].zfill(2),end='')
    print()

def printasstr(s):
    for i in range(len(s)):
        # chr(s[i]) converts from ordinal to character
        print(chr(s[i]),end='')
    print()

k = 0x08
IV = 0xAA

word_e_ctr = "jumbo"
printashex(enc_ctr(word_to_list(word_e_ctr),k,IV))
word_e_ecb = "congo"
printashex(enc_ecb(word_to_list(word_e_ecb),k))
word_e_cfb = "longo"
printashex(enc_cfb(word_to_list(word_e_cfb),k,IV))
word_e_cbc = "smokey"
printashex(enc_cbc(word_to_list(word_e_cbc),k,IV))
word_e_ofb = "smocks"
printashex(enc_ofb(word_to_list(word_e_ofb),k,IV))

hex_string_d_ctr = "342E3312041EF0F9"
# OFB and CTR are same forwards and backwards
printasstr(enc_ctr(hex_string_to_list(hex_string_d_ctr),k,IV))
hex_string_d_ecb = "963349A15F04"
printasstr(dec_ecb(hex_string_to_list(hex_string_d_ecb),k))
hex_string_d_cfb = "3520091F"
printasstr(dec_cfb(hex_string_to_list(hex_string_d_cfb),k,IV))
hex_string_d_cbc = "5B02A12F368E"
printasstr(dec_cbc(hex_string_to_list(hex_string_d_cbc),k,IV))
hex_string_d_ofb = "35CF602C45"
# OFB and CTR are same forwards and backwards
printasstr(enc_ofb(hex_string_to_list(hex_string_d_ofb),k,IV))