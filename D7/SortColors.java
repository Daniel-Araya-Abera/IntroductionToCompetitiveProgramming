package Week2.Day5;

public class SortColorsLeetCode {

    public void sortColors(int[] nums) {
        int[] result = new int[nums.length];
        int minn = nums[0];
        int maxx = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < minn){
                minn = nums[i];
            }
            if (nums[i] > maxx){
                maxx = nums[i];
            }
        }
        int[] count = new int[maxx + 1];

        for (int i = 0; i < nums.length; i++) {
            count[ nums[i] ] += 1;
        }

//        System.out.println("printing");
//        for (int i = 0; i < count.length; i++) {
//            System.out.print(count[i]);
//        }
        int currentIndex = 0;
        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0){
                result[currentIndex] = i;
                currentIndex++;
                count[i]--;
            }
        }
//        System.out.println("printing");
        for (int i = 0; i < result.length; i++) {
//            System.out.print(result[i]);
            nums[i] = result[i];
        }


    }

    public static void main(String[] args) {

    }

}
