       -----------====== CHALLENGE ======-----------

You are very proud of your new very lame program
("lame_project.tgz") and you want to distribute it to the 
world so that it can be compiled for every existing system.

In order to do that you decided to use autotools.
For this challenge you have to write the required Makefile.am 
(maybe more than one) and the "configure.ac" and add them to the project.

The rules are simple:
* Lib_foo must be compiled but NOT installed
* The main application must be compiled and installed under project/uselessbin/
* The main application uses a "mistery_value" function.
  The function is defined in "mistery.h" but the actual library containing the 
  implementation can be different in different systems. In particular, 
  it can be implemented in one of these libraries: 
   'magic', 'voodoo', or 'mistery'
  Make sure that **the configure script** (and not yourself) can find the 
  right one.

  Moreover, the mistery_value function can have one or two parameters depending
  on the systems. To be more general, main.h defines the appropriate
  "#define". Make sure that the configure script will set the variables 
  according to the number of parameters.
   
       -----------====== SUBMISSION ======-----------

Add the two required files, re-create the tgz archive, and submit it.
The project will be tested by running:

> cd project
> aclocal
> autoheader
> automake -a
> autoconf
> ./configure
> make
> make install
> ./uselessbin/mistery_foo


