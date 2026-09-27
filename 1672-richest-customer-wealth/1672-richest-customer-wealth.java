class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWlth = 0;
        for (int i=0 ; i<accounts.length; i++){
            int pi_wealth = 0;
            for(int j: accounts[i]){
                pi_wealth+=j;
            }
            maxWlth = Math.max(maxWlth,pi_wealth);
        }
        return maxWlth;
    }
}