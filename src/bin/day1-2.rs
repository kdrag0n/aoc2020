use std::io::{self, BufRead};

fn main() {
    let mut numbers = Vec::new();
    for line in io::stdin().lock().lines() {
        numbers.push(line.unwrap().parse::<i32>().unwrap());
    }

    'outer: for x in numbers.iter() {
        for y in numbers.iter() {
            for z in numbers.iter() {
                if x + y + z == 2020 {
                    println!("{}", x * y * z);
                    break 'outer;
                }
            }
        }
    }
}
