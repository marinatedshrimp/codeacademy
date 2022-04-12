import java.util.ArrayList;

class PrimeDirective {
  
  // Add your methods here:
  public boolean isPrime(int[] number)
  {
    for(int i = 2; i<number; i++)
    {
      if(number % i == 0)
      {
        return false;
      }
      if(number == 2)
      {
        return true;
      }else if(number < 2)
      {
        return false;
      }
    }
  }
    public Arraylist<Integer> onlyPrimes(int[] numbers)
    {
      ArrayList<Integer> primes = new ArrayList<Integer>();
      for (String number : nuumbers)
      {
        if(isPrime(number))
        {
          primes.add(number)
        }
      }
    }
    return primes;
  }
  
  public static void main(String[] args) {

    PrimeDirective pd = new PrimeDirective();
    int[] pd = {6, 29, 28, 33, 11, 100, 101, 43, 89};
    System.out.println(pd.isPrime[4]);
  }  

}