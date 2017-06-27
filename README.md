# NLP Using NLTK
## All the breaking toys related to nlp

### Installations
- import nltk
- nltk.download()
- download *words corpora* & below models
-- maxent_ne_chunker
-- punkt
-- averaged_perceptron_tagg

	
NLTK is smart enough to detect same word as verb or noun based on it's usage in word 

Below code is used
```python

from nltk import word_tokenize, pos_tag, ne_chunk
 
sentence = "You have to answer this question."
chunk =  ne_chunk(pos_tag(word_tokenize(sentence)))
print chunk
chunk.draw()

```

### Test Scenario

|Query 								 | output 													    | remarks     			|
|------------------------------------|--------------------------------------------------------------|-----------------------|
| You have to answer this question.  | (S You/PRP have/VBP to/TO answer/VB this/DT question/NN ./.) | answer is verb here |
| I like your answer. -> answer is noun here | (S I/PRP like/VBP your/PRP$ answer/NN ./.) | answer is noun here |

