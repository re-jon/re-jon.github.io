---
layout: post
title: How to use Wget
author: Regina Jonach
---

1) Create a folder with mkdir, for example  wget_project

2) Move into this folder

3) Open a file with an editor 

4) On the webside from which you like to wget files, open > inspector [Element untersuchen] with left mouse-click and look
for example for the XML-files

5) a) copy desired href-links into editor:
    
    <a href="/cds/downloads/MDSConnect/BooksAll.2014.part41.xml.gz">Part 41</a>

  b) copy the http link of the webside in the same file

      http://www.loc.gov/cds/products/MDSConnect-books_all.html


6) with _find_and _replace_ :
   
  a) Clean links from href 
    
~~<a href="~~

    /cds/downloads/MDSConnect/BooksAll.2014.part41.xml.gz

 ~~">Part 41</a>~~
   

b) and add http_extension of webside to each link

    http://www.loc.gov/cds/

   ~~products/MDSConnect-books_all.html~~

c) safe cleared links 

    http://www.loc.gov/cds/downloads/MDSConnect/BooksAll.2014.part41.xml.gz

   to a **.txt file**, for example _scrap.txt_


d) safe the file to your wgt_project directory
    

7) In your wget_project directory set the command:
    
    wget -i scrap.txt


For further information on wget, have a look at:

    https://www.gnu.org/software/wget/manual/wget.pdf


