"""YML python librairy. This librairie allow python developpers to open, create and edit .yml files."""
import ymlerrors

#######################################################
# FOR THIS LIBRAIRY, USE PATH WITH "\" AND NOT "/"    #
#######################################################

class YMLFile(object):
    """Class for YML files."""
    def __init__(self, path, name):
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
        with open(self.file, "r") as f:
            self.in_f = f   #read the file
        self.lines = self.in_f.split("\n")
        self.lines2 = []
        for i in self.lines:
            if i[0] == "#":
                print("One comment line skipped !")
                continue    #Go to next line if all the line is a comment
            self.lines2.append(i.split("#")[0]) #Remove comments
        for self.j, self.i in enumerate(self.lines2):
            x = self.i.split(": ")
            if len(x) == 0:
                raise ymlerrors.YMLSyntaxException("A line haven't got \": \" caracter and isn't a comment !\n--> SyntaxError")
            elif len(x) > 1:
                raise ymlerrors.YMLSyntaxException("A line have more than one \": \" caracter and isn't a comment !\n--> SyntaxError")
            if x[1] == "":
                self.add_section(x[0])
                continue
            else:
                self.add_value(x[0], x[1])
                continue

    def add_section(self, name):
        """start reading a subCategory
        Arguments:
        name : the name of the section (str)"""
        path = {}
        w = self.lines2[self.j-len(self.lines2)]
        print("Starting new section")
        raise ymlerrors.InDeveloppementWarning

    def add_value(self, name, value):
        """start reading a value
        Arguments:
        name : the name of the value (str)
        value : the value itself (ALWAYS str ! --> #will be returned to a str)"""
        self.path[name] = value

    def __del__(self):
        """Will be completed later, for destroy all and clear memory"""
        ...
