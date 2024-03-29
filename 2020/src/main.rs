use std::env;

mod shared;
mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;

fn main() {
    let args: Vec<String> = env::args().collect();
    assert!(args.len() == 2, "Supply day number");
    match args[1].parse::<u32>() {
        Ok(t) => match t {
            1 => day1::solve(),
            2 => day2::solve(),
            3 => day3::solve(),
            4 => day4::solve(),
            5 => day5::solve(),
            6 => day6::solve(),
            7 => day7::solve(),
            _ => panic!("Unkown puzzle number"),
        },
        Err(_) => panic!("Supply day number"),
    };
}

