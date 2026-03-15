class Solution {
    public void moveZeroes(int[] nums) {
        int Zero = 0;
        for (int i = 0; i < nums.length ; i++){
            if (nums[i] != 0){
                int temp = nums[Zero];
                nums[Zero] = nums[i];
                nums[i] = temp;

                Zero ++;
            }
        }
    }
}