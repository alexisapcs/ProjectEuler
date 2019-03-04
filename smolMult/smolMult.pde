public void setup() {
  int x = 2520;
  while (!divs(x)) 
      x+=20;
  println("Answer: " + x);
}

public boolean divs(int num) {
  for ( int i = 1; i <= 20; i++ )
    if ( num%i != 0 ) return false;
  return true;
}
