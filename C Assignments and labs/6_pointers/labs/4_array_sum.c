#include <stdio.h>

int arr_sum(int *ptr, int arr_len)
{
    int sum = 0;
    while (arr_len > 0)
    {
        sum += *ptr;
        ptr++;
        arr_len--;
    }
    
    return sum;
}

int main(void)
{
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    printf("Summation = %d\n", arr_sum(&arr[0], 10));
    
    return 0;
}