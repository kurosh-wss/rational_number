class RationalNumber:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    @classmethod
    def plus(self, up, down):
        new_up = (self.up * down) + (self.down * up)
        new_down = (self.down * down)
        number = RationalNumber(new_up, new_down)
        return number

    @classmethod
    def minus(self, up, down):
        new_up = (self.up * down) - (self.down * up)
        new_down = (self.down * down)
        number = RationalNumber(new_up, new_down)
        return number

    @classmethod
    def divided_by(self, up, down):
        new_up = self.up * down
        new_down = self.down * up
        number = RationalNumber(new_up, new_down)
        return number

    @classmethod
    def times(self, up, down):
        new_up = self.up * up
        new_down = self.down * down
        number = RationalNumber(new_up, new_down)
        return number

    @classmethod
    def show_number(self):
        if self.up is 0:
            print(0)
        elif self.down is 0:
            raise Exception('Division by zero!')
        else:
            print('{}/{}'.format(self.up, self.down))


number = RationalNumber(2, 3)
number.show_number()
new_number = number.divided_by(0, 2)
new_number.show_number()
