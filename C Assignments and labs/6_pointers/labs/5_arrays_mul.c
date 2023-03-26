#include <stdio.h>

int arrays_mul(int *ptr1, int *ptr2, int size)
{
    int scaler_mul = 0;
    while (size > 0)
    {
        scaler_mul += (*ptr1) * (*ptr2);
        ptr1++;
        ptr2++;
        size--;
    }
    return scaler_mul;
}

int main(void)
{
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5] = {1, 2, 3, 4, 5};

    printf("Scaler multiplication = %d\n", arrays_mul(arr1, arr2, 5));
    return 0;
}