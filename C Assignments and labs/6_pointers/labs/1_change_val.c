#include <stdio.h>

int main(void)
{
    int x = 10;
    int *ptr_x = &x;

    printf("x before changing using pointer: %d\n", x);
    *ptr_x = 20;
    printf("x after changing using pointer: %d\n", x);
    return 0;
}