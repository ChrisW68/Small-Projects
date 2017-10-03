using Microsoft.VisualStudio.TestTools.UnitTesting;
using Calculator.Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculator.Library.Tests
{
    [TestClass()]
    public class CalculatorTests
    {
        private TestContext _testContext;

        public TestContext TestContext

        {
            get
            {
                return _testContext;
            }
            set
            {
                _testContext = value;
            }
        }
        [TestMethod()]
        public void Divide_PositiveNumbers_ReturnsPositiveQuotients()
        {
            //Arrange
            int numerator = 20;
            int denominator = 4;
            int expected = 5;

            //Act
            int actual = Calculator.Divide(numerator, denominator);

            //Assert
            Assert.AreEqual(expected, actual);
        }

        [TestMethod()]
        public void Divide_PositiveNumeratorAndNegativeDenominator()
        {
            //Arrange
            int numerator = 20;
            int denominator = -4;
            int expected = -5;

            //Act
            int actual = Calculator.Divide(numerator, denominator);

            //Assert
            Assert.AreEqual(expected, actual);
        }
        public void TestMethod2()
            {
                System.Diagnostics.Debug.WriteLine("Debug: TM2 executed");
                TestContext.WriteLine("TestContext: TM2 executed");
        }
        }

    }
}