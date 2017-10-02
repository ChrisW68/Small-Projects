namespace Calculator.Library
{
    public class Calculator
    {
        public static int Divide(int numerator, int denominator)
        {
            int result = numerator / denominator;
            return result;
        }
        public static int Multiply(int firstNumber, int secondNumber)
        {
            int result = firstNumber * secondNumber;
            return result;
        }
        public static int Add(int firstNumber, int secondNumber)
        {
            int result = firstNumber + secondNumber;
            return result;
        }
        public static int Minus(int firstNumber, int secondNumber)
        {
            int result = firstNumber - secondNumber;
            return result;
        }
    }
}