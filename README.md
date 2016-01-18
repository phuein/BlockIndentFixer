# Block Indent Fixer
Fixes/Restores the indents (tabs) in empty lines, within indented blocks of code.

This Python2.7 script accepts a filename (full path) for parsing. 
It will apply the next-line's indentation to any empty (no spaces, 
or characters) line, except the first and last lines, if the 
previous-line has (any) indentation, as well.

In other words, if some evil editor (like Atom Jan' 2016) cleared all the whitespace-only lines in your Python code,
and for some reason you didn't revert immediately, this will restore them as indented lines.

Example:
http://i.imgur.com/s7lnA8Z.png
