use std::fs;

pub fn read_input(day: u32) -> String {
    match fs::read_to_string(format!("input/day{}", day)) {
        Ok(t) => t,
        Err(_) => panic!("Could not read input"),
    }
}
