---
layout: post
title : "Homework 8: Access Data with Python and Regex"
author: Regina Jonach
---
8a:Python Script that will create clean copies of text of each issue

1) Open a new directory, for example DATAEXTRACT

2) Copy the folder with the xml. data into this directory

3) Open a file in an editor (for example Sublime) and safe the
   file with extension  .py in the same directory, for example gettext.py

4) Write your code in this file, for example (Here I did it with Python 2.x.x): 

![File.py in Editor](/img/digi-homew0.JPG)

5) Make sure the indentations are correct
   Here the same code (copy&pastable):

![Indentations!](/img/digi-homew0a.JPG)


6)Open the terminal and go into directory DATAEXTRACT. Execute
  your file with the command:   python gettext.py

7) This code creates new files for the text accessed from the sourcefiles:

![Modified Files](/img/digi-homew1a.JPG)

8) Content of modified file:

![Content](/img/digi-homew2.JPG)





8b: Python script that will create clean copies of articles only

9) The source xml-files provide the key-word "articles" in order to access
   text written under this keyword

![Keyword "article"](/img/regex_perseus.png)


10) For this code to be executed I used Python 3. Please not that
the encoding="utf-8" - attribute only works when using Python 3 and
that there is a dash between utf and 8. If you run two version of Python on
your plattform, the command for Python3 to be used is:   python3 gettext.py

![Code for "article"](/img/digi-homew2-0.JPG)

11) I have used a different filename for the new file created. Apparently
the text of the header of the xml-file  is accessed by default.  But one can see that there
is a slight difference in the file size.

![File size difference](/img/digi-homew2-1.JPG)
