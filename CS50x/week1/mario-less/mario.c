#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h, c, r;
    do
    {
        h = get_int("Please insert the height: ");
    }
    while (h<1 || h>8);

    for (r=0; r<h ; r++)
    {
        for (c=1; c <= h; c++)
        {
            if (c< (h - r))
            {
                printf(" ");
            }
            else
                printf("#");
        }
    printf("\n");
    }
}