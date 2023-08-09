import java.util.*;

class Main {
    public static boolean pan(String str){
        Set<Character>set=new HashSet<>();
        for(char ch: str.toCharArray())
        {
            if(ch>='a'&& ch<='z')
               set.add(ch);
            if(ch>='A'&&ch<='Z')
            {
            ch=Character.toLowerCase(ch);
            set.add(ch);
            }
        }
        return set.size()==26;
    }
    public static void main(String[] args)
    {
        String str="The quick brown fox jumps over the lazy dog";
        if(pan(str))
        System.out.println(str+"\nis pangram");
        else
        System.out.println(str+"\nnot pangram");
    }
}
