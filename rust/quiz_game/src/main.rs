use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
  println!("Guess the number!");

  let secret_number: u32 = rand::thread_rng().gen_range(1..10);

  println!("Secret is {secret_number}");

  loop {
  
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
  
    let guess: u32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => {
          println!("Please, insert a number:");
          continue;
        }
      };
  
    println!("You guessed: {guess}");
  
    match guess.cmp(&secret_number) {
      Ordering::Less => println!("Too small!"),
      Ordering::Greater => println!("Too big!"),
      Ordering::Equal => {
        println!("You win!");
        break;
      }
    }
  }
}
