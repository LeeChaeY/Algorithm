import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        HashMap<Character,Integer> map = new HashMap<>();
        for(int i=0; i<s.length();i++){
            char ch = s.charAt(i);
            answer[i] = i-map.getOrDefault(ch,i+1);
            map.put(ch,i);
        }
        return answer;
    }
}


class Solution {
    public int[] solution(String str) {
        int[] result = new int[str.length()];

        for(int i=0;i<str.length();i++){

            String subStr = str.substring(0,i);
            if(subStr.indexOf(str.charAt(i))==-1) {
                result[i] = -1;
            }else {
                result[i] = i-subStr.lastIndexOf(str.charAt(i));
            }
        }
        return result;
    }
}
