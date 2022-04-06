import collections
def edit_distance(word1, word2):
    size1, size2, operations = len(word1), len(word2), 0
    ancestor = {}
    queue = collections.deque([word1])
    visited = set()
    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == word2:
                queue.clear()
                break
            size1 = len(word)
            for i in range(size1):
                if size1 > size2:
                    next_word = word[:i] + word[i + 1:]
                elif size1 < size2:
                    next_word = word[:i] + word2[i] + word[i:]
                else:
                    next_word = word[:i] + word2[i] + word[i + 1:]
                if next_word not in visited: 
                    visited.add(next_word)
                    queue.append(next_word)
                    ancestor[next_word] = word           
        operations += 1
        
    path = word = word2
    while word != word1:
        word = ancestor[word]
        path =  word + ' -> ' + path
    print(f'\n\tEdit Distance : {operations}\n\tPath : {path}\n')
    return operations

word1 = input('\n\tEnter 1st word : ')
word2 = input('\tEnter 2nd word : ')
edit_distance(word1, word2)