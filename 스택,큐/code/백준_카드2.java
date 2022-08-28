import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.stream.IntStream;

public class 백준_카드2{
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        Queue<Integer> que = new ArrayDeque<>();
        IntStream.range(1, n+1).forEach(i -> que.add(i));

        while(que.size() > 1){
            que.poll();
            que.add(que.poll());
        }
        System.out.println(que.peek());
    }
}