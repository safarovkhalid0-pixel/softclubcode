#include <iostream>
using namespace std;
int main() {
    int a;
    cin>>a;
    int a1 = a/100000%10;
    int a2 = a/10000%10;
    int a3 = a/1000%10;
    int a4 = a/100%10;
    int a5 = a/10%10;
    int a6 = a/1%10;

    cout<<"first number of ""<<a<<"<<a1<<endl;
    cout<<"second number of ""<<a<<"<<a2<<endl;
    cout<<"third number of ""<<a<<"<<a3<<endl;
    cout<<"fourth number of ""<<a<<"<<a4<<endl;
    cout<<"fifth number of ""<<a<<"<<a5<<endl;
    cout<<"six number of ""<<a<<"<<a6<<endl;
    cout<<"sum all number of ""<<a<<"<<a1+a2+a3+a4+a5+a6;

}
