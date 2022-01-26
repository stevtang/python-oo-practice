from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("test_words.txt")
    3 words read
    >>> wf.words
    ['cat', 'dog', 'porcupine']
    """

    def __init__(self, filepath):
        """Create Word Finder by reading in words from filepath"""
        self.words = self.readFile(filepath)
        print(f"{len(self.words)} words read")

    
    def readFile(self, filepath):
        """Reads a file and returns list of the file lines"""
        words = []
        file = open(filepath, "r")
        for line in file:
            words.append(line.strip())
        file.close()
        return words

    def random(self):
        """Returns random word"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """"""

    def __init__(self, filepath):
        super().__init__(filepath)

    
    def readFile(self, filepath):
        words = []
        file = open(filepath, "r")
        for line in file:
            if line.startswith("#") or line == "\n":
                continue
            words.append(line.strip())
        file.close()
        return words