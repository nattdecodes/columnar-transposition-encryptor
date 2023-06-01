def key_code(key):
    nums = []
    zipped = list(zip(key, range(1, len(key)+1)))
    alpha = sorted(zipped, key=lambda x: x[0])
    for iter in zipped: nums.append(alpha.index(iter) + 1)
    return nums

def encrypt(msg, key):
    rows = -(-(len(msg)) // len(key))
    columns = len(key)
    sliced = []
    for i in range(0, len(msg), columns): sliced.append(msg[i:i+columns])
    sliced[-1] = sliced[-1].ljust(columns, "*")
    final = []
    keycode = key_code(key)
    i = 0
    while i < columns:
        for str in sliced: final.append(str[i])
        i +=1
    final = [''.join(final[i:i+rows]) for i in range(0, len(final), rows)]
    final = [x for _, x in sorted(zip(keycode, final))]
    decrypted = "".join(final)
    decrypted = decrypted.replace("*", "")
    print(decrypted)

encrypt("EXAMPLEX", "HARD") # test