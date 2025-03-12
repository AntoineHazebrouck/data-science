import re

class TextAnalyzer:
	def processLine(self, line: str):
		pass

	def result(self):
		pass

	def reset(self):
		pass

class WordCounter(TextAnalyzer):
	count = 0

	def processLine(self, line) :
		self.count += len(re.findall(r'\b\w+\b', line))
		return self
	
	def result(self):
		return self.count
	
	def reset(self):
		self.count = 0

class WordLineIndexer(TextAnalyzer):
	words = {}
	index = 0

	def processLine(self, line):
		for word in re.findall(r'\b\w+\b', line):
			indexes = self.words.get(word) or []
			indexes.append(self.index)
			self.words[word] = indexes
		self.index += 1
	
	def result(self):
		return self.words
	
	def reset(self):
		words = {}

class TextReader:
	def __init__(self, analyzer: TextAnalyzer):
		self.analyzer = analyzer

	def scan(self, text: str):
		for line in text.splitlines():
			self.analyzer.processLine(line)

	def reset(self):
		self.analyzer.reset()

	def result(self):
		return self.analyzer.result()