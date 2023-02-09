fn main() {
  
  println!("{}", test(5));

  for (i, j) in (5..10).enumerate() {
    println!("i = {} e j = {}", i, j);
  }

  for x in 0..10 {
    println!("{}", x); // x: i32
  }

  let mut x = 5;

  loop {
      x += x - 3;
  
      println!("x is: {}", x);
  
      if x % 5 == 0 { break; }
  }

  'esterno: for x in 0..10 {
    'interno: for y in 0..10 {
        if x % 2 == 0 { continue 'esterno; } // continua al ciclo su x
        if y % 2 == 0 { continue 'interno; } // continua al ciclo su y
        println!("x: {}, y: {}", x, y);
    }
}
  
}


  fn test(x: i32) -> i32 {
    x + 2
  }

