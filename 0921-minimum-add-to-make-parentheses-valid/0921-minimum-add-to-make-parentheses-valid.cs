public class Solution {
    public int MinAddToMakeValid(string s) {

        List<int> temp = new List<int> {};

        for (int i = 0; i < s.Length; i++){
            if ("(".Contains(s[i]) ){
                temp.Add(-1);
            }else{
                bool found = false;
                for (int t = temp.Count - 1; t >= 0; t--){
                    if (temp[t] == -1){
                        temp[t] = 0;
                        found = true;
                        break;
                    }
                }
                if (!found){
                    temp.Add(1);
                }
            }
        }

        return Array.FindAll(temp.ToArray(), x => x != 0).Length;

        
    }
}