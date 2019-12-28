package com.company;

public class ReverseNum {
    public static int reverseNum(int givenNum){
        int result = 0;
        while(givenNum > 0){
            int remainder = givenNum % 10;
            givenNum = givenNum / 10;
            result = result * 10 + remainder;
        }
        return result;
    }

    public static void main(String[] args) {
        int num = 13425;
        int reversed = reverseNum(num);
        System.out.println("Num is " + num);

        System.out.println("Num reversed is " + reversed);

    }
}
