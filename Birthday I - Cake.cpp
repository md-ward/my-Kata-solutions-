#include <iostream>
#include<vector>

using namespace std;

std::string cake(int x, std::string y)
{
  y.insert(0," ");
  int sum=0;
  for (int i = 1; i <= y.size(); i++) {
if(i%2!=0)
sum+=int(y[i]);
sum+=i;
  }
  int total=x*70/100;
  if(sum>total)
  return "Fire!";
  else return "That was close!";
}