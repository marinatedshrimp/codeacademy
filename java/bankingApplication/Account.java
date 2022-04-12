import java.util.Scanner;
//allows user input

public class Account
{
  int balance;
  int previousTransaction;
  String customerName;
  String customerID;

  //class constructor
  public Account(String name, String id){
    customerName = name;
    customerID = id;
  }

  //function to deposit
  void deposit(int amount)
  {
    if(amount != 0)
    {
      balance += amount;
      previousTransaction = amount;
    }
  }

  //func to withdraw
  public void withdraw(int amount)
  {
    if(amount != 0)
    {
      balance -= amount;
      previousTransaction = -amount;
    }
  }

  void printPreviousTransaction()
  {
    if(amount > 0)
    {
      System.out.println("Deposited: " + previousTransaction);
    }
    else if(amount < 0)
    {
      System.out.println("Withdrawn: " + Math.abs(previousTransaction));
    }
    else
    {
      System.out.println("No transaction performed");
    }
    //Math.abs() gives absolute value
  }

  void interest(int years)
  {
    double interestRate = 0.06 / 100;
    double balance = interestRate * balance * years + balance;
    System.out.println("Current interest rate is " + interestRate * 100 + "%");
    System.out.println("Balance after " + years + "years: " + balance);
  }

  void showMenu()
  {
    char option = 'A';
    Scanner scanner = new scanner(System.in);
    System.out.println("Your name is " + customerName);
    System.out.println("Your id is " + customerID);
    System.out.println();
    System.out.println("What would you like to do today?");
    System.out.println();
    System.out.println("A: Check your balance");
    System.out.println("B: Make a deposit");
    System.out.println("C: Make a withdrawal");
    System.out.println("D: Check previous transaction");
    System.out.println("E: Calculate interest");
    System.out.println("F: Exit");

    do {
      System.out.println();
      System.out.println("Enter an option: ");
      char optionDraft = scanner.next().charAt(0);
      //makes it so it only processes index 0 of unput
      option = Character.toUpperCase(optionDraft);
      System.out.println();

      switch(option)
      {
        case 'A':
        System.out.println("***");
        System.out.println("Balance: $" + balance);
        System.out.println("***");
        break;

      case 'B':
        System.out.println("Deposit value: ");
        int amount = scanner.nextInt();
        //saves next int to be inputted
        deposit(amount);
        System.out.println();
        break;

      case 'C':
        System.out.println("Withdrawal value: ");
        int amount2 = Math.abs(scanner.nextInt());
        //just in case they try to add a -
        withdraw(amount2);
        System.out.println();
        break;

      case 'D':
        System.out.println("***");
        previousTransaction();
        System.out.println("***");
        System.out.println();
        break;

      case 'E':
        System.out.println("Enter years of interest: ");
        double years = scanner.nextDouble();
        interest(years);
        System.out.println();
        break;

      case 'F':
        break;
      }

    } while (option != 'F');
    //do the above loop then break out when option = 'F'
    System.out.println("Thank you for flying with us:)");
  }
}
