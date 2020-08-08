input = "G R D H P A T X C G G U P K L N \
E F L O X H J K X U Q H J F D F \
I T E C V Z Q H K L D H F N R E \
H R E B C M J D E U P M F W T D \
F H D T U O O L K G V R H N T J \
G J T G M F E C J L F W Q X C B \
B N D H D B O N U O P L A V R F \
R E V R I S D I S P A T C H E D \
E H W G C B E W G J K L Y T E F \
D G S H K B D H E K L D H T N C \
F R G H H T J F E H M V F S H G \
F Y H R N R O P V T D D H K U F \
X D R T H F D W H K G S T I U H \
D J E Y J M D F L O O T J E K E \
U R D F M D V T Y O H D K L F G \
R H D J Y F H T S Y B D M F F H \
H E W F J H D J D W L J G G T F"

# it's a grid of 17x 16
matrix = [["a" for x in range(0,16)] for y in range(0,17)]
# print(matrix)
for i in range(0,17):
    for j in range(0,16):
        matrix[i][j] = input.split(" ")[16*i + j]

# Create all n-letter horizontal words
def get_n_tuple_horizontal(n, matrix):
    start_index = 0
    n_words = list()
    try:
        # iterate each row
        for j in range(0,17):
            # gather each n-tuple word
            for i in range(0,17-n):
                n_words.append(matrix[j][start_index:start_index+n])
                start_index += 1
            # reset the start index on next row
            start_index = 0
    except:
        pass
    n_words = ["".join(each_word) for each_word in n_words]
    return n_words

# Create all n-letter vertical words
def get_n_tuple_vertical(n, matrix):
    start_index = 0
    n_words = list()
    try:
        # iterate each column
        for col in range(0,16):
            # gather each n-tuple word
            for word in range(0,18-n):
                n_tuple = ""
                for row in range(start_index,start_index+n):
                    n_tuple += matrix[row][col]
                # starting index shift on each word
                start_index += 1
                # add the new word to the list
                n_words.append(n_tuple)
            # reset the start index on next row
            start_index = 0
    except: 
        pass
    return n_words

def find_word(word_input, matrix):
    [print(word) for word in get_n_tuple_horizontal(len(word_input), matrix) if word == word_input]
    [print(word) for word in get_n_tuple_vertical(len(word_input), matrix) if word == word_input]

with open("engmix.txt", "r", errors="ignore") as dictionary:
        words_dictionary = dictionary.readlines()

# remove trailing new line
words_dictionary = [word.strip() for word in words_dictionary]

# brute force the puzzle for all words > 3 in length
[find_word(word.upper(), matrix) for word in words_dictionary if len(word) >=3]