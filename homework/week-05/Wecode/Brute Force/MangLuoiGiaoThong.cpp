#include <iostream>
#include <vector>
#include <queue> // Thêm thư viện queue

using namespace std;

const int MAXN = 100005;
int n, m;
vector<int> adj[MAXN];
bool visited[MAXN];

// Dem so cap dinh khong lien thong trong do thi
int BFS(int s) {
    visited[s] = true;
    queue<int> Q; Q.push(s);
    int num = 0;

    while (!Q.empty()) {
        int u = Q.front(); Q.pop();
        ++num;

        for(int v: adj[u])
        if (!visited[v]) {
            visited[v] = true;
            Q.push(v);
        }
    }

    return num;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(NULL);

    cin >> n >> m;
    for(int i = 1; i <= m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    long long ans = 0;
    for(int s = 1; s <= n; ++s)
    if (!visited[s]) {
        int cnt = BFS(s);
        ans += 1LL  * cnt * (n - cnt) ;
    }

    cout << ans / 2;

    return 0;
}
