from lib import *

with open('./file.txt', 'r') as file:
    data = file.read()
    
    reader1: TextReader = TextReader(WordCounter())
    reader1.scan(data)
    print(reader1.result())

    reader2: TextReader = TextReader(WordLineIndexer())
    reader2.scan(data)
    print(reader2.result())
