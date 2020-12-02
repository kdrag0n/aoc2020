use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() {
    let mut nums_vec = Vec::new();
    let mut nums_set = HashSet::new();
    for line in io::stdin().lock().lines() {
        let num = line.unwrap().parse::<i32>().unwrap();
        nums_vec.push(num);
        nums_set.insert(num);
    }

    'outer: for x in nums_vec.iter() {
        for y in nums_vec.iter() {
            let candidate = 2020 - (x + y);
            if nums_set.contains(&candidate) {
                println!("{}", x * y * candidate);
                break 'outer;
            }
        }
    }
}
