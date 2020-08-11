#include <string>
#include <iostream>

std::string getStr1() {
    std::string str = "str1";
    return str; 
}

const std::string& getStr2() {
    std::string str = "str2";
    return str; 
}


class A {
public:
    A(int xx) : x(xx) { std::cout << "A::A(" << x << ")" << std::endl; }
    int Out() const { std::cout << x << std::endl;}
private:
    int x{0};
};

const A& getA1()
{
    A a(1);
    return a;
}

A& getA2()
{
    A a(2);
    return a;
}

A getA3()
{
    A a(3);
    return a;
}


int main()
{
    const std::string& str1 = getStr1();
    std::cout << str1 << std::endl;
    const std::string& str2 = getStr2();
    std::cout << str2 << std::endl;

    const A& newA1 = getA1(); //1
    newA1.Out();

    A& newA2 = getA2(); //2
    newA2.Out();

    A newA3 = getA3(); //3
    newA3.Out();

    const A& newA4 = getA3(); //4
    newA4.Out();
}
