#ifndef IMPLE2_H
#define IMPLE2_H
// Libraries 
#include <cstring>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <list>
#include <fstream>
#include <stdlib.h>

using namespace std;

struct keywords {
    int line_pos, keyword_pos;
};

struct all_lines {
    vector<string> vs;
} line;

vector<string> readwordlist;
static vector<all_lines> vectorLine;
static vector<keywords> vectorKeyword;

bool cShiftFilter(const keywords &a, const keywords &b);
class Filters { 
    public: 
        void InputFilter(string inputKeyword);
        void readWordsFilter();

};

class AlphabetizerAndOutput {
    public:
        void after_cshifting();

};

#endif