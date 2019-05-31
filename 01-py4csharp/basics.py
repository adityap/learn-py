#comment
'''   This
    is multi
'''
import math
def demo_print_greeting():
    print("Test")

def local_variable():
    x = 7
    x="string"
    print(x)

name = "unknown"

def demo_global():
    global name
    name = "Adi"
    print(name +"y")

def demo_math():
    print(7+2)
    print(7-2)
    print(7*2)
    print(7/2)
    print(7%2)
    print(7**2)
    print(7//2)
    print(math.floor(7/2))
    print(math.ceil(7/2))

def demo_fns(fn ="Someone", ln = "Unknown"):
    return fn +" " + ln

def demo_conditions(x):
    if x > 80:
        print("Awesome")
    elif x > 70 and x <= 80:
        print("Good")
    else:
        print("Ok")

def demo_lists():
    friends = ['A', 'Adi','Adit']
    print(friends)
    print(friends[0])
    friends[0] = 'Aditya'
    print(friends[1:3])

    family = ['Mom', 'Dad', 'Cousin']

    people = [friends, family]
    print(people)
    print(people[0][0:2])
    print(str(people))

def demo_loop():
    for i in range(1,5):
        print(i, ' ')

    for i in range(1,5):
        print(i, ' ', end='')

    print()

    friends = ['A', 'Adi','Adit']
    family = ['Mom', 'Dad', 'Cousin']
    people = [friends, family]

    for item in people:
        for i in item:
            print(i)
    
    for i in range(0,len(people)):
        for x in range(0,len(people[i])):
            print('Z ' + people[i][x])

def demo_dict():
    fav_map = {'name': 'Adi', 'role':'lead'}
    print(fav_map)
    print(fav_map['name'])
    del fav_map['name'] #delete value
    print(fav_map)
    fav_map['name'] = 'Adit'
    print(fav_map)
    fav_map['role'] = 'manager'
    print(fav_map)

class employee:
    __name = "" #attribute
    
    #c'tor
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name.upper()

    def set_name(self, value):
        self.__name = value + ' New'

    @property
    def emp_name(self):
        return self.__name.upper()

    @emp_name.setter
    def emp_name(self, value): #same name as getter
        self.__name = value + ' !New'



    def get_intro(self):
        #print('Intro ' + self.__name)
        print("Hello {}" .format(self.get_name()))
        print("Hello {}" .format(self.emp_name)) #call as prop and not method '()'


def demo_class():
    e = employee('Adi')
    e.get_intro()
    e.set_name('Adit')
    e.get_intro()
    e.emp_name = 'Aditya'
    e.get_intro()

def main():
    #demo_print_greeting()
    #local_variable()
    #demo_global()
    #print(name)
    #demo_math()
    #print(demo_fns(ln="Bond"))
    #print(demo_fns)
    #demo_conditions(65)
    #demo_conditions(75)
    #demo_conditions(85)
    #demo_lists()
    #demo_loop()
    #demo_dict()
    demo_class()

if __name__ == "__main__":
    main()


