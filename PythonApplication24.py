from collections import deque
class brackets():#Class brackets
    #Making a list of brackets.
    Openiningbrackets = ["(", "{", "["]
    Closingbrackets = [")", "}", "]"]

    def Check(self, expression): # Check function that will check the brackets equivalance
        self.stack = deque() #Alloting memory to stack
        for i in expression: #Loop from 0 to the size of expression
            if i in self.Openiningbrackets: #If there's a opening bracket they will be appended in to the stack
                self.stack.append(i) #appending.
            elif i in self.Closingbrackets: #if there's a closing bracket the bracket will be poped out and it will be matched with the existing bracket
                pos = self.Closingbrackets.index(i)
                if ((len(self.stack) > 0) and (self.Openiningbrackets[pos] == self.stack[len(self.stack) - 1])): #if they are same brackets will be poped out.
                    self.stack.pop()
                else:

                    return "Unbalanced"
                if len(self.stack) == 0:
                    return "Balanced"
                else:
                    return "Unbalanced"


object = brackets() #Making object of class
expression=input("Input any expression: ")
print(object.Check(expression))#Calling check function
