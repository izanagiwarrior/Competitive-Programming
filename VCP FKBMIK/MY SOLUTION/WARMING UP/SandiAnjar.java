import java.util.*;
import java.lang.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // TODO code application logic here
        Scanner s = new Scanner(System.in);
        
        String str = s.nextLine();
        String[] splited = str.split(" ");
        String[] hasil = new String[splited.length];
        int sandi = s.nextInt();
        
        Character[] smallChar = new Character[26];
        Character[] bigChar = new Character[26];
        int i = 0;
        
        
        
        for(Character c = 'a'; c <= 'z'; c++) {
            smallChar[i] = c;
            i++;
        }
        
        i = 0;
        
        for(Character c = 'A'; c <= 'Z'; c++) {
            bigChar[i] = c;
            i++;
        }
        
        Boolean cekKata = true;
        Boolean ketemu = false;
        
        for(i = 0; i < splited.length; i++) {
            char[] charKata = splited[i].toCharArray();
            char[] geserKata = new char[charKata.length];
            for(int j = 0; j < charKata.length; j++) {
                Character ch = charKata[j];
                
                if ( (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {  
                    int idx = 0;
                    while(!ketemu) {                  
                        
                        if (ch.equals(smallChar[idx])) {
                            ketemu = true;
                            if (idx + sandi > (smallChar.length - 1)) {
                                int idxGeser = idx + sandi - smallChar.length;
                                geserKata[j] = smallChar[idxGeser];
                            } else if (idx + sandi < 0){
                                geserKata[j] = smallChar[smallChar.length + (idx + sandi)];
                            } else {
                                geserKata[j] = smallChar[idx + sandi];
                            }
                            
                        } else if (ch.equals(bigChar[idx])) {
                           
                            ketemu = true;
                            if (idx + sandi > (bigChar.length - 1)) {
                                int idxGeser = idx + sandi - bigChar.length ;
                                geserKata[j] = bigChar[idxGeser];
                            } else if (idx + sandi < 0){
                                geserKata[j] = bigChar[bigChar.length + (idx + sandi)];
                            } else {
                                geserKata[j] = bigChar[idx + sandi];
                            }
                        }
                        idx++;
                    }
                } else {
                    geserKata[j] = ch;
                }
                ketemu = false;
            }
            hasil[i] = String.valueOf(geserKata);
        }
        
        int idxHasilKurangSatu = hasil.length - 1;
        for(i = 0; i < idxHasilKurangSatu; i++) {
            System.out.print(hasil[i] + " ");
        }
        System.out.println(hasil[hasil.length - 1]);
    }
}