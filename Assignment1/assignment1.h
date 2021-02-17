#ifndef ASSIGNMENT1_H
#define ASSIGNMENT1_H

#include <cstring>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

struct keywords {
    int line_pos, keyword_pos;
};

struct all_lines {
    vector<string> vs;
} line;


static vector<all_lines> vectorLine;
static vector<keywords> vectorKeyword;

bool sortCompare(const keywords &a, const keywords &b);

#endif