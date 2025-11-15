use std::path::Path;
use std::io::{self, BufRead};
use std::fs::File;

const BOTH: u32 = 0;
const NEXT_ONLY: u32 = 1;
const PREV_ONLY: u32 = 2;

fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        sum += get_current_line_sum("blah", lines[0], lines[1], NEXT_ONLY);

        for i in (1..lines.len() - 1) {
            sum += get_current_sum(lines[i-1], lines[i], lines[i+1], BOTH);
        }

        sum += get_current_sum(lines[lines.len() - 2], lines[lines.len() - 1], "blah", PREV_ONLY);

        println!("{sum}");
    }

}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn get_whole_number(line: &str, idx: u32) -> u32 {
    let mut end = idx;

    while line[end].is_ascii_digit() {
        end += 1;
    }

    return end;
}

fn get_current_line_sum(prev_line: &str, cur_line: &str, next_line: &str, mode: u32) -> u32 {
    let mut sum = 0;
    let mut i = 0;
    while i < cur_line.len() {
        if cur_line[i].is_ascii_digit() {
            let end = get_whole_number(cur_line, i);

            let mut valid = false;
            
            if cur_line[i-1] != '.' || cur_line[end] != '.' {
                valid = true;
            }

            if mode != NEXT_ONLY {
                for j in (i-1..end+1) {
                    if prev_line[j] != '.' {
                        valid = true;
                    }
                }
            }
            if mode != PREV_ONLY {
                for j in (i-1..end+1) {
                    if next_line[j] != '.' {
                        valid = true;
                    }
                }
            }

            if valid {
                sum += cur_line[i..end as usize].parse().expect("rip");
            }
            i = end as usize;
        }
        i += 1;
    }
    return sum;
}