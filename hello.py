

class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passangers=[]
    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passangers)

flight = Flight(3)

people = ["Vitaliy", "Ludmila", "Pavel", "Martin"]
for person in people: 
    success=flight.add_passanger(person)
    if success :
        print(f"Add {person} to flight successfully")
    else:
        print(f"No available seat fo {person}")

input()





