with open("C:/Users/fctjg/Desktop/New Text Document.txt", 'r') as file:
    paragraph = file.read()


def ch(word):
    if '$' in word:
        word2 = ''
        for o in range(len(word)):
            if word[o] == '$':
                o += 1
                word2 += word[o].upper()
            word2 += word[o]
        return word2
    return word


content0_list = paragraph.split('\n')
content_list = []

for line in content0_list:
    p = line.split(',')
    for i in range(len(p)):
        if p[i] != '':
            content_list.append(p[i])
ori_char = []
p = 0

for i in range(len(content_list)):
    if content_list[i] != 'ZZZ':
        ori_char.append(ch(content_list[i].lower()))
    else:
        p = i
        break
new_char = [ch(content_list[i].lower())for i in range(p + 1, len(content_list))]
new_char2 = [item for item in new_char if item not in ori_char]

with open("C:/Users/fctjg/Desktop/Abstracted Document.txt", 'w') as file2:
    file2.write("The new word list:" + '\n')
    for item in new_char2:
        file2.write(item + '\n')

# cut = "~!@#$%^&*()_{}|:<>?，。/、】【’；·1234567890-=+——：“”《》？`"
# ci = 0
# for a in paragraph:
#     if a not in cut:
#         ci += 1
# print(ci)
