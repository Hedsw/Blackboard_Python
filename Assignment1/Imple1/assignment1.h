#ifndef ASSIGNMENT1_H
#define ASSIGNMENT1_H

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


static vector<all_lines> vectorLine;
static vector<keywords> vectorKeyword;

bool Filter_cshift(const keywords &a, const keywords &b);
bool alphabetizing(all_lines First, all_lines Second);

class InputFilter { 
    public: 
    void inputfunction(string inputKeyword);
    void readWordsFilter();

};

class Shift_Alphabet{
    public:
    void aftercircularshifting();

};


#endif