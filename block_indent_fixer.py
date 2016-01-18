######################################################################
# This Python2.7 script accepts a filename (full path) for parsing.  #
# It will apply the next-line's indentation to any empty (no spaces, #
# or characters) line, except the first and last lines, if the       #
# previous-line has (any) indentation, as well.                      #
######################################################################

import sys, os
import re

# Can be \t's or spaces.
r = re.compile(r"^\s+")

try:
    filename = sys.argv[1]
except:
    filename = None
    while not filename:
        filename = raw_input("Full path to file for parsing: ")

DIR = os.path.dirname(filename)
try:
    fileparts       = os.path.basename(filename).split(".")
    fileBasename    = fileparts[0]
    fileExtension   = fileparts[1]
except:
    fileBasename    = os.path.basename(filename)
    fileExtension   = ""

try:
    with open(filename) as f:
        fileData = f.read()
except Exception as e:
    print "Filed to open file: "+str(e)
    print "Leaving..."
    sys.exit()

fileDataLines = fileData.splitlines()

# Find any empty lines that doesn't have the same idents
# of the lines before and after it, and apply those idents to it.
counter = 0
for i in range(len(fileDataLines)):
    try:
        prevLine = fileDataLines[i-1]
        curLine = fileDataLines[i]
        nextLine = fileDataLines[i+1]
    except:
        # First and last lines are ignored.
        continue
    
    # prev and next must have indents.
    try:
        prevLineIndent = r.search(prevLine).group(0)
        nextLineIndent = r.search(nextLine).group(0)
    except:
        continue
    
    # cur must be empty, completely.
    if curLine:
        continue
    
    # apply nextline indent to current line.
    fileDataLines[i] = nextLineIndent + fileDataLines[i]
    counter += 1

# save to new file.
newFilename = fileBasename + "_fixed." + fileExtension
with open(os.path.join(DIR, newFilename), "w") as f:
    f.write("\n".join(fileDataLines)+"\n")

print "Finished fixing "+str(counter)+" unindented lines!"
print "Saved result: "+newFilename
