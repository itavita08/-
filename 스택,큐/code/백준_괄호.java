import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 백준_괄호{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        for(int i=0; i<n; i++){
            Stack<Character> stack = new Stack<>();
            String s = bf.readLine();
            for(int j=0; j<s.length(); j++){
                if(s.charAt(j) == '('){
                    stack.push('(');
                } else{
                    if(stack.isEmpty()){
                        stack.push(')');
                        break;
                    } else{
                        stack.pop();
                    }
                }
            }
            if(!stack.isEmpty()){
                System.out.print("NO\n");
            }else{
                System.out.print("YES\n");
            }
        }
    }
}