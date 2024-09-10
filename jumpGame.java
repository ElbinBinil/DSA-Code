class Solution {
    public int jump(int[] nums) {
         int l = 0, r = 0;
        int res = 0;
        while (r < nums.length - 1) {
            int maxJump = 0;
            for (int i = l; i <= r; i++) {
                maxJump = Math.max(maxJump, i + nums[i]);
            }
            l = r + 1;
            r = maxJump;
            res++;
        }
        return res;     
    }
}