from os import path

current_path = path.abspath(__file__)
began_direction = path.join(path.dirname(path.dirname(current_path)), 'New Text Document.txt')
end_direction = path.join(path.dirname(path.dirname(current_path)), "Abstracted Document.txt")

with open(began_direction, 'r') as file:
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
ci = 0

with open(end_direction, 'w') as file2:
    file2.write("The new word list:" + '\n')
    for item in new_char2:
        ci += 1
        file2.write(item + '\n')
    file2.write(f'Totally of {ci} words.')
# cut = "~!@#$%^&*()_{}|:<>?，。/、】【’；·1234567890-=+——：“”《》？`"
# for a in paragraph:
#     if a not in cut:
# print(ci)
