chamber_words = ['Not', 'for', 'the', 'first', 'time,', 'an', 'argument', 'had', 'broken', 'out', 'over', 'breakfast', 'at', 'number', 'four,', 'Privet', 'Drive.', 'Mr.', 'Vernon',
'Dursley', 'had', 'been', 'woken', 'in', 'the', 'early', 'hours', 'of', 'the', 'morning', 'by', 'a', 'loud,', 'hooting', 'noise', 'from', 'his', 'nephew', 'Harry’s', 'room.', 'Third', 'time', 'this', 'week!”',
'he', 'roared', 'across', 'the', 'table.', '“If', 'you', 'can’t', 'control', 'that', 'owl,', 'it’ll', 'have', 'to', 'go!', 'Harry', 'tried,', 'yet', 'again,', 'to', 'explain.', '“She’s', 'bored,”', 'he', 'said.',
'“She’s', 'used', 'to', 'flying', 'around', 'outside.', 'If', 'I', 'could', 'just', 'let', 'her', 'out', 'at', 'night', '—', '”', '“Do', 'I', 'look', 'stupid?”', 'snarled', 'Uncle', 'Vernon,', 'a',
'bit', 'of', 'fried', 'egg', 'dangling', 'from', 'his', 'bushy', 'mustache.', '“I', 'know', 'what’ll', 'happen', 'if', 'that', 'owl’s', 'let', 'out.”', 'He', 'exchanged', 'dark', 'looks', 'with', 'his', 'wife,',
'Petunia.', 'Harry', 'tried', 'to', 'argue', 'back', 'but', 'his', 'words', 'were', 'drowned', 'by', 'a', 'long,', 'loud', 'belch', 'from', 'the', 'Dursleys’', 'son,', 'Dudley.', '“I', 'want', 'more', 'bacon.”',
'“There’s', 'more', 'in', 'the', 'frying', 'pan,', 'sweetums,”', 'said', 'Aunt', 'Petunia,', 'turning', 'misty', 'eyes', 'on', 'her', 'massive', 'son.', '“We', 'must', 'build', 'you', 'up', 'while', 'we’ve', 'got',
'the', 'chance…', 'I', 'don’t', 'like', 'the', 'sound', 'of', 'that', 'school', 'food…”', '“Nonsense,', 'Petunia,', 'I', 'never', 'went', 'hungry', 'when', 'I', 'was', 'at', 'Smeltings,”', 'said', 'Uncle', 'Vernon',
'heartily.', '“Dudley', 'gets', 'enough,', 'don’t', 'you,', 'son?”', 'Dudley,', 'who', 'was', 'so', 'large', 'his', 'bottom', 'drooped', 'over', 'either', 'side', 'of', 'the', 'kitchen', 'chair,', 'grinned', 'and', 'turned',
'to', 'Harry.', '“Pass', 'the', 'frying', 'pan.”', '“You’ve', 'forgotten', 'the', 'magic', 'word,”', 'said', 'Harry', 'irritably.', 'The', 'effect', 'of', 'this', 'simple', 'sentence', 'on', 'the', 'rest', 'of', 'the',
'family', 'was', 'incredible:', 'Dudley', 'gasped', 'and', 'fell', 'off', 'his', 'chair', 'with', 'a', 'crash', 'that', 'shook', 'the', 'whole', 'kitchen;', 'Mrs.', 'Dursley', 'gave', 'a', 'small', 'scream', 'and',
'clapped', 'her', 'hands', 'to', 'her', 'mouth;', 'Mr.', 'Dursley', 'jumped', 'to', 'his', 'feet,', 'veins', 'throbbing', 'in', 'his', 'temples.', '“I', 'meant', '‘please’!”', 'said', 'Harry', 'quickly.', '“I', 'didn’t',
'mean', '—', '”', '“WHAT', 'HAVE', 'I', 'TOLD', 'YOU,”', 'thundered', 'his', 'uncle,', 'spraying', 'spit', 'over', 'the', 'table,', '“ABOUT', 'SAYING', 'THE', '‘M’', 'WORD', 'IN', 'OUR', 'HOUSE?”']

#first things first is we want to create a function

def harry_word_search(list_of_words):
  count = 0
  for words in list_of_words:
    if words == 'Harry':
      count = count + 1
  print(count)

harry_word_search(chamber_words)


#basic for loop
#for x in range(6):
    #print(x)
