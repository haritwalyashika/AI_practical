def KnowledgeBase():
    KB_plants={
           "Yellow spots on leaves": "Possible nutrient deficiency or fungal infection",
            "Brown spots on leaves": "Possible fungal infection",
            "Wilting leaves": "Possible dehydration or root rot",
            "White powdery substance on leaves": "Possible powdery mildew infection",
            "Holes in leaves": "Possible pest infestation"
    }
    return KB_plants

def diagonisis(symtom,KB_plants):
    if symtom in KB_plants:
        Diagonsis= KB_plants[symtom]
    return Diagonsis 


if __name__=="__main__":

    symtoms=input("enter the symptoms seen on ur plant leaves")
    #symtoms=input.split(",")
    print(symtoms)
    KB=KnowledgeBase()
    print(diagonisis(symtoms,KB))