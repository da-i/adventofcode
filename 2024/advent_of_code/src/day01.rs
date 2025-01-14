
use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn read_file_to_lines(file_path: &str) -> io::Result<impl Iterator<Item = io::Result<String>>>{
    // Check file and propegate error with ?
    let file = File::open(file_path)?;
    //  Buffer read object:
    let reader = io::BufReader::new(file);
    //  Return the lines iterator
    Ok(reader.lines())
}


pub fn solve() {
    let dev_mode = false; // Set this to false for final result
    let part2 = true; // Set this to true for part 2
    println!("Solving for day 1! {}", dev_mode);

   
    let file_path = if dev_mode {
        "input_example/day01.txt"
    } 
    else {
        "input/day01.txt"
    };

    println!("Using file: {}", file_path);

    let lines = match read_file_to_lines(file_path) {
        Ok(lines) => lines,
        Err(e) => {
            eprintln!("Error opening file: {}", e);
            return;
        }
    };
    let mut coords1 = Vec::new(); // Vector for coord1
    let mut coords2 = Vec::new(); // Vector for coord2

    for line in lines {
        match line {
            Ok(l) => {
                let parts: Vec<&str> = l.split(' ').collect();
                if dev_mode { println!("{:?}", parts);}
                let coord1 = parts[0].parse::<i32>();
                let coord2 = parts[3].parse::<i32>();
                if dev_mode { println!("{:?} {:?}", coord1, coord2);}
                // Handle parsing errors
                match (coord1, coord2) {
                    (Ok(c1), Ok(c2)) => {
                        coords1.push(c1);
                        coords2.push(c2);
                    }
                    _ => eprintln!("Failed to parse coordinates in line: {}", l),
                }
            }
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    if !part2 {
        coords1.sort();
        coords2.sort();
        
        let sums: Vec<i32> = coords1.into_iter().zip(coords2).map(|(c1, c2)| {c1 - c2}.abs()).collect();
        if dev_mode {println!("{:?}", sums);}
        // consumes the sums vector
        let sum: i32 = sums.into_iter().sum();
        println!("Final solution for day 1 is:");
        println!("{:?}", sum);
    }
    else {
        // Count the occurance in coords2 in a hash table
        let mut counts_coords2: HashMap::<i32,i32> = HashMap::new();
        for coord in coords2 {
            *counts_coords2.entry(coord).or_insert(0) += 1;
        }
        if dev_mode {println!("{:?}", counts_coords2);}

        // multiply the values of coords1 with the occurance in coords2
        let sum: i32 = coords1.into_iter().map(|c| c * counts_coords2.get(&c).unwrap_or(&0)).sum();
        println!("Final solution for day 1 part 2 is:");
        println!("{:?}", sum);

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
