# find combinations of partial strings in words

words = ['albums', 'barely', 'befoul', 'convex', 'hereby', 'jigsaw', 'tailor', 'weaver']

pieces = ['al', 'bums', 'bar', 'ely', 'be', 'foul', 'con', 'vex', 'here', 'by', 'jig',
          'saw', 'tail', 'or', 'we', 'aver']

# possible solutions = 16^2 combos - 16 dupes = 240
counter = 0
for i in range(len(pieces)):
    for j in range(len(pieces)):
        if i == j:
            continue
        counter +=1
        word = pieces[i] + pieces[j]
        if word in words:
            print counter, word, ' match'
        else:
            print counter, word, ' !='
