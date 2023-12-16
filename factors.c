#include <stdio.h>

int main()
{
    long int num = 239809320265259;
    long int i = 2;
    long int k;

    while (num % i)
    {
        if (i <= num)
        {
            i++;
        }
        else
        {
            return (-1);
        }
    }

    k = num / i;
    printf("%ld = %ld * %ld\n", num, k, i);
    return (0);
}
