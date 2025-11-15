//game 1 should fail blue
//game 2 should fail blue
//game 3 should pass

use std::path::Path;
use std::io::{self, BufRead};
use std::fs::File;
use std::cmp;

fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                let mut min_red = 0;
                let mut min_green = 0;
                let mut min_blue = 0;

                let game: Vec<&str> = ip.split(':').collect();
                let content = game[1];

                //iterate through all trials of a given game
                for round in content.split(';') {

                    let amounts: Vec<&str> = round.split_whitespace().collect();

                    //go through each 
                    for i in (0..amounts.len()).step_by(2) {
                        let amount: u32 = amounts[i].parse().expect("you fucked up em");
                        let color = amounts[i+1];

                        match color{
                            "red" | "red;" | "red," => {
                                min_red = cmp::max(min_red, amount);
                            },
                            "green" | "green," | "green;" => {
                                min_green = cmp::max(min_green, amount);
                            },
                            "blue" | "blue," | "blue;" => {
                                min_blue = cmp::max(min_blue, amount);
                            },
                            _ => {}
                        }

                    }
                }
                sum += min_red * min_blue * min_green;
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