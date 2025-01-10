use std::env;
use std::process;

mod day01;
mod day02;

fn main() {
    // Collect the command-line arguments
    let args: Vec<String> = env::args().collect();

    // Check if the user provided a day argument
    if args.len() < 2 {
        eprintln!("Please provide a day number as an argument (e.g., day01, day02, etc.)");
        process::exit(1);
    }

    // Get the day argument
    let day = &args[1];

    // Match the argument and call the corresponding day's solution
    match day.as_str() {
        "day01" => day01::solve(),
        "day02" => day02::solve(),
        // Add more days as you go
        _ => {
            eprintln!("Invalid day: {}. Please provide a valid day", day);
            process::exit(1);
        }
    }
}
