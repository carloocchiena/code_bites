#[derive(Debug)]
enum Coin {
  Penny,
  Nickel,
  Dime,
  Quarter,
}

fn main() {

  let penny = Coin::Penny;
  let nickel = Coin::Nickel;
  let quarter = Coin::Quarter;
    
  println!("A {:?} is worth {}", &penny, value_in_cents(&penny));
  println!("{}", value_in_cents(&nickel));
  println!("{}", value_in_cents(&quarter));
}

fn value_in_cents(coin: &Coin) -> u8 {
  match coin {
    Coin::Penny => 1,
    Coin::Nickel => 5,
    Coin::Dime => 10,
    Coin::Quarter => {
      println!("A quarter!");
      25
    }
  }
}
