      -----------====== CHALLENGE ======-----------
      
The goal of this assignment is to add one command to gdb named "fpointers"
that locates pointers in a given area of memory. The command (that has
to be written in python) should take two parameters, the first representing 
the address of the memory region and the second its size.
The output (see the example below for more info) has to report
all the pointers present in the area that point to other addresses in the 
same range. 

       -----------====== EXAMPLE ======-----------

Compile the public.c program with debugging symbols. 
Then save your code in a file called gdb.py and execute
the following test:

-------------
> gdb public
(gdb) source gdb.py
(gdb) b 20
Breakpoint 1 at 0x400595: file public.c, line 20.
(gdb) run
....
Breakpoint 1, main () at public.c:20
20      printf("Done\n");

(gdb) print first->next
$1 = (struct _test *) 0x602030
(gdb) print &first->next
$2 = (struct _test **) 0x602010

(gdb) fpointers 0x602000 100
Pointer at 0x602010 --> 0x602030
-------------

Verify that the output of your command is consistent with
the location of the first->next pointer. 


