pub fn solve() {
    let input = super::shared::read_input(6);

    let mut map: Vec<u32> = vec![0; 26];
    let mut map2: Vec<u32> = vec![1; 26];
    let mut map3: Vec<u32> = vec![0; 26];
    let mut p1: u32 = 0;
    let mut p2: u32 = 0;
    for n in input.split('\n') {
        if n.len() > 0 {
            for ch in n.as_bytes() {
                let i = ch - b'a';
                map[i as usize] = 1;
                map3[i as usize] = 1;
            }
            for i in 0..map2.len() {
                map2[i] = if map2[i] == 1 && map3[i] == 1 { 1 } else { 0 }
            }
            map3 = vec![0; 26];
        }
        else {
            p1 += map.iter().sum::<u32>();
            p2 += map2.iter().sum::<u32>();
            map = vec![0; 26];
            map2 = vec![1; 26];
        }
    }
    println!("p1 {}", p1);
    println!("p2 {}", p2);
}
