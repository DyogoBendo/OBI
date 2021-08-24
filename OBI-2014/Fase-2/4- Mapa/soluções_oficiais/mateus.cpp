#include <bits/stdc++.h>

using namespace std;

const int tmax = (int)1e5 + 100;

int parent[tmax], rank[tmax], weight[tmax];

int find(int node) {
  
  if (node == parent[node]) return node;
  return parent[node] = find(parent[node]);
}

void merge(int nodeA, int nodeB) {
  
  nodeA = find(nodeA);
  nodeB = find(nodeB);
  if (rank[nodeA] < rank[nodeB]) {
    weight[nodeB] += weight[nodeA];
    parent[nodeA] = nodeB;
  } else {
    weight[nodeA] += weight[nodeB];
    parent[nodeB] = nodeA;
    rank[nodeB]++;
  }
}

int main() {

  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    parent[i] = i;
    rank[i] = weight[i] = 1;
  }
  for (int i = 0; i < n - 1; i++) {
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    if (c == 0) 
      merge(a - 1,b - 1);
  }
  
  long long answer = 0LL;
  for (int i = 0; i < n; i++) {
    if (parent[i] != i) continue;
    answer += (n - weight[i]) * weight[i];
  }

  printf("%lld\n", answer / 2LL);
  return 0;
}
