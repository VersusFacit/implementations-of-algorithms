use rand::Rng;
use microbench::{self, Options};

type TestCase = (Vec<i32>, i32, Option<usize>);

fn test_case_generator(n: usize) -> Vec<TestCase> {
    let mut cases: Vec<TestCase> = vec![];
    let mut rng = rand::thread_rng();

    for _ in 0..n {
        let mut v: Vec<i32> = vec![];
        let lo: i32 = rng.gen::<i32>();
        let hi: i32 = rng.gen::<i32>();
        let (lo,hi) = if lo > hi { (hi,lo) } else { (lo, hi) };
        for _ in (lo as i8)..(hi as i8) {
            v.push(rng.gen::<i32>())
        }
        v.sort();
        v.dedup();
        let target = rng.gen::<i32>();
        cases.push((v.clone(), target, v.iter().position(|x| *x == target)));
    }
    cases
}

fn binary_search(v: Vec<i32>, t: i32, lo: usize, hi: usize) -> Option<usize> {
    let mid = match hi.checked_sub(lo) {
        Some(x) => lo + x/2,
        None => return None
    };

    if t == v[mid] {
        return Some(mid)
    } else if t < v[mid] {
        binary_search(v, t, lo,
            match mid.checked_sub(1) {
                Some(x) => x,
                None => return None
            }
        )
    } else if t > v[mid] {
        binary_search(v, t, mid+1, hi)
    } else {
        panic!("unknown error!")
    }
}

fn iter_binary_search(v: Vec<i32>, t: i32, low: usize, high: usize) -> Option<usize> {
    let mut l = low;
    let mut h = high;
    while l <= h {
        let mid = match h.checked_sub(l) {
            Some(x) => l + x/2,
            None => return None
        };

        if t == v[mid] {
            return Some(mid);
        } else if t > v[mid] {
            l = mid + 1;
        } else if t < v[mid] {
            h = match mid.checked_sub(1) {
                Some(x) => x,
                None => return None
            }
        } else {
            println!("unknown error!")
        }
    }
    None
}

fn main() {
    let cases = test_case_generator(10);

    cases.into_iter().for_each(|(v, target, res)| {
        if let Some(hi) = v.len().checked_sub(1) {
            run(v, target, hi, res)
        } else {
            println!("skipped!")
        };
        println!("----------");
    });
}

fn run(v: Vec<i32>, target: i32, hi: usize, res: Option<usize>) {
    let options = Options::default();
    assert!(binary_search(v.clone(), target, 0, hi) == res);
    microbench::bench(&options, "recursive", || binary_search(v.clone(), target, 0, hi));

    assert!(iter_binary_search(v.clone(), target, 0, hi) == res);
    microbench::bench(&options, "iterative", || iter_binary_search(v.clone(), target, 0, hi));
}
