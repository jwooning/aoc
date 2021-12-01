pub fn solve() {
    let mut nums: Vec<u32> = vec![];
    for n in super::shared::read_input(1).split("\n") {
        if n.len() > 0 {
            nums.push(n.parse::<u32>().unwrap());
        }
    }
    println!("Part1: ");
    for i in 0..nums.len() {
        for j in i..nums.len() {
            if nums[i] + nums[j] == 2020 {
                println!("{} * {} = {}", nums[i], nums[j], nums[i] * nums[j]);
            }
        }
    }

    println!("Part2: ");
    for i in 0..nums.len() {
        for j in i..nums.len() {
            for k in j..nums.len() {
                if nums[i] + nums[j] + nums[k] == 2020 {
                    println!("{}", nums[i] * nums[j] * nums[k]);
                }
            }
        }
    }
}
