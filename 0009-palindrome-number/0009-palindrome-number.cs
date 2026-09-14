public class Solution {
    public bool IsPalindrome(int x) {

        if (x > 0){
            
            bool pal = true;
            string xStr = $"{x}";
            int tLen = xStr.Length;

            for (int i = 0; i < tLen; i++){
                char f = xStr[i];
                char l = xStr[tLen - i - 1];

                if (f != l){
                    pal = false;
                    break;
                }
            }
            return pal;

        }else if (x < 0 ){
            return false;
        }
        return true;
        
    }
}