class Solution {
    public int strStr(String haystack, String needle) {
        
        if (needle.isEmpty()) {
            return 0;
        }

       
        if (haystack.length() < needle.length()) {
            return -1;
        }

        int i = 0; 
        int j = 0; 


        while (i <= haystack.length() - needle.length()) {
           
            while (j < needle.length() && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }

            
            if (j == needle.length()) {
                return i;
            }

            
            i++;
            j = 0;
        }

      
        return -1;
    }
}
