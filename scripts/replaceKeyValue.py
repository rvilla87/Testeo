import sys, re

# passing a key to fing this function returns his value reading from a keystore (has the key-value)
def get_value(key_to_find, keystore):
    f_keystore = open(keystore, "r")
    for line in f_keystore.readlines():
        found = re.search(key_to_find, line)
        if found:
            return line.split(':=')[1].split(';')[0].strip()  # define the separators as you wish

#
def replace_line(line, prefix_keyword, keystore):
    patternWord = r'\b\w+\b'  # this pattern matches whole words only
    while re.search(prefix_keyword, line):
        end = re.search(prefix_keyword, line).end()
        word_end = re.search(patternWord, line[end:]).end()
        key_to_find = line[end:end + word_end]  # the key we are looking in order to get his value
        value = get_value(key_to_find, keystore)
        line = re.sub(prefix_keyword + key_to_find, value, line)
    return line


if len(sys.argv) != 4:
    print("ERROR: Usage: 'python replaceKeyValue.py origin.file keystore.file prefix_keyword'")
    sys.exit(1)

origin = sys.argv[1]
keystore = sys.argv[2]
prefix_keyword = sys.argv[3]

f_origin = open(origin, "r")
f_keystore = open(keystore, "r")
f_replaced = open(origin + "_replaced", "w")

for lineO in f_origin.readlines():
    f_replaced.write(replace_line(lineO, prefix_keyword, keystore))
