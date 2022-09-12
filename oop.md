# Object-Oriented Programming / OOP

in python, everything is an object

what's an object ?
a way of encapsulating state and behavior
state : fields, attributes
behavior : what you do with that state (methods)

the object is responsible for modifying its own internal states
    python = self

objects interact with each others



OOP is really good at modeling real-life

OOP is easy to test
u can test an object and its relations with other objects

Definition :
Une classe définit des objets qui sont des instances (des représentants)
de cette classe. Dans ce chapitre on utilisera les
mots objet ou instance pour désigner la même chose.
Les objets peuvent posséder des attributs (variables associées aux objets)
et des méthodes (qui sont des fonctions associées aux objets
et qui peuvent agir sur ces derniers ou encore les utiliser).

Abstraction is hiding complexities of implementation and exposing simpler interfaces.

Encapsulation is hiding the state or internal representation of an object from the consumer of an API and providing publicly accessible methods bound to the object for read-write access. This allows for hiding specific information and controlling access to internal implementation.

Inheritance is the mechanism that allows one class to acquire all the properties from another class by inheriting the class. We call the inheriting class a child class and the inherited class as the superclass or parent class.

Polymorphism is the ability of an OOP language to process data differently depending on their types of inputs.

Heritage
Polymorphisme
Multi Heritage

class OK(FatherCls, PolyCls):
    version = '0.1' #class variable

    def __init__(self, a):
        self.a = a
        self.__field = "idk" # le __ permet en realite detre remplace par `_Classe__field`

    def do(self):
        # do something
        # call the parent do
        super().do()
        PolyCls.do()

    @property
    def radius(self):
        return self.diameter / 2.0

    @field.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    @classmethod
    def from_specialcase(cls, arg):
        a = arg + 20
        return cls(a)

    @staticmethod
    def do_smth(v):
        return v + 1

o = OK(a=3)