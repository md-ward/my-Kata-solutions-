#include <vector>
#include<iostream>
using namespace std;
int findOdd(const std::vector<int> numbers){
  //your code here
  int n=numbers.capacity();
vector<int> count(n);
  for(int i=0;i<n;i++)
  {for (int j= 0; j < n; j++) {
     if(numbers.at(i)==numbers.at(j))
     count[i]=count[i]+1;
  }

}
  for (int i = 0; i < n; i++) {
      /* code */

      if(count[i]%2!=0)
      return numbers[i];
  }
  

  }