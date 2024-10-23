// 문제풀이 시간: 1st - 1시간 반 소요 후 실패, 2nd - 질문하기 힌트(https://school.programmers.co.kr/questions/20800 )보고 20분 소요 후 성공

import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int max_w = 0;
        int max_h = 0;
        
        for (int i=0; i<sizes.length; i++) {
            max_w = Math.max(max_w, Math.max(sizes[i][0], sizes[i][1]));
            max_h = Math.max(max_h, Math.min(sizes[i][0], sizes[i][1]));
        }
        return max_w * max_h;
    }
}
