#include <iostream>
#include <vector>
#include <string>

void draw(int n) {
    if (n < 3) {
        return;
    }
    std::vector<std::string> slices;
    for (int i = 0; i < n - 1; i++) {
        std::string slice = std::string(n - i - 1, ' ') + '#';
        if (i > 0) {
            slice += std::string(i * 2 - 1, ' ') + '#';
        }
        slices.push_back(slice);
    }
    std::string slice;
    for (int i = 0; i < n - 1; i++) {
        slice += "# ";
    }
    slices.push_back(slice + '#');
    for (const auto& slice: slices) {
        std::cout << slice << "\n";
    }
}

int main() {
    draw(10);
}
