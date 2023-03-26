#include <stdio.h>

int main(void)
{
    int x, y, z;
    int *p, *q, *r;

    x = 10;
    y = 20; 
    z = 30;
    p = &x;
    q = &y;
    r = &z;

    printf("x = %d\n", x);
    printf("y = %d\n", y);
    printf("z = %d\n", z);
    printf("p = %p\n", p);
    printf("q = %p\n", q);
    printf("r = %p\n", r);
    printf("*p = %d\n", *p);
    printf("*q = %d\n", *q);
    printf("*r = %d\n", *r);

    printf("Swapping pointers\n");
    r = &x;
    p = &y;
    q = &z;
    printf("x = %d\n", x);
    printf("y = %d\n", y);
    printf("z = %d\n", z);
    printf("p = %p\n", p);
    printf("q = %p\n", q);
    printf("r = %p\n", r);
    printf("*p = %d\n", *p);
    printf("*q = %d\n", *q);
    printf("*r = %d\n", *r);
    return 0;
}