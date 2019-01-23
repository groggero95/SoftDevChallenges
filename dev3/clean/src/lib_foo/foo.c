#include <stdio.h>
#include "foo.h"
#include <time.h>

void print_today(){
    time_t    t;
    struct tm *tm;
    char buf[100];

    time(&t);
    tm = localtime(&t);

    strftime(buf, sizeof(buf), "Today is: %Y %m %d\n", tm);
    printf("%s",buf);
}

