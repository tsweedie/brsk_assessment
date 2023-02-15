
import json
import random
import re


def generate_data(source, output):
    hash_tab = {}
    with open(source) as f:
        corn = f.readlines()

    for w in corn:
        w = w.strip()
        letter = w[0]
        length = len(w)
        index = letter + str(length)

        if index not in hash_tab.keys():
            hash_tab[index] = [w]
        else:
            hash_tab[index].append(w)

    json.dumps(hash_tab, indent=4)
    with open(output, "w") as outfile:
        json.dump(hash_tab, outfile)


def load_data(source):
    with open(source) as json_file:
        data = json.load(json_file)
    return data


def run(hash_tab, i):
    i_list = i.split()

    new_sentence = ""

    for w in i_list:
        w = re.sub('[^A-Za-z]', '', w)
        letter = w[0]
        length = len(w)
        index = letter + str(length)

        try:
            l = hash_tab[index]
            new_sentence += l[random.randint(0, len(l) - 1)] + " "
        except KeyError:
            new_sentence += w  + " "

    return new_sentence


if __name__ == '__main__':
    # Uncomment to regenerate hash_table JSON
    generate_data('corncob_lowercase.txt', 'hash_table.json')

    hash_t = load_data('hash_table.json')
    print("Enter scrabble sentence or 'asdf' to exit:")

    while True:
        inp = input()
        if inp == "asdf":
            print("Thank you for playing ^_^")
            break

        scrabble = run(hash_t, inp)
        print(scrabble)
