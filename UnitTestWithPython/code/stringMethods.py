class StringMethods():

    def if_upper(self):
        self.a = 'foo'.upper()
        return self.a

    def check_isupper(self):
        self.a = 'FOO'.isupper()
        self.b = 'Foo'.isupper()
        return self.a, self.b

    def check_split(self):
        s = 'hello world'
        self.a = s.split()
        return self.a
