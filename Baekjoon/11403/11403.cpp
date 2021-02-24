#include <iostream>
using namespace std;

int n; // 정점의 개수
int map[100][100];
bool visited[100][100]; // 방문 기록

void dfs(int start,int x, int y){ // start는 시작한 줄, x번째 줄의 y번째 숫자
	map[start][y] = 1;
	visited[start][y] = true;

	for(int j = 0; j < n; j++){
		if(map[y][j]==1 && !visited[start][j]) // y번째 줄에서 j번째 숫자가 1인 경우 찾아 탐색
			dfs(start,y,j);
	}
}

int main(){
	cin>> n;

	for(int i = 0; i < n; i++){ // 초기화
		for(int j = 0; j < n; j++){
			visited[i][j] = false;
			cin>> map[i][j];
		}
	}

	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(map[i][j]&&!visited[i][j])
				dfs(i,i,j);

	for(int i = 0; i < n; i++){ // 출력
		for(int j = 0; j < n; j++)
			cout<< visited[i][j] << " ";
		cout<< endl;
	}
}


