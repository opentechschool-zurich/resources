#include <cassert>
#include <string>

std::string dash_to_camel_case(std::string text)
{
    for (int i = 0; i < text.size(); i++) {
        if (text.at(i) == '_' || text.at(i) == '-') {
            text.erase(i, 1);
            try {
                text.at(i) = std::toupper(text.at(i));
            } catch (const std::exception& e) {
                // ignore the _ or - at the end of the sring
            }
        }
    }
    return text;
}

int main()
{
    assert(dash_to_camel_case("this_is_my_variable") == "thisIsMyVariable");
    assert(dash_to_camel_case("join_the_party") == "joinTheParty");
}
