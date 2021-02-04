#include <iostream>

int test() {
  return ({
      3;
      });
}

int test1() {
  return ({
      return 2;
      3;
      });
}

int test2() {
  return ({
      if (true){
      return 1;
      }
      3;
      }) + 1;
}

int main() {
  std::cout << "test out : " << test() << std::endl;   // get 3
  std::cout << "test out : " << test1() << std::endl;  // get 2
  std::cout << "test out : " << test2() << std::endl;  // get 1
  return 0;
}
