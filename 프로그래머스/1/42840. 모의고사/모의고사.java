
import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int size = answers.length;
        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        for (int i=0; i<size; i++) {
            if (answers[i] == i%5+1) num1++;
            if (i%2 == 0) {
                if (answers[i] == 2) num2++;
            } else {
                if ((i%8 == 1 || i%8 == 3) && answers[i] == i%8) num2++;
                else if (i%8 == 5 && answers[i] == 4) num2++; 
                else if (i%8 == 7 && answers[i] == 5) num2++; 
            }
            switch(i%10) {
                    case 0: case 1:
                        if (answers[i] == 3) num3++;
                        break;
                    case 2: case 3:
                        if (answers[i] == 1) num3++;
                        break;
                    case 4: case 5:
                        if (answers[i] == 2) num3++;
                        break;
                    case 6: case 7:
                        if (answers[i] == 4) num3++;
                        break;
                    case 8: case 9:
                        if (answers[i] == 5) num3++;
                        break;
            }
        }
        
        System.out.println(num1+", "+num2+", "+num3);
        int max = Math.max(Math.max(num1,num2),num3);
        if (num1 == max) answer.add(1);
        if (num2 == max) answer.add(2);
        if (num3 == max) answer.add(3);
        return answer.stream().mapToInt(i->i).toArray();
    }
}