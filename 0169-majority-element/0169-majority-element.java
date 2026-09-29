class Solution {
    public int majorityElement(int[] nums) {
       Map<Integer,Integer> counter = new HashMap<>();
       for (int d: nums){
        counter.put(d,0);
       } 
       for(int d: nums){
            counter.put(d, counter.get(d) + 1);;
       }
       int maxcnt = 0;
       int num=nums[0];
       for (int k:counter.keySet()){
        if(counter.get(k)>maxcnt){
            maxcnt = Math.max(maxcnt,counter.get(k));
            num = k;
        }
       }
       return num;
    }
}