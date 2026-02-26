/*
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

 

Constraints:

    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.

*/
public class Solution {
    static int ToInt(char c)
    {
        return (int)(c - '0');
    }

    public string Multiply(string num1, string num2) {

        int num = 0;
        int carry = 0;
        int digits2 = 1;
        int digits1 = 1;

        // Compute and multiply the values like you would do on paper
        // from right to left
        for (int i = num2.Length - 1; i >= 0 ; --i)
        {
            int n2 = ToInt(num2[i]) * digits2;
            
            for (int y = num1.Length - 1; y >= 0 ; --y)
            {
                int n1 = ToInt(num1[y]) * digits1;
                int n = n2 * n1 + carry;

                num += n % 10;
                carry = (n / (10 * digits1 * digits2));

                Console.WriteLine($"({n2} * {n1}) + {carry} = {n} num = {num} carry = {carry} d1={digits1} d2={digits2}");
                digits1 *= 10;
            }

            n2 *= 10;
            digits1 = 1;
            digits2 *= 10;
        }

        return (num).ToString();
    }
}

// "123"
// "456"
// -----*=
//   18  (6 * 3)
//  120  (6 * 20)
//  600  (6 * 100)
// -----+
//  150  (50 * 3)
// 1000  (50 * 20)
//10000  (50 * 100)
// -----+
// 1200  (400 * 3)
// 8000 (400 * 20)
//40000 (400 * 100)
// -----+
//56088

// n2 = i=2 = 2 - 3 + 2 = 1
// n2 = i=1 = 1 - 3 + 2 = 1