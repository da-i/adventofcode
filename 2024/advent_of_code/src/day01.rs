
use std::fs::File;
use std::io::{self, BufRead, BufReader, Lines};

fn read_file_to_lines(file_path: &str) -> impl Iterator<Item = io::Result<String>>{
    // Check file and propegate error with ?
    let file = File::open(file_path).unwrap();
    //  Buffer read object:
    let reader = io::BufReader::new(file);
    //  Return the lines iterator
    reader.lines()
}

pub fn solve() {
    let dev_mode = true; // Set this to false for production
    println!("Solving for day 1! {}", dev_mode);

   
    let file_path = if dev_mode {
        "input_example/day01.txt"
    } 
    else {
        "input/day01.txt"
    };

    println!("Using file: {}", file_path);
    let lines = read_file_to_lines(file_path);

    for line in lines {
        match line {
            Ok(content) => println!("{}", content),
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        // Test your function here
    }
}
