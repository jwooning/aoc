use std::collections::HashSet;
use regex::Regex;

pub fn solve() {
    let input = super::shared::read_input(4);

    let req: HashSet<_> = 
        vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].into_iter().collect();

    let mut p1 = 0;
    let mut p2 = 0;
    let mut curr = HashSet::<&str>::new();
    let mut curr2 = HashSet::<&str>::new();
    for n in input.split('\n') {
        if n.len() > 0 {
            for pair in n.split(' ') {
                let kv: Vec<&str> = pair.split(':').collect();
                curr.insert(kv[0]);
                match kv[0] {
                    "byr" => {
                        let v: u32 = kv[1].parse().unwrap();
                        if 1920 <= v && v <= 2002 {
                            curr2.insert(kv[0]);
                        }
                    },
                    "iyr" => {
                        let v: u32 = kv[1].parse().unwrap();
                        if 2010 <= v && v <= 2020 {
                            curr2.insert(kv[0]);
                        }
                    },
                    "eyr" => {
                        let v: u32 = kv[1].parse().unwrap();
                        if 2020 <= v && v <= 2030 {
                            curr2.insert(kv[0]);
                        }
                    },
                    "hgt" => {
                        let ui = kv[1].len() - 2;
                        let v: u32 = match kv[1][0..ui].parse() {
                            Ok(t) => t,
                            Err(_) => continue,
                        };
                        let minmax = match &(kv[1][ui..]) {
                            "cm" => (150, 193),
                            "in" => (59, 76),
                            _ => continue,
                        };
                        if minmax.0 <= v && v <= minmax.1 {
                            curr2.insert(kv[0]);
                        }
                    },
                    "hcl" => {
                        let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
                        if re.is_match(kv[1]) {
                            curr2.insert(kv[0]);
                        }
                    },
                    "ecl" => {
                        if ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&kv[1]) {
                            curr2.insert(kv[0]);
                        }
                    },
                    "pid" => {
                        let re = Regex::new(r"^[0-9]{9}$").unwrap();
                        if re.is_match(kv[1]) {
                            curr2.insert(kv[0]);
                        }
                    },
                    "cid" => (),
                    _ => panic!("Unkown key"),
                }
            }
        }
        else {
            if curr.is_superset(&req) {
                p1 += 1;
            }
            if curr2.is_superset(&req) {
                p2 += 1;
            }
            curr = HashSet::new();
            curr2 = HashSet::new();
        }
    }

    println!("p1 {}", p1);
    println!("p2 {}", p2);
}
