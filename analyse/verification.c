#include "algos/sobriete76.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    printf("sobriete76:\n");
    printf("|%s|\n", erase("  b o n j  o u r  "));
    printf("strcmp: %d", strcmp(erase("  b o n j  o u r  "), "  bonj  our  "));
    return 0;
}
