use std::collections::HashMap;

struct Bag<'a> {
    name: &'a str,
    contains: Vec<&'a Bag<'a>>,
    containers: Vec<&'a Bag<'a>>,
}

impl Bag<'_> {
    fn new<'a>(name: &'a str) -> Bag<'a> {
        Bag {
            name,
            contains: vec![],
            containers: vec![],
        }
    }

    fn set_contains(&self, contains: Vec<&Bag>) {
        self.contains = contains;
    }

    fn add_container(&self, container: &Bag) {
        self.containers.push(container);
    }
}

pub fn solve() {
    let input = super::shared::read_input(7);

    let mut map: HashMap<&str, &Bag> = HashMap::new();
    let mut p1: u32 = 0;

    for n in input.split('\n') {
        if n.len() > 0 {
            let bags = vec![];
            let split = n.split(" contain ").collect();
            bags.push(split[0]);
            bags.push(split[1].split(", "));

            for bag in bags {
                if !map.contains(bag) {
                    map.insert(bag, Bag::new(bag));
                }
            }

            map[bags[0]].set_contains(bags[1..].map(|&b| map[b]));
            for bag in bags[1..] {
                map[bag].add_container(map[bags[0]]);
            }
        }
    }
    println!("p1 {}", p1);
}
