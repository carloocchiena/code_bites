fn main() {
  let x = 5;
  let y = 6;
  
  println!("{} * {} = {}", x , y, multiply(x, y));
}

fn multiply (x: u32, y: u32) -> u32 {
  x * y // no "Result", no ";" 
        // otherwise we'll get an error for an "implicitly returns ()"
}
