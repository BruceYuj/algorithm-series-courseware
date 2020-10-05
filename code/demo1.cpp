#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
 
const int N = 300010;
 
int n, m;
int p[N], minV[N], maxV[N], cnt[N];

void io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int get(int a) {
    if(p[a] != a) {
        p[a] = get(p[a]);
    }
    return p[a];
}

int getMin(int a) {
    return minV[get(a)];
}
int getMax(int a) {
    return maxV[get(a)];
}
int getCnt(int a) {
    return cnt[get(a)];
}

void unionS(int a, int b) {
    a = get(a);
    b = get(b);
    if(a == b) return;

    p[a] = b;
    minV[b] = min(minV[a], minV[b]);
    maxV[b] = max(maxV[a], maxV[b]);
    cnt[b] += cnt[a];   
}
int main() {
    io();
    cin>>n>>m;
    
    for(int i = 1; i <= n; i++) {
        p[i] = i;
        minV[i] = i;
        maxV[i] = i;
        cnt[i] = 1;
    }

    string op;
    int u, v;
    
    while(m--) {
        cin>>op;
        if(op == "get") {
            cin>>v;
            cout<<getMin(v)<<" "<<getMax(v)<<" "<<getCnt(v)<<endl;
        } else {
            cin>>u>>v;
            unionS(u, v);
        }
    }

    return 0;
} 