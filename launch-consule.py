print("Welome to the launch consule")
name = input('What is your name?')
print(f"Hello, {name}!")
menu = ["1: About me","2: my goals","3: Fun fact","4: Exit"]
def About_me(name):
    return f"My name is {name}"
def my_goals(goals):
    return f"my goals are {goals}"
def Fun_fact(fact):
    return f"A fun fact about me is {fact}"
print(menu)
choice = input("Pick one of the 4 menu options: ")
if int(choice) == 1:
    print(About_me(name))
elif int(choice) == 2:
    goals = "I want to go to A&M"
    print(my_goals(goals))
elif int(choice) == 3:
    fact = "I do not like bell peppers"
    print(Fun_fact(fact))
else:
    print("Goodbye!")
    exit()