#include<iostream>
#include<string>
using namespace std;
class CountDig
{
public:
    static int nbDig(int n, int d){
    string temp;int count=0;
    
    for (int i = 0; i <=n; i++) {
    
    temp+=to_string(i*i)+",";
    }
for (int i = 0; i < temp.size(); i++) {
    /* code */
    if(temp[i]==d+'0')
    count++;
}
return count;
    
}
};