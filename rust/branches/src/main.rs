fn main() {
  
  // dynamic variables assignation
  let trigger = true;
  let number = if trigger { 9 } else { 3 };

  // if - else
  if number < 4 {
    println!("less than");
  } else if number > 6 {
    println!("bigger than");
  } else {
    println!("in range");
  }

  // loops with labels
  let mut counter: i8 = 0;
  
  let result = loop {
    counter += 1;

    if counter == 8 {
      break counter * 2;
    }
  };

  println!("result is {result}");

  // loop with labels
  let mut count = 0;
  'counting_up: loop {
    println!("count = {count}");
    let mut remaining = 10;

    loop {
      println!("remaining = {remaining}");
      if remaining == 9 {
        break;
      } 
      if count == 2 {
        break 'counting_up;
      }
      remaining -= 1;
    }
    
    count += 1;
    
  }

  println!("End count = {count}");

  // while loops
  let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");

  // while thru an array
  let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < a.len() {
        println!("the value is: {}", a[index]);

        index += 1;
    }
  
}
