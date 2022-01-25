class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create generator with starting serial number"""
        self.start = start
        self.next_num = start
    
    def generate(self):
        """Returns next sequential number"""
        self.next_num += 1
        return self.next_num - 1

    def reset(self):
        """Set serial number back to starting number"""
        self.next_num = self.start

    