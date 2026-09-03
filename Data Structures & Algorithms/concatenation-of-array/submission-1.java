class Solution {
    public int[] getConcatenation(int[] nums) {
        int n=nums.length;
        int [] output= new int[n*2];
        for (int i=0; i<2; i++)
        {
            for (int j=0;j<n; j++)
            {
                output[i*n+j]=nums[j];
            }
        }
        return output;
    }
}