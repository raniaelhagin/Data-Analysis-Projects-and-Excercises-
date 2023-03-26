#include <stdio.h>
#include <stdbool.h>

void sort(int* arr_ptr, int size)
{
    int tmp;
    bool is_sorted = true;
    for (int i = size - 1; i > 0; i--)
    {// i = 4
        for (int j = 0; j < i; j++)
        {
            if (arr_ptr[j] > arr_ptr[j+1])
            {
                is_sorted = false;
                tmp = arr_ptr[j];
                arr_ptr[j] = arr_ptr[j+1];
                arr_ptr[j+1] = tmp;
            }
            if (is_sorted)
            {
                break;
            }
        }
    }
    
}
/*
1st iteration: i = 4
    j = 0: 23, 43, 9, 2, 4
    j = 1: 23, 9, 43, 2, 4
    j = 2: 23, 9, 2, 43, 4
    j = 3: 23, 9, 2, 4, 43

2nd iteration: i = 3
    j = 0: 9, 23, 2, 4, 43
    j = 1: 9, 2, 23, 4, 43
    j = 2: 9, 2, 4, 23, 43

3rd iteration: i = 2
    j = 0: 2, 9, 4, 23, 43
    j = 1: 2, 4, 9, 23, 43

4th iteration: i = 1
    j = 0: 2, 4, 9, 23, 43

*/

int main(void)
{
    int arr[5] = {43, 23, 9, 2, 4};
    sort(arr, 5);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}