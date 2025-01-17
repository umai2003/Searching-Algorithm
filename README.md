
# Search Algorithms: Binary Search and Linear Search

## Purpose of the Code
This repository demonstrates the implementation of two fundamental search algorithms: **Binary Search** and **Linear Search**.  
These algorithms are commonly used for retrieving data from arrays. The purpose of this project is to:
- Compare the efficiency of these algorithms.
- Understand their behavior under different scenarios, including worst-case performance.

## How to Run the Program
Follow these steps to run the program:

1. Clone this repository to your local machine:
   ```bash
   git clone (https://github.com/umai2003/Searching-Algorithm)
   ```
2. Navigate to the project directory:
   ```bash
   cd Searching-Algorithm
   ```
3. Run the script (assuming Python is used):
   ```bash
   python search_algorithms.py
   ```
4. Input the required array and target number as prompted by the program.

## Time Complexity Analysis
### Binary Search
- **Best Case:** O(1) (when the middle element is the target).
- **Worst Case:** O(log n) (when the target is at the beginning or end of a sorted array).
- **Example of Worst Case:**  
  For a sorted array `[1, 2, 3, 4, 5, 6, 7, 8]` and target `8`, the algorithm performs multiple divisions of the search range until it finds the target.

### Linear Search
- **Best Case:** O(1) (when the first element is the target).
- **Worst Case:** O(n) (when the target is the last element or not present).
- **Example of Worst Case:**  
  For an array `[1, 2, 3, 4, 5, 6, 7, 8]` and target `8`, the algorithm scans each element sequentially.

## Program Output
The program will:
1. Search for the target using both algorithms.
2. Print the result of each search.
3. Display the total time taken for both searches to help understand the efficiency difference.

## Features
- Clean and readable code with comments for clarity.
- Handles edge cases like empty arrays and invalid inputs.
- Prints the numbers involved in the **worst-case scenario** for Binary Search.

## Learning Outcomes
Through this project, I have:
- Gained hands-on experience with core searching techniques.
- Developed a better understanding of algorithmic efficiency.
- Improved my ability to write well-documented and maintainable code.

## Contribution
Feel free to:
- Report issues.
- Suggest improvements.
- Fork and create pull requests for new features or bug fixes.

## License
This project is licensed under the [MIT License](LICENSE).

---

Happy Coding! 😊
