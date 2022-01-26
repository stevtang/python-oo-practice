class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("test_words.txt")
    3 words read
    >>> wf.words
    ['cat', 'dog', 'porcupine']
    """

    def __init__(self, filepath):
        """Create Word Finder by reading in words from filepath"""
        self.words = WordFinder.readFile(filepath)
        print(f"{len(self.words)} words read")

    @staticmethod
    def readFile(filepath):
        """Reads a file and returns list of the file lines"""
        words = []
        file = open(filepath, "r")
        for line in file:
            words.append(line.strip())
        file.close()
        return words
