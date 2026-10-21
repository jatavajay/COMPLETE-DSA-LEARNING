class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==0) return -1;
        int n=nums.length;
        int i =0;
        int j=n-1;
        int mid=-1;
        while(j>=i){
            mid=(i+(j-i)/2);
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]>target){
                j=mid-1;
            }
            else{
                i=mid+1;
            }
        }
        return -1;
    }
}
