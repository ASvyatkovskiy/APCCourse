//$ begin include_iostream_iterator
#include <iostream>
#include <iterator>
//$ end
#include <sstream>
#include <string>
#include <vector>

#include "boost/shared_ptr.hpp"

#define OVERLOADS 1
//$ begin greet_s
std::string greet(const std::string &str="world") {
    return "hello " + str;
}
//$ end

#if OVERLOADS > 1
//$ begin greet_s2
std::string greet(const std::string &str, int nrepeat) {
    std::ostringstream ss;
    ss << "Hello";
    for (int i = 0; i != nrepeat; ++i) ss << " " << str;
    return ss.str();
}
//$ end

//$ begin greet_i
std::string greet(int i) {
    std::ostringstream ss;
    ss << "Hello " << i;
    return ss.str();
}
//$ end
#endif

/************************************************************************************************************/

//$ begin class_X
class X {
public:
    void set(const std::string& msg) { msg_ = msg; }
    std::string greet() { return "hello " + msg_; }
private:
    std::string msg_;
};
//$ end

//$ begin class_Y
struct Y {
    int i;
};
//$ end

//$ begin class_Z
struct Z {
    X& getX() { return x; }
    X x;
    Y *y;
};
//$ end

//$ begin goo
X& goo(Z &z, Y *y) {
    z.y = y;
    return z.x;
}
//$ end

/************************************************************************************************************/

//$ begin print_vector
template<typename T>
void print_vector(const std::vector<T>& v) {
    std::copy(v.begin(), v.end(),
              std::ostream_iterator<T>(std::cout, " "));
    std::cout << std::endl;
}
//$ end

/************************************************************************************************************/

//$ begin makeVectorX
std::vector<boost::shared_ptr<X> > makeVectorX()
{
    const int n = 2;
    std::vector<boost::shared_ptr<X> > v(n);

    v[0] = boost::shared_ptr<X>(new X); v[0]->set("Robert");
    v[1] = boost::shared_ptr<X>(new X); v[1]->set("Lupton");

    return v;
}
//$ end

/************************************************************************************************************/
/************************************************************************************************************/
//$ begin boost_python_hpp
#include "boost/python.hpp"
//$ end
//$ begin indexing_suite_hpp
#include "boost/python/suite/indexing/vector_indexing_suite.hpp"
//$ end

#if OVERLOADS == 1
//$ begin overloads
BOOST_PYTHON_FUNCTION_OVERLOADS(greet_s_overloads, greet, 0, 1)
//$ end
#elif OVERLOADS == 2
//$ begin overloads_i_s2
std::string (*greet_i)(int) = &greet;
std::string (*greet_s)(const std::string &, int i) = &greet;

BOOST_PYTHON_FUNCTION_OVERLOADS(greet_s_overloads, greet, 0, 2)
//$ end
#endif

//$ begin BOOST_PYTHON_MODULE
BOOST_PYTHON_MODULE(speak)
{
    using namespace boost::python;
//$ end

#if OVERLOADS == 0
//$ begin define_greet
    def("greet", greet);
//$ end
#elif OVERLOADS == 1
//$ begin define_greet_overloads
    def("greet", greet, greet_s_overloads());
//$ end
    #else
//$ begin define_greet_overloads_i_s2
    def("greet", greet_i);
    def("greet", greet_s, greet_s_overloads());
//$ end
#endif

/************************************************************************************************************/
    
#if 0
//$ begin define_X
    class_<X>("X")
        .def("greet", &X::greet)
        .def("set",   &X::set)
    ;
//$ end
#endif
//$ begin define_X_shared
    class_<X, boost::shared_ptr<X> >("X")
        .def("greet", &X::greet)
        .def("set",   &X::set)
    ;
//$ end

//$ begin define_Y
    class_<Y>("Y")
        .def_readwrite("i",   &Y::i)
    ;
//$ end

//$ begin define_Z
class_<Z>("Z")
  .def("getX",       &Z::getX, return_internal_reference<1>())
  .add_property("y",
   make_getter(&Z::y, return_value_policy<reference_existing_object>()),
   make_setter(&Z::y, return_value_policy<reference_existing_object>()))
  ;
//$ end

//$ begin define_goo
    def("goo", goo,
        return_internal_reference<1, with_custodian_and_ward<1, 2> >());
//$ end

/************************************************************************************************************/

    //$ begin define_vectorDouble
    class_<std::vector<double> >("vectorDouble")
        .def(vector_indexing_suite<std::vector<double> >())
        ;
    //$ end

    //$ begin define_print_vector
    def("print_vector", print_vector<double>);
    //$ end

/************************************************************************************************************/

    //$ begin define_vectorX
    class_<std::vector<boost::shared_ptr<X> > >("vectorX")
        .def(vector_indexing_suite<std::vector<boost::shared_ptr<X> >,
                                   true>())
        ;
    //$ end

    //$ begin define_shared_ptrX
    def("makeVectorX", makeVectorX);
    //$ end

//$ begin end_BOOST_PYTHON_MODULE
}
//$ end
