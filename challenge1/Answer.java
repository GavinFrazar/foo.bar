public class Answer {
    public static void main(String[] args)
    {
      String s = "abcabc";
      System.out.println(answer(s));
    }
    public static int answer(String s) { 

        // Your code goes here.
        int ans = 1; //default answer
        int len = s.length();
        int limit = (int) Math.sqrt(len) + 1;
        for (int i = 1; i <= limit; i++)
        {
          if (len % i == 0)
          {
            int divisor = i;
            String substr = s.substring(0,divisor);
            int count = len/divisor;
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < count; j++)
            {
              sb.append(substr);
            }
            String comp_str = sb.toString();
            
            if (comp_str.equals(s))
            {
              ans = len/divisor;
              break;
            }
          }
        }
        return ans;
    }
}