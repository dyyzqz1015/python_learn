#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int simple_function(void) {
    static int counter = 0;
    counter++;
    return counter;
}

void add_one_to_string(char *input) {
    int ii = 0;
    for (; ii < strlen(input); ii++) {
        input[ii]++;
    }
}


void free_C_string(char* ptr) {
    printf("         About to free %p(%ld):  %s\n", ptr, (long int)ptr, ptr);
    free(ptr);
}

void func5_print_but_do_not_free_string(char* ptr) {
    printf("         About to free %p(%ld):  %s\n", ptr, (long int)ptr, ptr);
}

