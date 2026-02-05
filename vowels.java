public class vowels {
    public static void main(String[] args) {

        String s = "education";
        int count = 0;

        for (char ch : s.toCharArray()) {
            if (ch == 'a' || ch == 'e' || ch == 'i'
                    || ch == 'o' || ch == 'u') {
                count++;
            }
        }

        System.out.println(count);
    }
}
