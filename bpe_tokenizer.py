import tiktoken

encoding = tiktoken.encoding_for_model('gpt2')  
text= ("Hello quick brown fox jumps over the lazy dog.")
tokens = encoding.encode(text)

print(tokens)

decoded_text = encoding.decode(tokens)
print(decoded_text)
