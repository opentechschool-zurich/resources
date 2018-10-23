#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> sum (std::vector<int> a, std::vector<int> b)
{
    std::vector<int> result{};

    int n_a = a.size() - 1;
    int n_b = b.size() - 1;
    int n = std::max(n_a, n_b);

    int remainder{0};
    int value{0};
    for (int i = 0; i < n + 1; i++) {
        value = remainder;
        if (i <= n_a) {
            value += a.at(n_a - i);
        }
        if (i <= n_b) {
            value += b.at(n_b - i);
        }
        if (value > 9) {
            remainder = 1;
            value -= 10;
        } else {
            remainder = 0;
        }
        result.push_back(value);
    }
    if (remainder > 0) {
        result.push_back(remainder);
    }

    std::reverse(result.begin(), result.end());
    return result;
}

int main()
{
    {
        auto result = sum({1, 2, 3}, {5, 7, 8});
        for (auto d: result) {
            std::cout << d;
        }
        std::cout << std::endl;
    }
    {
        auto result = sum({9, 9, 9}, {1});

        for (auto d: result) {
            std::cout << d;
        }
        std::cout << std::endl;
    }
}
