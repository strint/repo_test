* local var in function return has RVO, but no member of class
* const T& ref = f(), T f(){ T x; return x }, f return local temp x by value, life time of x will extended by ref
* lambda is a kind of functor, capture values are var members
* std::functioin store lambda, there is 3 copies when lambda capture by value;
  * why
  * always try to pass by ref(is ptr) or pass by shared_ptr
