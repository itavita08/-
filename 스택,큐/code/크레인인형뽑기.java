import java.util.Stack;

public class 크레인인형뽑기 {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int count = 0;
        for(int move : moves){
            for(int i = 0; i<board.length; i++){
                if(board[i][move-1] != 0){
                    if(!stack.isEmpty() && board[i][move-1] == stack.peek() ){
                        stack.pop();
                        count += 2;
                    }else{
                        stack.push(board[i][move-1]);
                    }
                    board[i][move-1] = 0;
                    break;
                }
            }
        }
        return count;
    }
}
