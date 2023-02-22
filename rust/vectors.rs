fn main() {
  let mut v: Vec<i32> = vec![1, 2, 3];

  println!("{:?}", v);

  v.push(6);

  println!("{:?}", v);

  let v1 = &v[1]; // index can goes out of range

  println!("{:?}", v1);
  
  let v2 = v.get(2); // out of ranges return None

  println!("{:?}", v2);

  let v = vec![100, 32, 57];
  for i in &v {
      println!("{i}");
  }

  enum SpreadsheetCell {
      Int(i32),
      Float(f64),
      Text(String),
  }

  let _row = vec![
      SpreadsheetCell::Int(3),
      SpreadsheetCell::Text(String::from("blue")),
      SpreadsheetCell::Float(10.12),
  ];

  
}
    
