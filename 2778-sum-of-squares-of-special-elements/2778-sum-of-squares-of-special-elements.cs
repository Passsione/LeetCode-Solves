public class Solution {
    public int SumOfSquares(int[] nums) {

        int sum = 0;

        for (int i = 0; i < nums.Length; i++){
            int ind = i + 1;
            if (nums.Length % ind == 0){

                sum += nums[i] * nums[i];
            }
        }

        return sum;
        
    }
}