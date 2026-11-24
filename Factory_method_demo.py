class FrenchLocalizer:
    def __init__(self):
        self.translation={"car":"voiture","bike":"bicycle"}

    def localize(self,msg):
        return self.translation.get(msg,msg)


def Factory(language="English"):

    localizers={"French": FrenchLocalizer,"English": EnglishLocalizer}
