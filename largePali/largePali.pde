//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

//Find the largest palindrome made from the product of two 3-digit numbers.

public void setup() {
  println(999*999);
  println( largerPali() );
}

public int largerPali() {
  int biggest = 0;
  for ( int o = 999; o > 0; o-- )
    for ( int i = 999; i > 0; i-- )
      if (isPalindrome(Integer.toString(o*i)))
        if ( o*i > biggest )
          biggest = o*i;
  return biggest;
}
public boolean isPalindrome(String sWord){
  if ( reverse(sWord).equals(sWord) ) 
    return true;
  return false;
}

public String reverse(String sWord){
  String ans = "";
  for ( int i = sWord.length(); i > 0; i-- ) {
    ans += sWord.substring(i-1, i);
  }
  return ans;
}
