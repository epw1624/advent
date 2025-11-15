use std::path::Path;
use std::io::{self, BufRead};
use std::fs::File;
use std::cmp;


fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                let game: Vec<&str> = ip.split(':').collect();
                let numbers: Vec<&str> = game[1].split('|').collect();

                let winners: Vec<&str> = numbers[0].split_whitespace().collect();
                let yours: Vec<&str> = numbers[1].split_whitespace().collect();

                let mut winning_nums: Vec<u32> = Vec::new();
                for num in winners {
                    winning_nums.push(num.parse().expect("rip"));
                }
                let mut your_nums: Vec<u32> = Vec::new();
                for num in yours {
                    your_nums.push(num.parse().expect("rip"));
                }

                sum += get_score(winning_nums, your_nums);  
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

fn get_score(winners: Vec<u32>, yours: Vec<u32>) -> u32 {
    let mut score = 0;
    for num in yours {
        if winners.contains(&num) {
            score = cmp::max(1, 2*score);
        }
    }
    return score;
}