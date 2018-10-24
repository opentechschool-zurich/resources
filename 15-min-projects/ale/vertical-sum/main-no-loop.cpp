#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

void left_pad(std::vector<int>& v, int size)
{
    std::vector<int> zeros(size - v.size(), 0);
    v.insert(v.begin(), zeros.begin(), zeros.end());
}

int plus(int a, int b)
{
    static int remainder = 0;
    int sum = remainder + a + b;
    remainder = sum > 9 ? 1 : 0;
    sum -= remainder * 10;
    return sum;
}

void print(std::vector<int> v)
{
	std::cout << std::accumulate(v.begin() + 1, v.end(), std::to_string(*v.begin()),
		[](const std::string &s, const int i) { return s + ", " + std::to_string(i); })
	<< std::endl;
}

std::vector<int> sum_vector(std::vector<int> a, std::vector<int> b)
{
    int n = std::max(a.size(), b.size());
    left_pad(a, n);
    left_pad(b, n);
    std::reverse(a.begin(), a.end());
    std::reverse(b.begin(), b.end());
    std::transform (a.begin(), a.end(), b.begin(), a.begin(), plus);
    if (plus(0, 0) > 0) {
        a.push_back(1);
    }
    std::reverse(a.begin(), a.end());
    return a;
}

int main()
{
    print(sum_vector({1,2,3}, {5,6,7}));
    print(sum_vector({9,9,9}, {1}));
}
