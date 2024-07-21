



#print(1+1)


#File_object = open(r"File_Name","Access_Mode")
#https://www.geeksforgeeks.org/reading-writing-text-files-python/



# Resources :
# https://stackoverflow.com/questions/2983139/assign-operator-to-variable-in-python
# https://realpython.com/python-sets/#defining-a-set










### Dictionaries

# Prefilled with test data for now, will be dynamically generated from file information in the future.

# Input ID of tag to get set containing all IDs of files containing such tag. 
FilesContainingTag = {
    1: set((0,1,2,3,4)),
    9: set([3,4,5,6,7]),
    3: {6,7,8,9,10},
    5: {0,2,18,4,9},
}

# Input name of tag to get corresponding ID of tag.
IDofTag = {
    "Zelda": 1, 
    "Link": 9,
    "Mario": 3
}


# ------------------------------------



### Query

# Will be pulled from the GUI prompt whenever that is setup.
# For now, prefilled value for testing.

searchbar = "( Zelda ~ Link ) -Mario"



# ----------------------------------------







### Functions

# Where the program's logic is defined


def setOperation(
    set1: set,
    set2: set,
    operator: str
) -> set:
    if operator == "union":
        return set1 | set2
    elif operator == "intersection":
        return set1 & set2
    else:
        return "no valid operators"


def readQuery(query: str):
    searchterms = query.split()
    newlist = []
    i = 0
    indent_level = 0
    for x in searchterms:
        match x:
            case "(":
                indent_level +=1
                indentedSubQuery()
            case ")":
                pass
                #compute that query level
            case _:
                pass



        newlist.append(x)
    return newlist

        
def indentedSubQuery():
    pass



class tag:
    def __init__(self) -> None:
        pass

    

class query:
    def __init__(self,query) -> None:
        self.query = query

    def __str__(self) -> str:
        pass

    def read():
        pass




def getTagID(query: str) -> list:
    tags = query.split()
    IDs = []
    for x in tags:
        IDs.append(IDofTag[x])
    return IDs


def getFileSets(query: str) -> list:
    IDs = getTagID(query)
    sets = []
    for x in IDs:
        sets.append(FilesContainingTag[x])
    return sets


def process_query():
    pass


# -------------------------------

### Main function

# Where the program is run

def main():

    #sets = getFileSets(query)

    #output = setOperation(sets[0],sets[1],"intersection")
    output = readQuery(searchbar)

    query1 = query(searchbar)
    output = query1.query

    print(output)


main()


#### HELLOOOOO
# notes so you don't get lost, everything worked fine.
# You could convert many tag names to their IDs and then get the sets of file IDs, and then do an operation by hardcoding a selection of two of these sets.
# So now you wanted to add the ability to process actual search syntax
# For that, I split the input via spaces for now, and then I do a match case to see if it's a tag, or an operator / parentheses.
# The parenthesis bit and nesting the sub queries that need to be resolved first, is the thing I next need to figure out.
# I think that switching my current code to be class/object oriented will smoothe things out a lot.
# I could …
# WAAAAIIIIIITTTTT
# Can't you just actually do set operations on all of the sets at once with parentheses and all ?
# Although, all things considered, I do like the idea of figuring it out manually still, cuz I'll get more control, and will be able to enforce specific operator orders.
# So, going back to what I was saying
# Switch to class/object oriented.
# Then I can basically do a query.resolve() thingie and it'll either reformat the list to make parenteses as only one list entry, or return clear / continue to the other steps.
# The next steps include going through each of the new list items, and if one of them has yet another paretheses in it, you create a s…
# Ugh that doesn't make sense, I'm leaving this to you, you got this. I gotta go play Splatoon to do more than one thing today.



