class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        String[] words = s.split("\\s+");
        if(words.length == 0){
            return 0;
        }
        return words[words.length - 1].length();
    }
}