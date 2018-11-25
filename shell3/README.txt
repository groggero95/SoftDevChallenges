  -----------====== The Challenge  ======--------------

In order to save space on your new solid state disk, you want to 
automatically compress all the directories that do not contain
at least one file used in the last month.

For example, suppose you run the command from inside the followin directory:

./file1
./dirA
 ./dirA/dirC
  ./dirA/dirC/file4
  ./dirA/dirC/file5
  ./dirA/dirC/dirD
   ./dirA/dirC/dirD/file8
   ./dirA/dirC/dirD/file6
   ./dirA/dirC/dirD/file7
 ./dirA/dirE
  ./dirA/dirE/file9
 ./dirA/file2
 ./dirA/file3
./dirB
 ./dirB/file10
  ./dirB/dirF
   ./dirB/dirF/file11
   ./dirB/dirF/file12
   ./dirB/dirF/dirG
    ./dirB/dirF/dirG/file13

Where the only files that have been accessed in the past month are file10 and file6.

After you run your command, the direcory has to look like this:

./file1
./dirA
 ./dirA/dirC
  ./dirA/dirC/file4
  ./dirA/dirC/file5
  ./dirA/dirC/dirD
   ./dirA/dirC/dirD/file8
   ./dirA/dirC/dirD/file6
   ./dirA/dirC/dirD/file7
 ./dirA/dirE.tgz
 ./dirA/file2
 ./dirA/file3
./dirB
 ./dirB/file10
  ./dirB/dirF.tgz

You can use any combination of command line programs, but you CANNOT
use scripting languages such as perl or python

   -----------====== Help  ======--------------

* Check the atime for each file
* To compress a directory you can use the tar command
  (and save the archive in a .tgz file)
* To test your solution, you can play around with the
  "touch" command

 -----------====== Submission  ======--------------

Write your command(s) in a file called solution.
The file is then places in a directory and executed by 
invoking "bash solution".
At the end of the execution, all the subdirectories that do not
contain at least one file accessed in the last month should
be compressed.

Make sure you test your script on the example described above
*before* submitting the file.

