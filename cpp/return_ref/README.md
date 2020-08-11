* function return has RVO
* const T& ref = f(), T f(){ T x; return x }, f return local temp x by value, life time of x will extended by ref
* return local temp var by reference is useless and dangerous
