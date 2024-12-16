# PrimeChecker
 check prime and time of checking for test
 # Prime Number Checker

This project implements a Python script to check whether a given number is prime. The program provides an efficient method using the square root optimization and optionally measures the execution time for the computation.

## Features
- Determines if a number is prime.
- Identifies the first divisor if the number is not prime.
- Optionally measures and displays the execution time of the computation.

## Usage

### Prerequisites
- Python 3.x

### How to Run
1. Save the script to a file (e.g., `prime_checker.py`).
2. Run the script in a Python environment.
   ```bash
   python prime_checker.py
   ```
3. Input the number you want to check when prompted.

### Example Execution
```plaintext
Choose a number and press enter: 29
Execution time: 0.00003 seconds
29 is prime!
```
```plaintext
Choose a number and press enter: 30
Execution time: 0.00002 seconds
30 is not prime, the first multiplier found is 2
```

## Code Explanation

### Function: `is_prime`
The core functionality is provided by the `is_prime` function, which:
1. **Takes Two Parameters**:
   - `number` (int): The number to check.
   - `time_stats` (bool): Optional flag to enable execution time measurement.

2. **Handles Edge Cases**:
   - Returns `[False, 0]` for numbers less than 2 since they are not prime.

3. **Performs Prime Check**:
   - Loops from 2 to the square root of the number (`isqrt(number)`) using the `for` loop.
   - Checks divisibility (`number % i == 0`).
   - If a divisor is found, the loop breaks early, and the function returns the divisor.

4. **Measures Execution Time** (if `time_stats=True`):
   - Uses `time.process_time()` to calculate and print the elapsed time.

5. **Returns Results**:
   - A list `[is_prime (bool), first_multiplier (int)]` where:
     - `is_prime` is `True` if the number is prime, `False` otherwise.
     - `first_multiplier` is the first divisor found or `0` if the number is prime.

### Main Program Logic
- Prompts the user to input a number.
- Calls `is_prime` with `time_stats=True` to display execution time.
- Displays whether the number is prime and, if not, the first divisor found.

## Optimization Details
- The use of `isqrt` (from `math` library) limits the loop to the square root of the number, significantly reducing the number of iterations compared to checking all numbers up to `n-1`.
- Early termination of the loop on finding the first divisor makes the function more efficient.

## Sample Output
### Prime Number
Input: `29`
Output:
```plaintext
29 is prime!
Execution time: 0.00003 seconds
```

### Non-Prime Number
Input: `30`
Output:
```plaintext
30 is not prime, the first multiplier found is 2
Execution time: 0.00002 seconds
```

## License
This project is distributed under the MIT License. Feel free to use, modify, and distribute the code.

---

For issues or suggestions, feel free to open a discussion or issue in this repository.

