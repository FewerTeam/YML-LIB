# YML Librairy
A Python 3 librairy for open, create and edit .yml files.
## ! in path use "\" and not "/"

# Documentation of this project is in "DOC/Doc.html"
### Format of the files :
  \#a comment

  value_name: value_in_str alWAYS ! \#with another comments

  section_name:

    an_othervalue: 4.5 \#always a string

### Format in this lib :
  yml = {"value_name" : "value_in_str", "section_name" : {"an_othervalue" : "4.5"}}   \#It remove the comments !