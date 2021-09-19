#include <vector>
#include <queue> 

using namespace std;

struct {
    int r;
    int c;
} drdc[4] = { {0, 1}, {0, -1}, {1, 0}, {-1 ,0}};

int max_area = 0;
bool visited[100][100] = { 0 };

int bfs(int row, int col, int num_row, int num_col) {
    queue<pair<int, int>> q;
    int next_row, next_col;
    int area = 1;
    
    q.push({row, col});
    
    while (!q.empty()) {
        auto point = q.front();
        q.pop();
        
        for (auto p: drdc) {
            next_row = point.first + p.r;
            next_col = point.second + p.c;
            
            if (!visited[next_row][next_col]) {
                visited[next_row][next_col] = true;
                q.push({next_row, next_col});
                area += 1;
            }
        }
    }
    
    return area;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int area = 0;
    for(int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                max_area = max(max_area, bfs(i, j, m, n));
                
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int main() {
    cout << solution()
}