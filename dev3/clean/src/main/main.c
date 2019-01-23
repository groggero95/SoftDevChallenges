#include "main.h"
#include "../lib_foo/foo.h"
#include <mistery.h>

int main(){
    int value;

    print_today();
    value = MISTERY_VALUE(2);
    printf("The mistery value is %i", value);
    return 0;
}
