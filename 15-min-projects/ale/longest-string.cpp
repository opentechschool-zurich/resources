// we have some text and we have to find the longest line#

#include<string>
#include<iostream>
#include<algorithm>

int main() {
    std::string text = "some text\nanother line\nthird line\n";
 
    int count = 0;
    int max_length = 0; // MIN_INT
    int start_longest = 0;
    // for (char c: text) {}
    for (int i = 0; i < text.length(); i++) {
        // std::cout << text[i] << "\n";
        if (text[i] == '\n') {
            // std::cout << count << "\n";
            if (count > max_length) {
                start_longest = i - count;
                max_length = count;
            }
            // max_length = std::max(max_length, count);
            count = 0;
        } else {
            count += 1;
        }          
    }
    std::cout << max_length << "\n";
    std::cout << text.substr(start_longest, max_length) << "\n";
}
