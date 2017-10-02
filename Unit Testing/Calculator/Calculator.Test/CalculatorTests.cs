using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Calculator.Library.Test
{
    [TestClass]
    public class CalculatorTests
    {
        [TestMethod]
        public void Divide_PositiveNumbers_ReturnPositiveQuotient()
        {
            //Arrange Section
            int expected = 5;
            int numerator = 20;
            int denominator = 4;

            //Act Section
            int actual = Calculator.Divide(numerator, denominator);

            //Assert Section
            Assert.AreEqual(expected, actual);
        }
        [TestMethod]
        public void Divide_PositiveNumeratorAndNegativeDenomitor_ReturnNegativeQuotient()
        {
            //Arrange Section
            int expected = -5;
            int numerator = 20;
            int denominator = -4;

            //Act Section
            int actual = Calculator.Divide(numerator, denominator);

            //Assert Section
            Assert.AreEqual(expected, actual);
        }
        [TestMethod]
        public void Divide_NegativeNumbers_ReturnPositiveQuotient()
        {
            //Arrange Section
            int expected = 5;
            int numerator = -20;
            int denominator = -4;

            //Act Section
            int actual = Calculator.Divide(numerator, denominator);

            //Assert Section
            Assert.AreEqual(expected, actual);
        }
    }
}
