#include <iostream>
#include <cassert>

class Fraction
{
    public:
        Fraction(int nom, int den): nom{nom}, den{den} {}
        int nom;
        int den;
        Fraction operator+(const Fraction& other)
        {
            return {nom * other.den + other.nom * den, den * other.den};
        }
        Fraction operator-(const Fraction& other)
        {
            return {nom * other.den - other.nom * den, den * other.den};
        }
};

bool operator==(const Fraction& lhs, const Fraction& rhs)
{
    return lhs.nom == rhs.nom && lhs.den == rhs.den;
}

std::ostream &operator<<(std::ostream &os, Fraction const &m) { 
    return os << m.nom << " / " << m.den;
}

class FractionItem
{
    public:
        FractionItem(int n) : n{n} {}
        int n;
        Fraction operator/(const FractionItem& other)
        {
            return Fraction{n, other.n};
        }
};

FractionItem operator"" _fr ( unsigned long long n )
{
        return FractionItem(n);
}


int main()
{
    std::cout << Fraction{3, 4} + Fraction{2, 3} << std::endl;
    std::cout << Fraction{1, 2} + Fraction{3, 5} << std::endl;
    std::cout << Fraction{1, 2} - Fraction{1, 4} << std::endl;
    assert((Fraction{1, 2} - Fraction{1, 4}) == (Fraction{2, 8}));
    std::cout << (3_fr / 4_fr) + (2_fr / 3_fr)  << std::endl;
    std::cout << (1_fr / 2_fr) + (3_fr / 5_fr)  << std::endl;
    std::cout << (1_fr / 2_fr) - (1_fr / 4_fr)  << std::endl;
    assert(1_fr / 2_fr - 1_fr / 4_fr == 2_fr / 8_fr);
}
