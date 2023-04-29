#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int main(void)
{
    string text = get_string("Please insert the text: ");
    int letter = count_letters(text);
    int word = count_words(text);
    int sentence = count_sentences(text);

    float index, L, S;
    L = ((float) letter / (float) word) * 100;
    S = ((float) sentence / (float) word) * 100;
    index = (0.0588 * L - 0.296 * S - 15.8);
    int q = round(index);

    if (q >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (q < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", q);
    }
}

int letter;
int count_letters(string text)
{
    int i;
    for (i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letter++;
        }
    }
    return letter;
}

int word;
int count_words(string text)
{
    int j;
    for (j = 0; j < strlen(text); j++)
    {
        if (text[j] == ' ')
        {
            word++;
        }
    }
    return (word + 1);
}

int sentence;
int count_sentences(string text)
{
    int k;
    for (k = 0 ; k < strlen(text); k++)
    {
        if (text[k] == '.' || text[k] == '!' || text[k] == '?')
        {
            sentence++;
        }
    }
    return sentence;
}