"""YML python librairy. This librairie allow python developpers to open, create and edit .yml files."""

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

class SubCategory(object):
    """Subcategory in a YML file"""
    def __init__(self, name):
        """Constructor"""
        ...

class Value(object):
    """Value in a YML file"""
    def __init__(self, name, default):
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
        self.subcategory = []

    def read(self):
        """Start reading the file."""
        with open(self.file, "r") as f:
            self.in_f = f
        self.lines = self.in_f.split("\n")
        for i in self.lines:
            sub = i.split(":")
            if sub[1] == "" or sub[1] == " ":
                ...

    def start_section(self, name):
        """start reading a subCategory"""
        ...