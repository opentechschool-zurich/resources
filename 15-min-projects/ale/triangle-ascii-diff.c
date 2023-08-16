5,6c5,6
< void print_spaces(int n);
< void print_line(int line, int height);
---
> void print_spaces(int line, int height);
> void print_lines(int line, int height);
11c11,12
<     print_pyramid(10);
---
>     int height = get_height();
>     print_pyramid(height);
14c15
< void print_blocks(int n)
---
> int get_height(void)
16c17,28
<     for (int i = 0; i < n; i++)
---
>     int height = 0;
>     do
>     {
>         height = get_int("Height: ");
>     }
>     while (height > 8 || height < 1);
>     return height;
> }
> 
> void print_blocks(int line)
> {
>     for (int blocks = 1; blocks <= line; blocks++)
22c34
< void print_spaces(int n)
---
> void print_spaces(int line, int height)
24c36
<     for (int i = 0; i < n; i++)
---
>     for (int spaces = height - line; spaces > 0; spaces--)
30c42
< void print_line(int line, int height)
---
> void print_lines(int line, int height)
32c44
<     print_spaces(height - line);
---
>     print_spaces(line, height);
41c53
<         print_line(line, height);
---
>         print_lines(line, height);
43a56,57
> 
> /// with every line add spaces (base -1) and stars(++), base = line
