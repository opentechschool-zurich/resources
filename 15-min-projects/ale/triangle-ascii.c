#include <stdio.h>

int get_height(void);
void print_blocks(int line);
void print_spaces(int line, int height);
void print_lines(int line, int height);
void print_pyramid(int height);

int main(void)
{
    int height = get_height();
    print_pyramid(height);
}

int get_height(void)
{
    int height = 0;
    do
    {
        height = get_int("Height: ");
    }
    while (height > 8 || height < 1);
    return height;
}

void print_blocks(int line)
{
    for (int blocks = 1; blocks <= line; blocks++)
    {
        printf("# ");
    }
}

void print_spaces(int line, int height)
{
    for (int spaces = height - line; spaces > 0; spaces--)
    {
        printf(" ");
    }
}

void print_lines(int line, int height)
{
    print_spaces(line, height);
    print_blocks(line);
    printf("\n");
}

void print_pyramid(int height)
{
    for (int line = 1; line <= height; line++)
    {
        print_lines(line, height);
    }
}

/// with every line add spaces (base -1) and stars(++), base = line
