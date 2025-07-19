from random import randint
class train:
    def __init__(self, train_no):
        self.train_no = train_no
        
    def train_info(self,from_station, to_station):
        print(f"Train No: {self.train_no}, From: {from_station}, To: {to_station}")
    
    def getstatus(self):
        print(f"Train No: {self.train_no} is running on time.")

    def getfare(self,from_station, to_station):
        print(f"Fare for Train No: {self.train_no} from {from_station} to {to_station} is ${randint(50, 200)}")

t = train(1234)
t.train_info("New York", "Los Angeles")
t.getstatus()
t.getfare("New York", "Los Angeles")