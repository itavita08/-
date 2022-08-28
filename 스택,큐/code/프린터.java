
import java.util.Collections;
import java.util.PriorityQueue;

public class 프린터 {
    static int [] priorities = {2,1,3,2};
    static int location = 2;

    public static int solution(int[] priorities, int location){
        int answer = 0;
        PriorityQueue<Integer> que = new PriorityQueue<>(Collections.reverseOrder()); // 높은숫자가 우선순위인 우선순위 큐
        for (int i : priorities) {
            que.add(i);
        }

        while(!que.isEmpty()){
            for(int i = 0; i < priorities.length; i++){
                if(priorities[i] == que.peek()){  // index값 확인 후 위치까지 같으면 answer 출력
                    if(i == location){
                        answer++;
                        return answer;
                    }
                    que.poll();  // 위치값이 다르면 찾는 인쇄물이 아니므로 que에서 삭제 
                    answer++;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args){
        System.out.println(solution(priorities, location));
    }

}
