fn main() {

  struct Cat {
    name: & 'static str,
    color: & 'static str,
    gender: & 'static str,
  }

  let tobia = Cat{name: "tom", color: "black", gender: "male"};

  println!("Name: {}, Color: {}, Gender: {}", tobia.name, tobia.color, tobia.gender);

}
