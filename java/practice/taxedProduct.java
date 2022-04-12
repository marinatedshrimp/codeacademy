import java.util.Scanner;
//allows user input

public class taxedProduct{
  /*
  String product;
  double price;
  */

  public taxedProduct(/*String productType, double ogPrice*/){
    /*
    product = productType;
    price = ogPrice;
    */
  }
  //PARENT = CHILD;
  /*WHEN USING IN METHODS USE THE PARENT INSTANCE NAME NOT
  THE CONSTRUCTOR OBJECTS???*/

  public double priceWithTax(){

  }
/*IF U WANNA USE THE RESULT OUTSIDE THE METHOD REPLACE VOID WITH
THE TYPE OF VARIABLE U WANNA RETURN

ANYTHING WRITTEN AFTER RETURN WILL NOT BE READ*/

  public static void main(String[] args){
    Scanner myProduct = new Scanner(System.in);
    //create a scanner object
    System.out.println("Enter product name: ");
    //create a prompt to induce input
    String pName = myProduct.nextLine();

    Scanner myPrice = new Scanner(System.in);
    System.out.println("Enter product price: ");
    Double pPrice = myPrice.nextDouble();


    taxedProduct thing = new taxedProduct("coffee", 4.99);


  }
}

  /*coffee 4.99
  dvd 15.00*/
