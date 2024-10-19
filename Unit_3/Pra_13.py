#👉 Write a programe to implement multiple inheritance using two base classes

class father:
    def height(self):
        print("Height is 6.0 foot")

class mother:
    def complexion(self):
        print("compexion is fair")

class child(father,mother):
    pass
c = child()

print("child inherited qualitities")
c.height()
c.complexion()

# #output:-
# child inherited qualitities
# Height is 6.0 foot
# compexion is fair
