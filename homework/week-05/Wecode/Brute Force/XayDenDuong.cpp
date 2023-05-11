#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

bool check(int r, int a[1000], int n, int m)
{ 
    int d = 0;
    int j = 0;
    for(int i = 0; i < m; i++)
    {
        d = a[j] + 2*r;
        while(j<n && a[j] <= d)
            j++;
    }

    if(j >= n)
        return true;

    return false;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(NULL);
    int n, m;
    int a[1000];

    cin>>n>>m;

    for(int i=0; i<n; i++)
        cin>>a[i];

    sort(a, a+n);

    for(int i = 1; i < 5000; i++) if(check(i, a, n, m)) 
    {
        cout<<i;
        break;
    }

    return 0;
}