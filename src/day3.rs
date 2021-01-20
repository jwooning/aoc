pub fn solve() {
    let input = super::shared::read_input(3);
    let mut map: Vec<Vec<u8>> = vec![];
    for n in input.split('\n') {
        if n.len() > 0 {
            let mut row: Vec<u8> = vec![];
            for ch in n.chars() {
                match ch {
                    '.' => row.push(0),
                    '#' => row.push(1),
                    '\n' => (),
                    _ => panic!("Encountered unkown character"),
                };
            }
            map.push(row);
        }
    }

    let mut res = 1;
    for slope in vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] {
        let trees = find(&map, slope.0, slope.1);
        println!("r: {}, d: {} -> {}", slope.0, slope.1, trees);
        res *= trees;
    }
    println!("Part2: {}", res);
}

fn find(map: &Vec<Vec<u8>>, r: usize, d: usize) -> u32 {
    let mut i = 0;
    let mut j = 0;
    let mut res = 0;
    while j < map.len() {
        res += map[j][i] as u32;
        i = (i + r) % (map[0].len());
        j += d;
    }
    res
}
