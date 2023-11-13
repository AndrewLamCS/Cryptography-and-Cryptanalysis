def frequencyAnalysis(ciphertext):
  #Function: Prints/calculates letter counts and relative frequencies of characters in a string argument

  freq_dict = {}  #initialize dictionary to store frequencies of each character
  letter_count = 0  #counts total number of letters in ciphertext

  for char in ciphertext:  #iterate through each character in ciphertext
    if char.isalpha():  #check if each character is alphabetical
      char = char.lower(
      )  #if so, convert each character to lowercase to manage case sensitivity
      if char in freq_dict:  #if character already exists in dictionary, add 1 to count
        freq_dict[char] += 1
      else:
        freq_dict[char] = 1  #if character does not exist, start count at 1
      letter_count += 1  #increment the letter_count for frequency analysis

  freq_dict = dict(sorted(freq_dict.items()))  #sort dictionary

  relative_freq_dict = {}  #initalize dictionary to store relative frequency
  for char, freq in freq_dict.items(
  ):  #iterate through dictionary and for each key, update the frequency value
    relative_freq_dict[char] = freq / letter_count

  relative_freq_dict = dict(
      sorted(relative_freq_dict.items(), key=lambda x: x[1],
             reverse=True))  #sort dictionary by highest VALUE

  print("Letter Counts of Characters in Ciphertext:")
  for k, v in freq_dict.items():  #print letter counts
    print(f"{k} : {v}")

  print("")

  print("Relative Frequencies of Characters in Ciphertext: ")
  for k_rel, v_rel in relative_freq_dict.items():  #print relative frequencies sorted by VALUE 
    print(f"{k_rel} : {v_rel:.4f}")
  
  print("")
  displayEngLetterFreq()

  print(f"\nOriginal Ciphertext:\n {ciphertext}")  #print original ciphertext

  deciphered_text = ""  #initialize new empty string to store deciphered characters

  for char in ciphertext:
    if (char == 'r'):
      deciphered_text += 'e'

    elif (char == 'b'):
      deciphered_text += 't'
  
    elif (char == 'm'):
      deciphered_text += 'a'
  
    elif (char == 'k'):
      deciphered_text += 'n'
  
    elif (char == 'j'):
      deciphered_text += 'o'
  
    elif (char == 'w'):
      deciphered_text += 'i'
  
    elif (char == 'i'):
      deciphered_text += 's'
  
    elif (char == 'p'):
      deciphered_text += 'h'
  
    elif (char == 'u'):
      deciphered_text += 'r'
  
    elif (char == 'd'):
      deciphered_text += 'd'
  
    elif (char == 'h'):
      deciphered_text += 'l'
  
    elif (char == 'v'): 
      deciphered_text += 'c'
    
    elif (char == 'x'): 
      deciphered_text += 'f'
    
    elif (char == 'y'): 
      deciphered_text += 'm'
    
    elif (char == 'n'): 
      deciphered_text += 'u'
    
    elif (char == 's'): 
      deciphered_text += 'p'
    
    elif (char == 't'): 
      deciphered_text += 'y'
    
    elif (char == 'l'): 
      deciphered_text += 'b'
    
    elif (char == 'o'): 
      deciphered_text += 'g'
    
    elif (char == 'q'): 
      deciphered_text += 'k'
    
    elif (char == 'a'): 
      deciphered_text += 'x'
    
    elif (char == 'c'): 
      deciphered_text += 'w'
    
    elif (char == 'e'): 
      deciphered_text += 'v'
    
    elif (char == 'f'): 
      deciphered_text += 'q'
    
    elif (char == 'g'): 
      deciphered_text += 'z'

    else:
      deciphered_text += char

  print(f"\nDeciphered Text:\n{deciphered_text}" )

def displayEngLetterFreq():
  """Displays dictionary contents of Table 1.1 - Relative Letter Frequencies of the English Language"""
  eng_dict = {'A' : 0.0817, 
              'B' : 0.0150, 
              'C' : 0.0278,
              'D' : 0.0425,
              'E' : 0.1270,
              'F' : 0.0223,
              'G' : 0.0202,
              'H' : 0.0609,
              'I' : 0.0697,
              'J' : 0.0015,
              'K' : 0.0077,
              'L' : 0.0403,
              'M' : 0.0241,
              'N' : 0.0675,
              'O' : 0.0751,
              'P' : 0.0193,
              'Q' : 0.0010,
              'R' : 0.0599,
              'S' : 0.0633,
              'T' : 0.0906,
              'U' : 0.0276,
              'V' : 0.0098,
              'W' : 0.0236,
              'X' : 0.0015,
              'Y' : 0.0197,
              'Z' : 0.0007
             }
  print("Table 1.1 - Relative Letter Frequencies of the English Language:")
  eng_dict = dict(sorted(eng_dict.items(), key=lambda x: x[1],reverse=True))  #sort dictionary by highest VALUE
  for k, v in eng_dict.items():
    print(f"{k} : {v}")

cipher_phrase = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""

frequencyAnalysis(cipher_phrase)
print("")
