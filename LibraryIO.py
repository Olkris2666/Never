

from stenway.sml import *

# Maybe I should extend the code so that it supports JSON style read and write methods ?

class Library:
    def __init__(self, path: str = "library.txt") -> None:

        self.path = path    # library object stores path argument to reuse across functions

        self.archanodes = ["Format", "Support", "IDs", "Aliases", "Definitions", "Entries"]     # This is a set containing known ARCHA node names
        self.format = None
        self.support = None
        self.ids = None
        self.aliases = None
        self.definitions = None
        self.entries = None
        self.extranodes = SmlElement("Extra Nodes")     # This is where you'll append the extra unknown nodes found across read calls.

        self.unsavednodes = []   # Append loaded nodes, remove individually saved nodes. Used for saving all remaining nodes at once.

        
    def __str__(self) -> str:
        pass

    def smlread(self, path: str = None):
        
        # If no path or incorrect path, use default path from parent class arguments.
        if path == None or type(path) != str:   
            path = self.path

        try:
            file = SmlDocument.load(path)
            file.setEndKeyword(None)
        except:
            print("Couldn't find SML document in provided path")

        root = file.getRoot()

        if root.getName() != "ARCHA":
            print("SML document does not have ARCHA root")
            return


        # Code that loads any node present in the loaded library that hasn't been loaded yet.
        if self.format == None and root.hasAttribute("Format"):
            self.format = root.attribute("Format")
            self.unsavednodes.append("Format")

        if self.support == None and root.hasElement("Support"):
            self.support = root.element("Support")
            self.unsavednodes.append("Support")

        if self.ids == None and root.hasElement("IDs"):
            self.ids = root.element("IDs")
            self.unsavednodes.append("IDs")

        if self.aliases == None and root.hasElement("Aliases"):
            self.aliases = root.element("Aliases")
            self.unsavednodes.append("Aliases")

        if self.definitions == None and root.hasElement("Definitions"):
            self.definitions = root.element("Definitions")
            self.unsavednodes.append("Definitions")

        if self.entries == None and root.hasElement("Entries"):
            self.entries = root.element("Entries")
            self.unsavednodes.append("Entries")

        for node in root.nodes:        # Store the extra unknown nodes
            if self.archanodes.count(node.getName()) == 0:
                self.extranodes.add(node)
                self.unsavednodes.append(node.getName())




    def smlwrite(self, path: str = None, nodestosave: list = None, printonly: bool = False): 
        
        # If no path or incorrect path, use default path from parent class arguments.
        if path == None or type(path) != str:
            path = self.path

        root = SmlElement("ARCHA")

        if type(nodestosave) == list:           # If user provided list of specific nodes to save
            for x in nodestosave:
                self.unsavednodes.remove(x)     # Then remove said nodes from list of nodes that have yet to be saved. 
        else:
            nodestosave = self.unsavednodes     # Else generate list of remaining nodes to save from nodes yet to be saved.
        
        while len(nodestosave) > 0:
            match nodestosave[0]:
                case "Format":
                    root.add(self.format)
                case "Support":
                    root.add(self.support)
                case "IDs":
                    root.add(self.ids)
                case "Aliases":
                    root.add(self.aliases)
                case "Definitions":
                    root.add(self.definitions)
                case "Entries":
                    root.add(self.entries)
                case _:
                    for extranode in self.extranodes.nodes:
                        if extranode.getName() == nodestosave[0]:
                            root.add(extranode)
            nodestosave.pop(0)

        file = SmlDocument()
        file.setRoot(root)
        file.setEndKeyword(None)

        if printonly == True:
            print(file)
            print("Would save the above to:",path)
        else:
            file.save(path)

    def smlbackup(self, path: str = None):

        # If no path or incorrect path, use default path from parent class arguments.
        if path == None or type(path) != str:   
            path = self.path

        file = SmlDocument.load(path)
        file.setEndKeyword(None)
        newpath = path.replace(".txt",".txt.old")
        file.save(newpath)

        # Should probably edit that code to make use of native Python file operations for better performance.
        # It would also make the backup method cross compatible with SML and JSON.
        # Also add support for multiple backups.


