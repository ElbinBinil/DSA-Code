class Solution {
    public boolean isPalindrome(String s) {
        String nStr = "";
        char ch;
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        for(int i=0; i<s.length(); i++){
            ch = s.charAt(i);
            nStr = ch+nStr;
        }
        if(s.equals(nStr)){
            return true;
        }else{
            return false;
        }
    }
}