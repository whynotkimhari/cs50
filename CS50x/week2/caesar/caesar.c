#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);

    string plain_text = get_string("Please insert your plaintext: ");
    printf("ciphertext: ");

    for (int j = 0; j < strlen(plain_text); j++)
    {
        if (isupper(plain_text[j]))
        {
            printf("%c", (plain_text[j] - 65 + k) % 26 + 65);
        }
        else if (islower(plain_text[j]))
        {
            printf("%c", (plain_text[j] - 97 + k) % 26 + 97);
        }

        else
        {
            printf("%c", plain_text[j]);
        }
    }
    printf("\n");
}
