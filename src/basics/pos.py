
# coding: utf-8

# In[1]:

from nltk import word_tokenize, pos_tag, ne_chunk
 
sentence = "Mukesh Ambani is CEO of Relaince"
chunk =  ne_chunk(pos_tag(word_tokenize(sentence)))
print chunk
chunk.draw()


# In[ ]:



