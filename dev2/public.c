#include<stdio.h> 
#include<string.h>
#include<stdlib.h>

typedef struct _test {
  struct _test* next;
  int    value;
} s;

void main(){
    s* first;

    first = (s*) malloc(sizeof(s));
    first->next = (s*) malloc(sizeof(s));

    first->value = 10;
    first->next->value = 5;
    first->next->next  = 0;

    printf("Done\n");

}
