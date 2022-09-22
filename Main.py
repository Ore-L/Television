from Algorithim import linear_search
from Channels import channels
from ChannelLetters import Channel_Types

#This is for the list of categories 
Channel_Type_String = ""
for letter, Type in Channel_Types.items():
    Channel_Type_String += "{0} - {1}\n".format(letter, Type)

#The first thing seen when program is turned on
def greet():
    print("The TV is on!!!")
    print("These are the channel categories available:\n" + Channel_Type_String)

#This is for choosing the category the user wants
def beginning():
    category_letter = input("Type in the corresponding letter of the category you want: ")
    if category_letter in Channel_Types:
        choice = Channel_Types[category_letter]
        return choice
    else:
        print("Sorry that's not a letter we have a category for. You can try again...")
        return beginning()

#This is where the algorithim is used to pick the channel from the list of channels in that category
def retrieval(key):
    if key in channels:
        if key is not None:
            key_print = key
        options = channels[key]
        options_string = options
        print("These are the channels in the " + str(key_print) + " category:\n" + str(options_string))
        option = input("Type in the channel you want to tune into:")
        decision = linear_search(options, option)
    return decision
        
#This is the function for changing from one channel to another
def change(key):
    if key is not None:
        go_back = input("Will you like to choose a different category? That's fine, type in 'o': ")
        if go_back == "o":
            key = beginning()
        else:
            print("Oops, that isn't 'o'...")
            change(key)
    else:
        key = beginning()
    return key

#This is for showing the categories again
def show_categories():
    see_categories = input("Would you like to see the list of categories again? Enter y/n: ")
    if see_categories == "y":
        print(Channel_Type_String)

#This puts all the vital functions together in order to make the program work
def final(key=None):
    key = change(key)
    decision = retrieval(key)
    if decision is not None:
        print("This channel is " + str(decision))
    else:
        ("This category does not have any TV stations")
    again = input("Would you like to move to another category? Enter y\n: ")
    if again == "y":
        show_categories()
        final(key)

#This is when you end the program or file
def goodbye():
    print("TV off")

#This is the full program
def reccomendation():
    greet()
    final()
    goodbye()

reccomendation()