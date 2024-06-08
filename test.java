public class test {
    
    public static void main(String[]args){
        int[] nums = {1,1,1,2,2,3}; // Input array
        int[] expectedNums = {1,1,2,2,3}; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
    }
    
    
    public static int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
             if (i < 2 || n > nums[i - 2]){
                System.out.println(i + " " + n);
                nums[i++] = n;
             }
                
                
         return i;
    }
}
