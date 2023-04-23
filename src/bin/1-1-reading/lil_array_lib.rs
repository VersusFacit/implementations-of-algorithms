/** Little array functions */

fn max(arr: &[i32]) -> Result<i32, &str> {
    let mut max: Option<i32> = None;

    arr.into_iter().for_each(|x|
        if let Some(z) = max {
            if *x > z {
                max = Some(*x);
            }
        } else {
            max = Some(*x);
        }
    );

    Ok(max.unwra (Err("empty array")))

}

/** Little 2-D matrix array */

#[derive(Clone, Copy)]
struct Matrix {
    m: usize,
    n: usize
}

impl Matrix {
    fn row_count(&self) -> usize {
        self.m
    }

    fn col_count(self) -> usize {
        self.n
    }
}

fn main() {
    let arr = [1,3,4];
    println!("hmmm: {:?}", max(&arr));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_getters() {
        let m = Matrix { m: 4, n: 3 };
        assert_eq!(m.row_count(), 4);
        assert_eq!(m.col_count(), 3);
    }
}


