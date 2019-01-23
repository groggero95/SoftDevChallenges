#include "config.h"

#ifdef MISTERY_VALUE_ONEPARAM
 #define MISTERY_VALUE(x) mistery_value(x)
#else
 #define MISTERY_VALUE(x) mistery_value(x,1)
#endif


