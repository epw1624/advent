use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                sum += 10 * find_first_num(&ip).unwrap_or(0);
                sum += find_last_num(&ip).unwrap_or(0);
                println!("sum is now {sum}");
            }
        }
    }
    println!("{sum}");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn find_first_num(line: &str) -> Option<u32> {
    for (i, c) in line.char_indices() {
        if c.is_ascii_digit() {
            println!("index was {}", i);
            return Some(c.to_digit(10).unwrap());
        }
        else {
            let result = matches_string_forward(i, line);
            if let Some(value) = result {
                println!("index was {}", i);
                return Some(value);
            }
        }
    }
    None
}

fn find_last_num(line: &str) -> Option<u32> {
    for (i, c) in line.char_indices().rev() {
        if c.is_ascii_digit() {
            println!("index was {}", i);
            return Some(c.to_digit(10).unwrap());
        }
        else {
            let result = matches_string_backward(i+1, line);
            if let Some(value) = result {
                println!("index was {}", i);
                return Some(value);
            }
        }
    }
    None
}

fn init_hashmap() -> HashMap<String, u32> {
    let mut vals = HashMap::new();

    vals.insert(String::from("one"), 1);
    vals.insert(String::from("two"), 2);
    vals.insert(String::from("three"), 3);
    vals.insert(String::from("four"), 4);
    vals.insert(String::from("five"), 5);
    vals.insert(String::from("six"), 6);
    vals.insert(String::from("seven"), 7);
    vals.insert(String::from("eight"), 8);
    vals.insert(String::from("nine"), 9);

    return vals;
}

fn matches_string_forward(i: usize, full_string: &str) -> Option<u32> {
    let map = init_hashmap();
    for (key, value) in &map {
        if key.len() <= (full_string.len() - i) {
            let substring = &full_string[i ..(i + key.len())];
            if substring.eq(key) {
                return Some(*value);
            }
        }  
    }
    None
}

fn matches_string_backward(i: usize, full_string: &str) -> Option<u32> {
    let map = init_hashmap();
    for (key, value) in &map {
        if key.len() <= i {
            let substring = &full_string[(i - key.len())..i];
            // println!("substring is {substring}");
            if substring.eq(key) {
                return Some(*value);
            }
        }
    }
    None
}