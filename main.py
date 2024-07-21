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

query = "Zelda Link Mario"

# ----------------------------------------

### Functions

# Where the program's logic is defined

def set_operation(
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


def translate_query(query: str) -> list:
    tags = query.split()
    IDs = []
    for i in tags:
        IDs.append(IDofTag[i])
    return IDs




def process_query(query: str):
    pass
    #for i in translate_query(query):
    #FilesContainingTag[]






# -------------------------------

### Main function

# Where the program is run

def main():
    IDs = translate_query(query)
    sets = []
    for i in IDs:
        sets.append(FilesContainingTag[i])


    
    output = sets
    output = set_operation(sets[0],sets[1],"intersection")


    print(output)


main()
