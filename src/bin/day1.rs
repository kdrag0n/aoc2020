use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() {
    let mut numbers = HashSet::new();
    for line in io::stdin().lock().lines() {
        numbers.insert(line.unwrap().parse::<i32>().unwrap());
    }

    for num in numbers.iter() {
        let candidate = 2020 - num;
        if numbers.contains(&candidate) {
            println!("{}", num * candidate);
            break;
        }
    }
}
