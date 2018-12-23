import random

def identity(content):
    return content

def random_insert(content, ratio=0.05):
    new_content = []
    for c in content:
        if random.random() < ratio:
            new_content.append(chr(ord('a') + random.randrange(0, 26)))
        new_content.append(c)
    return ''.join(new_content)

def random_change(content, ratio=0.05):
    new_content = []
    for c in content:
        if random.random() < ratio:
            new_content.append(chr(ord('a') + random.randrange(0, 26)))
        else:
            new_content.append(c)
    return ''.join(new_content)

def random_line_swap(content, ratio=0.2):
    new_content = content.split('\n')
    for i in range(len(new_content) - 1):
        if random.random() < ratio:
            new_content[i], new_content[i + 1] = new_content[i + 1], new_content[i]
    return '\n'.join(new_content)

def random_word_append(content, ratio=0.05):
    new_content = []
    for c in content:
        if c == ' ' and random.random() < ratio:
            for i in range(random.randrange(3, 10)):
                new_content.append(chr(ord('a') + random.randrange(0, 26)))
        new_content.append(c)
    return ''.join(new_content)

def random_word_insert(content, ratio=0.05):
    new_content = []
    for c in content:
        new_content.append(c)
        if c == ' ' and random.random() < ratio:
            for i in range(random.randrange(3, 10)):
                new_content.append(chr(ord('a') + random.randrange(0, 26)))
    return ''.join(new_content)

def random_word_change(content, ratio=0.05):
    new_content = []
    give_up = False
    for c in content:
        if give_up and c == ' ' or c == '\n':
            give_up = False
        if give_up:
            continue
        new_content.append(c)
        if c == ' ' and random.random() < ratio:
            for i in range(random.randrange(5, 10)):
                new_content.append(chr(ord('a') + random.randrange(0, 26)))
    return ''.join(new_content)

def random_capitilize(content, ratio=0.05):
    new_content = []
    give_up = False
    for c in content:
        if give_up and c == ' ' or c == '\n':
            give_up = False
        if give_up:
            continue
        new_content.append(c)
        if c == ' ' and random.random() < ratio:
            for i in range(random.randrange(5, 10)):
                new_content.append(chr(ord('a') + random.randrange(0, 26)))
    return ''.join(new_content)
