"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 8 (b)
"""
class GPA:
    def __init__(self):
        self._gpa = 0.0

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, value):
        if value < 0:
            self._gpa = 0
        elif value > 4:
            self._gpa = 4
        else:
            self._gpa = value

    gpa = property(_get_gpa, _set_gpa)

    @property
    def letter(self):
        letter = ''
        if self.gpa < 1:
            letter = 'F'
        elif self.gpa < 2:
            letter = 'D'
        elif self.gpa < 3:
            letter = 'C'
        elif self.gpa < 4:
            letter = 'B'
        else:
            letter = 'A'
        return letter

    @letter.setter
    def letter(self, letter):
        if letter == 'F':
            self.gpa = 0.0
        elif letter == 'D':
            self.gpa = 1.0
        elif letter == 'C':
            self.gpa = 2.0
        elif letter == 'B':
            self.gpa = 3.0
        elif letter == 'A':
            self.gpa = 4.0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    student.gpa = float(input("Enter a new GPA: "))

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    student.letter = input("Enter a new letter: ")

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()