/*
Rating: ~ 2.6 / 10
Link: https://open.kattis.com/problems/busnumbers
Complexity: O(N) where N is the length of the string
*/

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String args[]) {
        // read & store input
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner.close();
        // convert input to lowercase
        input = input.toLowerCase();

        // declare hashmap
        HashMap<Character, String> alphabetMap = new HashMap<Character, String>();
        alphabetMap.put('a', "@");
        alphabetMap.put('b', "8");
        alphabetMap.put('c', "(");
        alphabetMap.put('d', "|)");
        alphabetMap.put('e', "3");
        alphabetMap.put('f', "#");
        alphabetMap.put('g', "6");
        alphabetMap.put('h', "[-]");
        alphabetMap.put('i', "|");
        alphabetMap.put('j', "_|");
        alphabetMap.put('k', "|<");
        alphabetMap.put('l', "1");
        alphabetMap.put('m', "[]\\/[]");
        alphabetMap.put('n', "[]\\[]");
        alphabetMap.put('o', "0");
        alphabetMap.put('p', "|D");
        alphabetMap.put('q', "(,)");
        alphabetMap.put('r', "|Z");
        alphabetMap.put('s', "$");
        alphabetMap.put('t', "']['");
        alphabetMap.put('u', "|_|");
        alphabetMap.put('v', "\\/");
        alphabetMap.put('w', "\\/\\/");
        alphabetMap.put('x', "}{");
        alphabetMap.put('y', "`/");
        alphabetMap.put('z', "2");

        // convert to new alphabet
        for (int i = 0; i < input.length(); i++) {
            Character inputCharacter = input.charAt(i);
            if (alphabetMap.containsKey(inputCharacter)) {
                System.out.print(alphabetMap.get(inputCharacter));
            } else {
                System.out.print(inputCharacter);
            }
        }
    }
}
