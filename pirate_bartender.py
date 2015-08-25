import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def askCustomer():

    answers = dict()
        
    for flavor in questions:
        input_val = raw_input(questions[flavor]).lower()
        
        if input_val in ["y", "yes"]:
            answers[flavor] = True
        else:
            answers[flavor] = False
    return answers
    
    
def makeDrink(preference):
    
    drink = list()
    
    for flavor in preference:
        if preference[flavor]:
            drink.append(random.choice(ingredients[flavor]))
    return drink
    
def genDrinkName():
    adj = ["Stinky","Happy","Blue"]
    noun = ["Elephant","Suitcase","Granny"]
    
    return random.choice(adj) + " " +random.choice(noun)
    
def main():
    wantDrink = True
        
    while wantDrink:
        getPref = askCustomer()
        drink = makeDrink(getPref)
        
        print "Enjoy your " + genDrinkName()
        
        for item in drink:
            print "Ingredient: {}".format(item)
            
        inputNewDrink = raw_input("Would you like another drink? ").lower()
        if inputNewDrink not in ["y","yes"]:
            wantDrink = False
            print "Goodbye."
        
    
if __name__ == "__main__":
    main()
