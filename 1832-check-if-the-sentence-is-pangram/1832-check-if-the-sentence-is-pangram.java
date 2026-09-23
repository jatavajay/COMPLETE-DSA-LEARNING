class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] seen = new boolean [26];
        for (char c : sentence.toCharArray()){
            seen[c-'a'] = true;
            // seen[ord(c) - ord('a')] = True , in python
        }
        for (boolean b : seen){
            if (!b){
                return false;
            }
        }
        return true;
    }
}