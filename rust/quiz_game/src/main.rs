extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
  println!("Guess the number");

  let secret = rand::thread_rng().gen_range(1, 11);

  println!("(secret is {secret})");

  loop {

    println!("It's your turn:");
  
    let mut trial = String::new();
  
    io::stdin().read_line(&mut trial)
      .expect("Can't read the line");
  
    let trial: u32 = match trial.trim().parse() {
      Ok(num) => num,
      Err(_) => continue,
    };
  
    println!("Input is {trial}");
  
    match trial.cmp(&secret) {
      Ordering::Less    => println!("Too low"),
      Ordering::Greater => println!("Too big"),
      Ordering::Equal   => {
        println!("That's it!");
        break;
      }
    }
  }
}