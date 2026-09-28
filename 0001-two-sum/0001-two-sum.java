class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = nums.length;
        Map<Integer,Integer> visited = new HashMap<>();
        for (int i=0; i<l ; i++ ){
            if (visited.containsKey(target-nums[i])){
                return new int[]{(visited.get(target-nums[i])),i};
            }
            visited.put(nums[i],i);
        }
        return new int[2];
    }
}