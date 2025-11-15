//game 1 should fail blue
//game 2 should fail blue
//game 3 should pass

use std::path::Path;
use std::io::{self, BufRead};
use std::fs::File;

const MAX_RED: u32 = 12;
const MAX_GREEN: u32 = 13;
const MAX_BLUE: u32 = 14;

fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                let mut success = true;

                let game: Vec<&str> = ip.split(':').collect();
                let title: Vec<&str> = game[0].split_whitespace().collect();
                let content = game[1];
                let game_num: u32 = title[1].parse().expect("ftsio");
                
                for round in content.split(';') {
                    let amounts: Vec<&str> = round.split_whitespace().collect();
                    for i in (0..amounts.len()).step_by(2) {
                        let amount: u32 = amounts[i].parse().expect("you fucked up em");
                        let color = amounts[i+1];

                        match color{
                            "red" | "red;" | "red," => {
                                if amount > MAX_RED {
                                    success = false;
                                }
                            },
                            "green" | "green," | "green;" => {
                                if amount > MAX_GREEN {
                                    success = false;
                                }
                            },
                            "blue" | "blue," | "blue;" => {
                                if amount > MAX_BLUE {
                                    success = false;
                                }
                            },
                            _ => {}
                        }
                    }
                }
                if success {
                    sum += game_num;
                }
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