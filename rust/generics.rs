use std::cmp::PartialOrd as Ord;

fn main() {
  let number_list = vec![34, 50, 25, 100, 65];

  let result = largest(&number_list);

  println!("the largest number is {}", result);

  let char_list = vec!["y", "m", "c", "a"];

  let result = largest(&char_list);

  println!("the largest char is {}", result);
  
}

// FUNCTIONS
fn largest<T: Ord>(list: &[T]) -> &T {
  let mut largest = &list[0];

  for item in list {
    if item > largest {
      largest = item;
    }
  }

  largest

}

fn largest_char(list: &[char]) -> &char {
  let mut largest = &list[0];

  for item in list {
    if item > largest {
      largest = item;
    }
  }

  largest
  
}
