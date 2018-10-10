#include <iostream>
int main()
{
    int zahl{124};
    int e{zahl % 10};
    zahl /= 10;
    int z{zahl % 10};
    int h{zahl / 10};
    std::cout << e + z + h << std::endl;
}
