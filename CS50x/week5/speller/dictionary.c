// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

unsigned int count_word;
unsigned int hash_value;
// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hash_value = hash(word);
    node *cursor = table[hash_value];

    while (cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long k = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        k += tolower(word[i]);
    }
    return k % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(f, "%s", word) != EOF)
    {
        node *w = malloc(sizeof(node));
        if (w == NULL)
        {
            return false;
        }

        strcpy(w->word, word);
        hash_value = hash(word);
        w->next = table[hash_value];
        table[hash_value] = w;
        count_word++;
    }
    fclose(f);
    return true;
}
// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count_word;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int h = 0; h < N; h++)
    {
        node *cursor = table[h];
        while (cursor)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }

        if (cursor == NULL && h == N - 1)
        {
            return true;
        }
    }
    return false;
}
