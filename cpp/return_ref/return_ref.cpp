#include <string>
#include <iostream>
#include <functional>

std::function<const std::string &()> getFunc() {
    std::string str = "str";
    auto func = [str]() -> const std::string& { return str; };
    return func;
}

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
    A(const A& a) { x = a.x; std::cout << "A::A(" << x << ") copy" << std::endl; }
    int Out() const { std::cout << x << ", " << __LINE__ << std::endl;}
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

void getFunc2(std::function<const A&()>& func) {
    A a(4);
    std::cout << "before func2" << std::endl;
    func = [a]() -> const A& { return a; };
    std::cout << "after func2" << std::endl;
}

void getFunc3(std::function<A()>& func) {
    A a(5);
    std::cout << "before func3" << std::endl;
    func = [a]() -> A { return a; };
    std::cout << "after func3" << std::endl;
}

void getFunc4(std::function<const A&()>& func) {
    std::cout << "before func4" << std::endl;
    func = []() -> const A& { A a(6); return a; };
    std::cout << "after func4" << std::endl;
}

void getFunc5(std::function<A()>& func) {
    std::cout << "before func5" << std::endl;
    func = []() -> A { A a(7); return a; };
    std::cout << "after func5" << std::endl;
}


int main()
{
    auto func = getFunc();
    std::cout << func() << std::endl;

    std::cout << "before Func2" << std::endl;
    std::function<const A&()> func2;
    getFunc2(func2);
    std::cout << "after Func2" << std::endl;
    func2().Out();

    std::cout << "before Func3" << std::endl;
    std::function<A()> func3;
    getFunc3(func3);
    std::cout << "after Func3" << std::endl;
    func3().Out();

    std::cout << "before Func4" << std::endl;
    std::function<const A&()> func4;
    getFunc4(func4);
    std::cout << "after Func4" << std::endl;
    func4().Out();

    std::cout << "before Func5" << std::endl;
    std::function<A()> func5;
    getFunc5(func5);
    std::cout << "after Func5" << std::endl;
    func5().Out();

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
