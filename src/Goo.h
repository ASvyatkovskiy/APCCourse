#if !defined(GOO_H)
#define GOO_H

#include <string>

//$ begin Goo
class Goo {
public:
    Goo() : i_(0), s_("") {}
    Goo(int i) : i_(i), s_("") {} Goo(std::string const& s) : i_(0), s_(s) {}
    int getI() const { return i_; }
    std::string getS() const { return s_; }
private:
    int i_;
    std::string s_;
};
//$ end
#endif

