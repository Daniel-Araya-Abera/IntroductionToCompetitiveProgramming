class Solution {
public:
    int smallestRepunitDivByK(int K) {
        int lastDigit = K % 10;
        if (lastDigit == 0 || lastDigit == 2 || lastDigit == 4 || 
            lastDigit == 5 || lastDigit == 6 || lastDigit == 8){
            return -1;
        }
        // int divisonResult = 
        int remainder = 1 % K;
        int countDigit = 1;
        
        
        while (remainder){
            int updatedNumber = (remainder * 10 + 1) ;
            remainder = updatedNumber % K;
            countDigit++;
            
        }
        
        return countDigit;
    }
};