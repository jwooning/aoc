pub fn solve() {
    let input = super::shared::read_input(2);

    let mut p1 = 0;
    let mut p2 = 0;
    for n in input.split('\n') {
        if n.len() > 0 {
            let s: Vec<&str> = n.split(' ').collect();
            let c: Vec<&str> = s[0].split('-').collect();

            let min = c[0].parse::<u32>().unwrap();
            let max = c[1].parse::<u32>().unwrap();
            let ch = s[1].chars().nth(0).unwrap() as char;
            let passwd = s[2];

            let count = passwd.matches(ch).count() as u32;
            if min <= count && count <= max {
                p1 += 1;
            }

            let o1 = passwd.chars().nth(min as usize - 1).unwrap() as char == ch;
            let o2 = passwd.chars().nth(max as usize - 1).unwrap() as char == ch;
            if (o1 && !o2) || (!o1 && o2) {
                p2 += 1;
            }
        }
    }
    println!("Part1 {}", p1);
    println!("Part1 {}", p2);
}
