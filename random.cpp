// C++で開発しましょう。

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <random>

using namespace std;

int main(){
    srand(time(0));

    int randomInt=rand()%11;

    vector<int> intArr={0,1,2,3,4,5,6,7,8,9,10};

    for(auto i=0;i<intArr.size();++i){
        int j=i+rand()/((RAND_MAX / (intArr.size()-i))+1);

        int temp=intArr[i];
        intArr[i]=intArr[j];
        intArr[j]=temp;
    }

    for(auto num: intArr){
        cout << num << endl;
    }

}
/*乱数の作り方*/
/*Fisher Yatesアルゴリズムを使用*/