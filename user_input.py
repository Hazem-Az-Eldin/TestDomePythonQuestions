class TextInput:

    data = ""
    def add(self, character):
       self.data +=character

    def get_value(self):
        return self.data

  
class NumericInput(TextInput):
    def add(self,character):
        if (character.isdigit()):
            self.data +=character

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())