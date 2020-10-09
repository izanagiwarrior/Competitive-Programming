import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt(), b = in.nextInt();
        long total = 0;
        for(int i = a;i<=b;i++){
        total += i;
        }
        System.out.println(total%1000000007);
    }
}