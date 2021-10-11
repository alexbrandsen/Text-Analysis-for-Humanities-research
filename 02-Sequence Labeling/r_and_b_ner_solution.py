# tokenise text
rb_tokens = word_tokenize(rb_text)

# get POS tags
rb_pos = pos_tag(rb_tokens)

# get NER tags
rb_ner = ne_chunk(rb_pos)

# create new list to hold all places
places_found = []

# loop through NER tags and print only places
for chunk in rb_ner:
    if type(chunk)==nltk.tree.Tree and chunk.label()=='GPE':
            place = " ".join([token[0] for token in chunk.leaves()])
            places_found.append(place)

# count places
counted_places = Counter(places_found)

# sort places by count
sorted_counted_places = counted_places.most_common()

# output
sorted_counted_places