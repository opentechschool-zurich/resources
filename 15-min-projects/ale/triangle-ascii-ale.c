#include <stdio.h>

int get_height(void);
void print_blocks(int line);
void print_spaces(int n);
void print_line(int line, int height);
void print_pyramid(int height);

int main(void)
{
    print_pyramid(10);
}

void print_blocks(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" #");
    }
}

void print_spaces(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

void print_line(int line, int height)
{
    // the hollow triangle
    print_spaces(height - line);
    printf("#");
    if (line == height)
    {
        // the last line must be a "full" one
        print_blocks(line - 1);
    }
    else if (line > 1)
    {
        // all lines but the first one have a second # on the right side
        print_spaces((line - 1) * 2 - 1);
        printf("#");
    }
    printf("\n");
}

void print_pyramid(int height)
{
    for (int line = 1; line <= height; line++)
    {
        print_line(line, height);
    }
}
