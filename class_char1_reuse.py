###
### Class vs. Function
### - Class is reusable
###

class Human:
    pass

human1 = Human()
human2 = Human()

human1.first = 'Soo'
human2.first = 'Tae'

print(
    "human1.first:", human1.first, "\n"
    "human2.first:", human2.first
)

def Human():
    pass

fake1 = Human
fake2 = Human

fake1.first = 'Monday'
fake2.first = 'Tuesday'

print(
    "fake1.first:", fake1.first, "\n"
    "fake2.first:", fake2.first
)