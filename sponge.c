#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int i = 0, random;
    time_t t;
    char string[1024];

    printf("Enter a string.\n");
    scanf("%[^\n]", string);

    srand((unsigned) time(&t));

    while(string[i++] != '\0')
    {
        random = rand() % 2;
        if(random)
        {
            string[i] = tolower(string[i]);
        }
        else
        {
            string[i] = toupper(string[i]);
        }
    }

    printf("\n");
    printf("%s\n", string);
}