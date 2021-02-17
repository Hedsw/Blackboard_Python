
/* 
First Implementation 
The first implementation
• reads the all lines from the keyboard,
• stores all the lines in the core with each word stored as a sequence of characters,
• circularly shifts all the lines and stores them,
• alphabetizes the circularly shifted lines, and then
• displays the results on the screen.
*/

#include "assignment1.h"

int main()
{
    cout << " Please type lines again, If you are done, type CTRL + D " << endl;
    string inputKeyword;
    //compare sorter;

    while (cin >> inputKeyword)
    {
        line.vs.push_back(inputKeyword); // Add all keyword into L struct line by line
        if (getchar() == '\n')
        {
            vectorLine.push_back(line); // In Empty space, input all lines into vectorLine
            //cout << "Next lines will be sorted separately with previous contents " << endl;

            line.vs.clear();  // When Enterkey is twiced ,Clear all of information in L.vs
        }
    }
    
    for (int i = 0; i < vectorLine.size(); i++) // Without line change, count how many contents in vectorLine 
    {
        for (int j = 0; j < vectorLine[i].vs.size(); j++) // How many keywords in the line 
        {
            keywords mywords = {i,j}; // i lines j keywords 
            // cout << mywords.line_pos << " and " << mywords.keyword_pos << " Wow " << endl; 
            vectorKeyword.push_back(mywords); // add the keyword into ..
        }
    }

    // cout << vw.size() << " <-- size check " << endl;
    sort(vectorKeyword.begin(), vectorKeyword.end(), sortCompare);
    
    cout << '\n' << "Sorted all_liness below " << '\n' << endl; 

  
    for (int i = 0; i < vectorKeyword.size(); i++) // How many lines ..
    {
        int line_pos = vectorKeyword[i].line_pos;
        int keyword_pos = vectorKeyword[i].keyword_pos;
        int vs_sz = (int)vectorLine[line_pos].vs.size();
        int count = 0; 
        
        // cout << vs_sz << " <-- size check " << endl;
        
        for (int j = keyword_pos; j < vs_sz; j++) // How many keyword in the line 
        {
            count++;
            cout << vectorLine[line_pos].vs[j] ;
            if(count == vs_sz) 
            {
                cout << "" << endl;
            }
            else 
            {
                cout << " " ;
            }
        }

        for (int j = 0; j < keyword_pos; j++)
        {
            count++;
            cout << vectorLine[line_pos].vs[j];

            if(count == vs_sz) 
            {
                cout << "" << endl;
            }
            else 
            {
                cout << " ";
            }

        }
    }
    return 0;
}

// This function is to use at third parameter at sort in main function 
// sort(first, second , sortcompare function) 
// We are going to sort using this parameter

bool sortCompare(const keywords &a, const keywords &b)  {
    all_lines First, Second;
    int length = 0;

    for (int i = a.keyword_pos; i < vectorLine[a.line_pos].vs.size(); i++)
    {
        First.vs.push_back(vectorLine[a.line_pos].vs[i]);
        //cout << vectorLine[a.line_pos].vs[i] << " What is it? " << endl;
    }
    for (int i = 0; i < a.keyword_pos; i++)
    {
        First.vs.push_back(vectorLine[a.line_pos].vs[i]);
        //cout << vectorLine[a.line_pos].vs[i] << " number two " << endl;
    }

    for (int i = b.keyword_pos; i < vectorLine[b.line_pos].vs.size(); i++)
    {
        Second.vs.push_back(vectorLine[b.line_pos].vs[i]);
    }
    for (int i = 0; i < b.keyword_pos; i++)
    {
        Second.vs.push_back(vectorLine[b.line_pos].vs[i]);
    }

    if((int)First.vs.size() < (int)Second.vs.size()) {
        length = (int)First.vs.size();
        // cout << length << " First Value ? " << endl;
    }
    else {
        length = (int)Second.vs.size();
        // cout << length << " Second ? " << endl;
    }

    // Switch Postions again and again.. 
    for (int i = 0; i < length; i++)
    {
        if (First.vs[i] != Second.vs[i])
        {
            return First.vs[i] < Second.vs[i];
        }
    }

    return First.vs.size() < Second.vs.size();
}
