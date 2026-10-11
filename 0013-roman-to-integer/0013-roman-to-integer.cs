public class Solution {
    public int RomanToInt(string s) {

        int value = 0;
        int past = -1;

        for (int i = 0; i < s.Length; i++){
            int current = 0;
            string num = s[i] + "";
            switch (num)
            {
                case "I":
                    current = 1;
                    break;   
                case "V":
                    current = 5;
                    break;
                case "X":
                    current = 10;
                    break;
                case "L":
                    current = 50;
                    break;
                case "C":
                    current = 100;
                    break;
                case "D":
                    current = 500;
                    break;
                case "M":
                    current = 1000;
                    break;

            }   

            if (past > -1 && past < current){
                value += current - (past * 2);
            }else{
                value += current;
            }
            past = current;
        }

        return value;
        
    }
}