    -----------====== The Story  ======--------------

You have added a new section to your homepage containing
a collection of your best pictures. To make things easier,
you want to automatize the creation of the thumbnails using
a makefile.

  -----------====== The Challenge  ======--------------
 
Your project has two subdirectories, 'pictures' where you put the high
resolution photos, and 'thumbs' where you want to put the
automatically generated thumbnails.
The objective is to write a simple Makefile that, when invoked with
'make all' creates, for each '.jpg' file in 'pictures/'
the corresponding thumbnail (with the same file name) under 'thumbs/'.

To create a thumbnail version of picture X, you can invoke the 
following command:

>  convert -thumbnail 100 pictures/X thumbs/X

Important:
The first time the makefile is executed, it has to create the thumbnail 
version of all the photos. If then it is executed again, it has to 
re-generate the thumbnail *ONLY* for the pictures that have been modified
since the last command.

 -----------====== Submission  ======--------------

Submit the Makefile. It will be tested by running
'make all' (first test). Then some pictures will be modified 
and 'make all' will be run again to check that it works as expected
(second test).


