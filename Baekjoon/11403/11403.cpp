#include <iostream>
using namespace std;

int n; // ������ ����
int map[100][100];
bool visited[100][100]; // �湮 ���

void dfs(int start,int x, int y){ // start�� ������ ��, x��° ���� y��° ����
	map[start][y] = 1;
	visited[start][y] = true;

	for(int j = 0; j < n; j++){
		if(map[y][j]==1 && !visited[start][j]) // y��° �ٿ��� j��° ���ڰ� 1�� ��� ã�� Ž��
			dfs(start,y,j);
	}
}

int main(){
	cin>> n;

	for(int i = 0; i < n; i++){ // �ʱ�ȭ
		for(int j = 0; j < n; j++){
			visited[i][j] = false;
			cin>> map[i][j];
		}
	}

	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(map[i][j]&&!visited[i][j])
				dfs(i,i,j);

	for(int i = 0; i < n; i++){ // ���
		for(int j = 0; j < n; j++)
			cout<< visited[i][j] << " ";
		cout<< endl;
	}
}


