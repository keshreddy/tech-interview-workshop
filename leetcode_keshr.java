class Solution {
    public int maxSubArray(int[] nums) 
    {
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++)
        {
            int currSum = 0;
            for (int j = i; j < nums.length; j++)
            {
                currSum += nums[j];
                maxSum = Math.Max
            }
        }
        return maxSum;
    }
}