"""YML python librairy. This librairie allow python developpers to open, create and edit .yml files."""
import ymlerrors

#######################################################
# FOR THIS LIBRAIRY, USE PATH WITH "\\" AND NOT "/"    #
#######################################################

class YMLFile(object):
    """Class for YML files."""
    def __init__(self, path:str, name:str):
        """Constructor of this class.
        Arguments :
        - path : the path to the file (str)
        - name : the name of the file (str)"""
        self.name = name
        self.path = path
        self.sub = []
        if self.path[-1] == "\\":
            self.self = self.path + self. file
        else:
            self.self = self.path + "\\" + self. file
        ...
        
    def read(self):
        """Read the file and return a dico"""
        f = open(self.path, "r")
        content = f.read()
        f.close()
        
        dico = {}
        
        return dico

class Editor(object):
    """Class who will edit in YML files."""
    def __init__(self, file, out="file.yml"):
        """Constructor of this class."""
        ...

class Reader(object):
    """Class who will read in YML files."""
    def __init__(self, file):
        """Constructor of this class."""
        self.file = file
        self.lines = []
        self.path = {}

    def read(self):
        """Start reading the file."""
        self.nblines = 0
        with open(self.file, "r") as f:
            self.in_f = f   #read the file
        self.lines = self.in_f.split("\n")
        self.lines2 = []
        for i in self.lines:
            if i[0] == "#":
                print("One comment line skipped !")
                continue    #Go to next line if all the line is a comment
            self.lines2.append(i.split("#")[0]) #Remove comments
        self.maxnblines = len(self.lines2)
        

    def add_section(self, name, indent):
        """start reading a subCategory
        Arguments:
        name : the name of the section (str)
        --> return a dictionnary"""
        

    def add_value(self, name, value):
        """start reading a value
        Arguments:
        name : the name of the value (str)
        value : the value itself (ALWAYS str ! --> #will be returned to a str)"""
        self.path[name] = value

    def __del__(self):
        """Will be completed later, for destroy all and clear memory"""
        ...
