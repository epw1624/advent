use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                sum += 10 * find_first_num(&ip).unwrap_or(0);
                sum += find_last_num(&ip).unwrap_or(0);
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
    for c in line.chars() {
        if c.is_ascii_digit() {
            return Some(c.to_digit(10).unwrap());
        }
    }
    return None;
}

fn find_last_num(line: &str) -> Option<u32> {
    for c in line.chars().rev() {
        if c.is_ascii_digit() {
            return Some(c.to_digit(10).unwrap());
        }
    }
    return None;
}

