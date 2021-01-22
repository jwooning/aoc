use std::cmp::max;

pub fn solve() {
    let input = super::shared::read_input(5);

    let mut p1 = 0;
    for n in input.split('\n') {
        if n.len() > 0 {
            let seat = find_seat(n);
            let id = seat.0 * 8 + seat.1;
            p1 = max(p1, id);
        }
    }
    println!("p1: {}", p1);
    
    let mut map: Vec<bool> = vec![false; p1 as usize + 1];
    for n in input.split('\n') {
        if n.len() > 0 {
            let seat = find_seat(n);
            let id = seat.0 * 8 + seat.1;
            map[id as usize] = true;
        }
    }
    for i in 1..=map.len() - 2 {
        if map[i - 1] && !map[i] && map[i + 1] {
            println!("p2: {}", i);
        }
    }
}

fn find_seat(pass: &str) -> (u32, u32) {
    let mut ri = 0;
    let mut rl = 128;
    let mut ci = 0;
    let mut cl = 8;
    for ch in pass.chars() {
        match ch {
            'F' => rl /= 2,
            'B' => {
                rl /= 2;
                ri += rl;
            },
            'L' => cl /= 2,
            'R' => {
                cl /= 2;
                ci += cl;
            },
            _ => panic!("Invalid character"),
        }
    }
    assert!(rl == 1 && cl == 1, "Not exactly specified");
    (ri, ci)
}
