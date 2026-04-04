class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int x =0; x<nums.length-1; x++){
            for(int y = nums.length-1; y>0; y--){
                if (nums[x] == nums[y]){
                    if(x==y){
                        continue;
                    }
                    return true;
                }
            }
        }
        return false;
    }
}