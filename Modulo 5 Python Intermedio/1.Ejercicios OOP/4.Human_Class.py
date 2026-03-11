class Head:
    def __init__(self, eyes=2):
        self.eyes = eyes
class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		self.right_leg = right_leg
		self.left_leg = left_leg
class Arm:
	def __init__(self, hand):
		self.hand = hand
class Hand:
	def __init__(self, fingers=5):
		self.fingers = fingers
class Leg:
    def __init__(self, feet):
        self.feet = feet
class Feet:
    def __init__(self):
        pass


class Human:
    def __init__(self, name, head, torso, right_arm, left_arm, right_leg, left_leg):
        self.name = name
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
    

right_hand = Hand()
right_arm = Arm(right_hand)

left_hand = Hand()
left_arm = Arm(left_hand)

right_feet = Feet()
right_leg = Leg(right_feet)

left_feet = Feet()
left_leg = Leg(left_feet)

head = Head()
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)


person = Human("John", head, torso, right_arm, left_arm, right_leg, left_leg)