public class Solution {
    public string LongestCommonPrefix(string[] strs) {

        string first_str = strs[0];

        if (strs.Length == 1) return first_str;
        
        string common = "";
        for (int s = 0; s < first_str.Length; s++){
            char sub = first_str[s];
            bool passed = true;

            for (int j = 1; j < strs.Length; j++){
                string current = strs[j];

                int prefix = current.Length > s && current[s] == sub ? s : -1 ;

                if (prefix < 0 || prefix > s){
                    passed = false;                    
                    break;
                }                                                
            }
            if (passed){
                common += sub;
            }else{
                break;
            }
        }     

        return common;      

    }
}