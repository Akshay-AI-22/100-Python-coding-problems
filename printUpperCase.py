"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

class Sample:

    def getString(self):
        self.inputVal = input("Enter a String: ")

    def printString(self):
        self.outputVal = self.inputVal.upper()
        print(self.outputVal)

obj = Sample()
obj.getString()
obj.printString()