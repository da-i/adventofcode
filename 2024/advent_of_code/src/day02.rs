
use std::fs::File;
use std::io::{self, BufRead};


fn read_file_to_lines(file_path: &str) -> io::Result<impl Iterator<Item = io::Result<String>>>{
    // Check file and propegate error with ?
    let file = File::open(file_path)?;
    //  Buffer read object:
    let reader = io::BufReader::new(file);
    //  Return the lines iterator
    Ok(reader.lines())
}


fn check_report(report: Vec<i32>) -> bool {
    let mut safe = false;

    safe
}

pub fn solve() {
    let dev_mode = true; // Set this to false for final result
    let part1 = false; // Set this to true for part 2
    println!("Solving for day 2! dev = {} part 1 = {}", dev_mode, part1);

    // Your solution code
    let file_path = if dev_mode {
        "input_example/day02.txt"
    } 
    else {
        "input/day02.txt"
    };
    println!("Using file: {}", file_path);
    let lines = match read_file_to_lines(file_path) {
        Ok(lines) => lines,
        Err(e) => {
            eprintln!("Error opening file: {}", e);
            return;
        }
    };
    let mut safe_reports: i32 = 0;
    for line in lines {
        match line {
            Ok(l) => {
                let report: Result<Vec<i32>,_> = l.split(' ').map(|c| c.parse::<i32>()).collect();
                // if dev_mode { println!("{:?}", report);}
                match report {
                    Ok(report) => {
                        if dev_mode { println!("{:?}", report);}
                        let safe_status = check_report(report);
                        if dev_mode { println!("{:?}", safe_status);}

                        if safe_status{safe_reports += 1;}
                    }
                    _ => {
                        eprintln!("Failed to parse report line into report: {}", l);
                    }
                }
            }
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    println!("Safe reports: {}", safe_reports);
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        // Test your function here
    }
}
