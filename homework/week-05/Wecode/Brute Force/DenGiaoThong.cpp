#include <iostream>
#include <cmath>

using namespace std;

void convert(string &s)
{
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='D') s[i]='0';
        else if(s[i]=='X') s[i]='1';
        else s[i]='2';
    }
}

int main()
{
    string state;
    int t[9];
    string signal[9];

    for(int i=0;i<9;i++)
    {
        cin>>t[i];
        cin>>signal[i];
    }

    cin>>state;

    convert(state);

    int t_min = 1000000000;
    for(int i=0; i<pow(3,9); i++)
    {
        string tmp = state;
        int time = 0;
        int k = i;
        for(int j=0, d=1;j<9;j++,d*=3)
        {
            int m = k % 3;
            k /= 3;
            time += t[j] * m;
            for(char c:signal[j])
            {
                int id = c - '0' - 1;
                tmp[id] = (tmp[id] -'0' + m) % 3 + '0';
            }
        }
        if(tmp == "111111111") 
        {
            t_min = min(t_min, time);
        }
    }
    if(t_min == 1000000000) cout<<"-1";
    else cout<<t_min;
    return 0;
}