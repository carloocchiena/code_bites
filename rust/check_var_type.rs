/ create the function
fn print_type_of<T>(_: T) {
    println!("{}", std::any::type_name::<T>())
}

/ example of running it
fn main() {
  let a: &str = "text";

  print_type_of(a);
  println!("{a}");
  
}
  
