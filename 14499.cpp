#include <iostream>
using namespace std;

typedef enum { EAST=1, WEST, NORTH, SOUTH } DIR;

int map[20][20];
int numRow, numCol;

class Dice {
public:
    int row, col;
    int top = 0, bottom = 0, right = 0, left = 0, front = 0, rear = 0;
    int temp;
    Dice(int row, int col): row(row), col(col) {};
    
    int move(int d) {
        switch(d) {
        case EAST:
            if (numCol <= col + 1) return -1;
            temp = top;
            top = left;
            left = bottom;
            bottom = right;
            right = temp;
            col++;
            break;
        case WEST:
            if (col - 1 < 0) return -1;
            temp = top;
            top = right;
            right = bottom;
            bottom = left;
            left = temp;
            col--;
            break;
        case SOUTH:
            if (numRow <= row + 1) return -1;
            temp = top;
            top = front;
            front = bottom;
            bottom = rear;
            rear = temp;
            row++;
            break;
        case NORTH:
            if (row - 1 < 0) return -1;
            temp = top;
            top = rear;
            rear = bottom;
            bottom = front;
            front = temp;
            row--;
            break;
        }
        if (map[row][col] == 0) {
            map[row][col] = bottom;
        }
        else {
            bottom = map[row][col];
            map[row][col] = 0;
        }
        return top;
    }
};

int main() {
    int row, col;
    int numInstructions;
    int direction;
    int res;
    
    cin >> numRow >> numCol >> row >> col;
    cin >> numInstructions;
    
    Dice dice(row, col);
    
    for (int i = 0; i < numRow; i++) {
        for (int j = 0; j < numCol; j++) {
            cin >> map[i][j];
        }
    }
    
    for (int i = 0; i < numInstructions; i++) {
        cin >> direction;
        res = dice.move(direction);
        if(res != -1) cout << res << '\n';
    }
}