#include "algos/sobriete76.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char* string = erase("  b o n j  o u r  ");
    printf("sobriete76:\n");
    printf("|%s|\n", string);
    printf("strcmp: %d", strcmp(string, "  bonj  our  "));
    return 0;
}
