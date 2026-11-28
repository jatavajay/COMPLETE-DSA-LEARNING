import java.util.*;
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> st = new ArrayDeque<>();
        for(int ast: asteroids){
            boolean alive = true;
            while (!st.isEmpty() && st.peek()>0 && ast<0){
                if (st.peek()<-ast){
                    st.pop();
                }
                else if (st.peek() == -ast) {
                    st.pop();
                    alive = false;
                    break;
                }
                else {
                    alive = false;
                    break;
                }
            }
            if (alive) {
                st.push(ast);
            }
        }
        int[] ans = new int[st.size()];
        for (int i = ans.length - 1; i >= 0; i--) {
            ans[i] = st.pop();
        }
        return ans;
    }
}