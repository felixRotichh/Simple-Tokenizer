import re

class SimpleTokenizerV1:
    def __init__(self,vocab):
        self.str_to_int = vocab #store vocabulary as class attribute for access in the encode and decode
        self.int_to_str = {i:s for s,i in vocab.items()}

    #process input text into token ids
    def encode(self,text):
        preprocessed = re.split(r'([.,!?_"()\']|--|\s)',text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip() 
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    #convert token ids back to text
    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])

        #remove spaces before punctuation
        text = re.sub(r'\s+([.,!?"()\'])',r'\1',text)
        return text

vocab = {  
      "The": 1, "quick": 2, "brown": 3, "fox": 4, "jumps": 5,
    "over": 6, "the": 7, "lazy": 8, "dog": 9, ".": 10,
    "<UNK>": 0  # Unknown token
 } 
tokenizer = SimpleTokenizerV1(vocab)
text = """The quick brown fox jumps over the lazy dog."""
ids = tokenizer.encode(text)
print(ids)