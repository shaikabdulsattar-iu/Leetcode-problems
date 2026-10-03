class Solution {
public:
    bool isValid(int i , int j, char c , vector<vector<char>>& board){

        //check the row
       
        for(int k = 0 ; k < 9 ; k++){
            if(board[i][k]==c)return false;
        }

        //check the col
        for(int k = 0 ; k < 9 ; k++){
            if(board[k][j] == c) return false;
        }

        //check 3X3
        int startx = (i / 3) * 3;
        int starty = (j / 3) * 3;
        for(int k = startx ; k < startx+3 ; k++){
            for(int x = starty ; x < starty + 3 ; x++){
                if(board[k][x] == c)return false;
            }
        }
        return true;
    }
    bool Solve(vector<vector<char>>& board){

        for(int i = 0 ; i < 9 ; i++){
            for(int j = 0 ; j < 9 ; j++){
                if(board[i][j] == '.'){
                    for(char c = '1' ; c <= '9' ; c++){
                        if(isValid(i,j,c,board)){
                            board[i][j] = c;
                            if(Solve(board)) return true;

                            board[i][j] = '.';
                        }
                        
                    }
                    return false;
                }
            }
        }
        return true;
    }
    void solveSudoku(vector<vector<char>>& board) {

        Solve(board);

        

        
    }
};