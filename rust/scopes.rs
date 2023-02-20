fn main() {
  {
    let s = "this is a scope";
    println!("{s}");

    let mut b = String::from("this is also as scope");
    b.push_str(" and i can add things");
    println!("{b}");
    // s.push_str(", isn't it?"); // !error method not found in &str

    
    // OWNERSHIP
    take_ownership(b);
    // println!("{b}"); // !error value borrowed here after move // the function has taken the
                        // pointer to the string, dropping its original scope 
                        // this means that even a trivial len() will drop our initial variable
                        // how can we fix that? borrowing it instead than "owning" it.

    let c = String::from("another string var");
    
    let d = give_back(c); // using return in a function allow us to assign it instead than 
                          // dropping it
    println!("{d}");

    // BORROWING
    let e = String::from("borrow me");
    borrow_var(&e); 
    println!("{e}"); // this has been possibile thanks to the & reference sign, used 
                     // both in function arguments than in function call

    // BORROWING WITH MUTABILITY
    let mut f = String::from("change me");

    change_var(&mut f);
    
  }

  // println!("{s}") // !error not found in this scope
  // println!("{b}"); // !error not found in this scope

  let mut a = String::from("hello"); 

  a.push_str(", world!");

  println!("{a}");
  
}

// FUNCTIONS

fn take_ownership(some_string: String) {
  println!("{some_string}");
}

fn give_back(a_string: String) -> String {
  a_string
}

fn borrow_var(a_string: &String) {
  println!("{a_string}");
}

fn change_var(a_string: &mut String) {
  a_string.push_str(", added content");
  println!("{a_string}");
}
