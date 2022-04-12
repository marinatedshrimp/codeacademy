public class Order {
  boolean isFilled;
  double billAmount;
  String shipping;

  public Order(boolean filled, double cost, String shippingMethod) {
		if (cost > 24.00) {
      System.out.println("High value item!");
    } else {
      System.out.println("Low value item!");
    }
    isFilled = filled;
    billAmount = cost;
    shipping = shippingMethod;
  }

  //int x = 1

  public void ship() {
    if (isFilled) {
      System.out.println("Shipping");
    } else {
      System.out.println("Order not ready");
    }

    double shippingCost = calculateShipping();

    System.out.println("Shipping cost: ");
    System.out.println(shippingCost);
  }

  public double calculateShipping() {
    double shippingCost;
    switch (shipping) {
      case "Regular":
        shippingCost = 0;
        break;
      case "Express":
        shippingCost = 1.75;
        break;
      default:
        shippingCost = .50;
    }
    return shippingCost;
 	}

  public static void main(String[] args) {
    Order myOrder = new Order(true, 134.50, "Express");
    System.out.println(myOrder.billAmount);
    System.out.println(myOrder.isFilled);
    System.out.println(myOrder.shipping);
    //why is the dot followed by instances?
  }
}

//apply to majors a college may not be known for