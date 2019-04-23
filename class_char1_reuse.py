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

def Human():
    pass

fake1 = Human
fake2 = Human

fake1.first = 'Monday'
fake2.first = 'Tuesday'

print(f"human1.first: {human1.first}\n"
      f"human2.first: {human2.first}\n"
      f"fake1.first: {fake1.first}\n"
      f"fake2.first: {fake2.first}")

# results >>>
# human1.first: Soo
# human2.first: Tae
# fake1.first: Tuesday
# fake2.first: Tuesday