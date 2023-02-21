#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
  }

impl Rectangle {
  fn area(&self) -> u32 {
    self.width * self.height
  }

  fn can_hold(&self, other: &Rectangle) -> bool {
    self.width > other.width && self.height > other.height
  }
}

fn main() {
  let rect1 = Rectangle {
    width: 30,
    height: 50,
  };

  let rect2 = Rectangle {
    width: 20,
    height: 10,
  };

  let rect3 = Rectangle {
    width: 50,
    height: 60,
  };

  println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
  println!("Can rect2 hold rect3? {}", rect2.can_hold(&rect3));
}

// FUNCTIONS

fn area(rectangle: &Rectangle) -> u32 {
  rectangle.width * rectangle.height
}
