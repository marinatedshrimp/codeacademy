import java.util.*;

public class jnotes{
  public jnotes(String it){
    this.it = it;
  };
};

String and = "&&";
String or = "||";

/*
If updates get rejected becuase the remote contains
work that you do not have locally.
*/

$ git pull
$ git fetch 
$ git merge   


//-----USER INPUT-----//
import java.util.Scanner; //import scanner class
Scanner myScan = new Scanner(System.in); //create scanner object
System.out.println("Enter a thing: ")
String scanWord = myScan.nextLine(); //read user input
//nextBoolean(), nextDouble(), nextFloat(), nextInt()
System.out.println("ur thing is: " + scanWord);

//----ARRAYLIST----//

System.out.println(Arrays.toString(specials));
//this makes the printed value a string instead of a memory address

ArrayList<String> toDoList = new ArrayList<String>();
ArrayList<Integer> numbers = new ArrayList<Integer>();
//not int becuase the values are not primitive types in ArrayLists

ArrayList assortment = new ArrayList<>();
assortment.add("Hello") // String
assortment.add(12) // Integer
assortment.add(ferrari) // reference to Car
// assortment holds ["Hello", 12, ferrari]
//if you dont specify you can hold diff types
System.out.println(assortment.size());
String arrayLength = ".length";
String arraylistLength = ".size()";

String arrayIndex = ".get(Index)";
String arraylistIndex = "arraylist[Index]";

//REWRITING ITEMS IN ARRAYS VS ARRAYLISTS//
String[] shoppingCartt = {"egg", "barnacle", "wine"};

shoppingCartt[0] = "Tweed Cape";

  //|||||||||||||||||||||||||||||||||||||||||||||

//exclusively string element ArrayList
ArrayList<String> shoppingCart = new ArrayList<String>();
shoppingCart.add("egg");
shoppingCart.add("barnacle");
shoppingCart.add("wine");
//switch index 0 with tweed Cape
shoppingCart.set(0, "Tweed Cape");

//arraylist with exclusively char elements
ArrayList<Char> grades = new ArrayList<Char>();
   grades.add('B');
   grades.add('B');
   grades.add('D');

//   |||||||||||||||||||||||||||||||||||||||||||||||

//random number generator

// create random object
        Random ran = new Random();
        // Print next int value
        // Returns number between 0-9
        int nxt = ran.nextInt(10);

//-----INTERPOLATION-----//
System.out.printf("%, d",1000000000) == " 1,000,000,000"
System.out.printf("%,d",1000000000) == "1,000,000,000"
System.out.printf("%d",1000000000) == "1000000000"
// the "," separates it by the thousands

String d = "formats decimal integers";
String f = "formats float numbers";
String s_or_S = "lowercase_or_uppercase strings";
String b_or_B = "lowercase_or_uppercase booleans";
//prefix the letter with a %

System.out.printf("the%nmore%nthe%nmerrier");
/*
the
more
the
merrier
*/

Arraylist secretCode = new Arraylist 
[1,3,4,3,6,4,8,5,3]
for (int i = 0; i < secretCode.length; i++) {
  // Increase value of element value by 1
  secretCode[i] += 1;
}

for(i = 0; i < secreCode.length; i += 1){
  secretCode[i] += 1;
}


Arraylist<Double> expenses = new Arraylist<Double>();
expenses.add(21.44);
expenses.add(89.89);
expenses.add(62.74);
expenses.add(12.99);

double mostExpensive = 0;

//FOR-EACH LOOPING
for(double expense : expenses){
  if(expense > mostExpensive){
    mostExpensive = expense;
  }
}
System.out.println(mostExpensive);
//traverses through expenses and analyzes each item
//Output: 89.89
//requires a DATATYPE


//removing an item mid-traverse
//will move index of elements after the removed -1

/**
removing in a while loop:
do not increment the counter when removing item
**/
ArrayList<Integer> numlst = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5,6,7,8,9,10));

i = 0;
while(i < numlst.size()){
  //remove odd numbers but do not increment i

  if(numlst.get(i) % 2 == 1){
    numlst.remove(i);

  }else{
    //pass and increment i

    i += 1;
  }
}

/*
when removing from for-loop, the loop increments automatically
so you need to manually subtract one increment's worth from the counter var
*/


class Lunch {
 
  public static ArrayList<String> removeAnts(ArrayList<String> lunchBox) {
    // Add your code below
   for (int i = 0; i < lunchBox.size(); i ++)
   {
     if (lunchBox.get(i) == "ant")
     {
       lunchBox.remove(lunchBox.get(i));
       i--;
     }
   }
   return lunchBox;
  }
  
  public static void main(String[] args) {
    ArrayList<String> lunchContainer = new ArrayList<String>();
    lunchContainer.add("apple");
    lunchContainer.add("ant");
    lunchContainer.add("ant");
    lunchContainer.add("sandwich");
    lunchContainer.add("ant");
    lunchContainer = removeAnts(lunchContainer);
    System.out.println(lunchContainer);

  }
}


//---USING LOOPS TO ITERATE THROUGH ARRAY(LISTS)---
/*
int code = 132431214;
for (int i = 0; i < code.length; i += 1){
    code[i] += 1;
}

int ip = 0;  //initialize counter

while (ip < secretCode.size()) {
  int num = secretCode.get(i);
  secretCode.set(ip, num + 1);
  ip += 1;   //increment the while loop
}
*/
















