use std::env;

mod shared;
mod day1;
mod day2;

fn main() {
    let args: Vec<String> = env::args().collect();
    assert!(args.len() == 2, "Supply day number");
    match args[1].parse::<u32>() {
        Ok(t) => match t {
            1 => day1::solve(),
            2 => day2::solve(),
            _ => panic!("Unkown puzzle number"),
        },
        Err(_) => panic!("Supply day number"),
    };
}

