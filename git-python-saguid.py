using System;

class Program
{
    static void Main(string[] args)
    {
        bool showMenu = true;

        while (showMenu)
        {
            showMenu = MainMenu();
        }
    }

    static bool MainMenu()
    {
        Console.Clear();
        Console.WriteLine("===========================================================================");
        Console.WriteLine("                    Final Project Computer Programing 2");
        Console.WriteLine("===========================================================================");
        Console.WriteLine("                                Main Menu");
        Console.WriteLine("===========================================================================");
        Console.WriteLine("                                1. For Loop");
        Console.WriteLine("                                2. Do While");
        Console.WriteLine("                                3. While Loop");
        Console.WriteLine("                                4. Array");
        Console.WriteLine("                                5. Exit");
        Console.WriteLine("===========================================================================");
        Console.Write("                               Enter your choice: ");


        switch (Console.ReadLine())
        {
            case "1":
                ForLoop();
                return true;
            case "2":
                Dowhile();
                return true;
            case "3":
                WhileLoop();
                return true;
            case "4":
                Array();
                return true;
            case "5":
                Console.WriteLine("Exiting the program...");
                return false;
            default:
                Console.WriteLine("Please enter a valid option (1-5).");
                Console.ReadLine();
                return true;
        }
    }

    static void ForLoop()
    {
        bool showSubMenu = true;

        while (showSubMenu)
        {
            Console.Clear();
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          For Loop Submenu:");
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          1. Show Code");
            Console.WriteLine("                          2. Run the Code");
            Console.WriteLine("                          3. Back to Main Menu");
            Console.WriteLine("===========================================================================");
            Console.Write("                            Enter your choice: ");

            switch (Console.ReadLine())
            {
                case "1":
                    Console.WriteLine("You selected Show Code.");
                    string forLoopCode = @"

using System;

class Program
{
    static void Main()
    {
        for (bool runagain = true; runagain == true;)
        {
            Console.Write(""Enter your exam score: "");
            if (int.TryParse(Console.ReadLine(), out int examScore))
            {
                string result = Grades(examScore);
                Console.WriteLine(""Result: "" + result);
            }
            else
            {
                Console.WriteLine(""Invalid input. Please enter a valid integer score."");
                continue;
            }
            Console.Write(""Do you want to continue? (YES/NO): "");
            string userInput = Console.ReadLine().ToLower();
            if (userInput != ""yes"")
            {
                runagain = false;
            }
        }
    }

    static string Grades(int score)
    {
        if (score == 100)
        {
            return ""EXCELLENT"";
        }
        else if (score >= 90 && score <= 99)
        {
            return ""VERY GOOD"";
        }
        else if (score >= 80 && score <= 89)
        {
            return ""GOOD"";
        }
        else if (score >= 70 && score <= 79)
        {
            return ""PASSED"";
        }
        else
        {
            return ""FAILED"";
        }
    }
}";
                    Console.WriteLine();
                    Console.WriteLine(forLoopCode);
                    Console.WriteLine("Press Enter To Choose Number Again.");
                    Console.ReadLine();
                    break;
                case "2":
                    Forlooprun();
                    Console.WriteLine();
                    Console.WriteLine("Press Enter to exit and choose number again.");
                    Console.ReadLine();
                    break;
                case "3":
                    showSubMenu = false;
                    break;
                default:
                    Console.WriteLine("Please enter a valid option (1-3).");
                    Console.ReadLine();
                    break;
            }
        }

    }
    static void Forlooprun()
    {
        for (bool runagain = true; runagain == true;)
        {
            Console.Write("Enter your exam score: ");
            if (int.TryParse(Console.ReadLine(), out int examScore))
            {
                string result = Grades(examScore);
                Console.WriteLine("Result: " + result);
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid integer score.");
                continue;
            }
            Console.Write("Do you want to continue? (YES/NO): ");
            string userInput = Console.ReadLine().ToLower();
            if (userInput != "yes")
            {
                runagain = false;
            }
        }
    }

    static void Dowhile()
    {
        bool showSubMenu = true;

        while (showSubMenu)
        {
            Console.Clear();
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          Do While Submenu:");
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          1. Show Code");
            Console.WriteLine("                          2. Run the Code");
            Console.WriteLine("                          3. Back to Main Menu");
            Console.WriteLine("===========================================================================");
            Console.Write("                            Enter your choice: ");

            switch (Console.ReadLine())
            {
                case "1":
                    Console.WriteLine("You selected Show Code.");
                    string doWhileLoopCode = @"

static void main()
{
    char continueInput;
    do
    {
        Console.Write(""Enter a decimal number: "");

        if (int.TryParse(Console.ReadLine(), out int decimalNumber))
        {
            string octalNumber = DecimalToOctal(decimalNumber);
            Console.WriteLine($""Octal equivalent: {octalNumber}"");
        }
        else
        {
            Console.WriteLine(""Invalid input. Please enter a valid decimal number."");
        }

        Console.Write(""Do you want to enter another number? (YES/NO): "");
        continueInput = Console.ReadLine().Trim().ToLower()[0];

    }
    while (continueInput == 'y');
}

static string DecimalToOctal(int decimalNumber)
{
    string octalNumber = Convert.ToString(decimalNumber, 8);
    return octalNumber;
}";
                    Console.WriteLine(doWhileLoopCode);
                    Console.WriteLine("Press Enter To Choose Number Again.");
                    Console.ReadLine();
                    break;
                case "2":
                    DowhileloopRun();
                    Console.WriteLine();
                    Console.WriteLine("Press Enter to exit and choose number again.");
                    Console.ReadLine();
                    break;
                case "3":
                    showSubMenu = false;
                    break;
                default:
                    Console.WriteLine("Please enter a valid option (1-3).");
                    Console.ReadLine();
                    break;
            }
        }
    }
    static void DowhileloopRun()
    {
        char continueInput;
        do
        {
            Console.Write("Enter a decimal number: ");

            if (int.TryParse(Console.ReadLine(), out int decimalNumber))
            {
                string octalNumber = DecimalToOctal(decimalNumber);
                Console.WriteLine($"Octal equivalent: {octalNumber}");
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid decimal number.");
            }

            Console.Write("Do you want to enter another number? (YES/NO): ");
            continueInput = Console.ReadLine().Trim().ToLower()[0];

        }
        while (continueInput == 'y');
    }

    static string DecimalToOctal(int decimalNumber)
    {

        string octalNumber = Convert.ToString(decimalNumber, 8);
        return octalNumber;
    }



    static void WhileLoop()
    {
        bool showSubMenu = true;

        while (showSubMenu)
        {
            Console.Clear();
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          While Loop Submenu:");
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          1. Show Code");
            Console.WriteLine("                          2. Run the Code");
            Console.WriteLine("                          3. Back to Main Menu");
            Console.WriteLine("===========================================================================");
            Console.Write("                            Enter your choice: ");

            switch (Console.ReadLine())
            {
                case "1":
                    Console.WriteLine("You selected Show Code.");
                    string whileLoopCode = @"

static void main()
{
    bool runagain = true;
    
    while (runagain)
    {
        Console.Write(""Enter your exam score: "");
        if (int.TryParse(Console.ReadLine(), out int examScore))
        {
            string result = Grades(examScore);
            Console.WriteLine(""Result: "" + result);
        }
        else
        {
            Console.WriteLine(""Invalid input. Please enter a valid integer score."");
            continue;
        }
        Console.Write(""Do you want to continue? (YES/NO): "");
        string userInput = Console.ReadLine().ToLower();
        if (userInput != ""yes"")
        {
            runagain = false;
        }
    }
}";
                    Console.WriteLine(whileLoopCode);
                    Console.WriteLine();
                    Console.WriteLine("Press Enter To Choose Number Again.");
                    Console.ReadLine();
                    break;
                case "2":
                    whileloopRun();
                    Console.WriteLine();
                    Console.WriteLine("Press Enter to exit and choose number again.");
                    Console.ReadLine();
                    break;
                case "3":
                    showSubMenu = false;
                    break;
                default:
                    Console.WriteLine("Please enter a valid option (1-3).");
                    Console.ReadLine();
                    break;
            }
        }
    }
    static void whileloopRun()
    {
        bool runagain = true;

        while (runagain)
        {
            Console.Write("Enter your exam score: ");
            if (int.TryParse(Console.ReadLine(), out int examScore))
            {
                string result = Grades(examScore);
                Console.WriteLine("Result: " + result);
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid integer score.");
                continue;
            }
            Console.Write("Do you want to continue? (YES/NO): ");
            string userInput = Console.ReadLine().ToLower();
            if (userInput != "yes")
            {
                runagain = false;
            }
        }
    }
    static void Array()
    {
        bool showSubMenu = true;

        while (showSubMenu)
        {
            Console.Clear();
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          Array Submenu:");
            Console.WriteLine("===========================================================================");
            Console.WriteLine("                          1. Show Code");
            Console.WriteLine("                          2. Run the Code");
            Console.WriteLine("                          3. Back to Main Menu");
            Console.WriteLine("===========================================================================");
            Console.Write("                            Enter your choice: ");

            switch (Console.ReadLine())
            {
                case "1":
                    Console.WriteLine("You selected Show Code.");
                    string arrayCode = @"

static void main()
{
    do
    {
        Console.Write(""Enter a decimal number: "");
        int decimalNumber = int.Parse(Console.ReadLine());

        string binaryNumber = DecimalToBinary(decimalNumber);

        Console.WriteLine(""Binary equivalent: "" + binaryNumber);

        Console.Write(""Do you want to continue? (YES/NO): "");
    } while (Console.ReadLine().ToLower() == ""yes"");
}

static string DecimalToBinary(int decimalNumber)
{
    string binaryNumber = "";

    while (decimalNumber > 0)
    {
        int remainder = decimalNumber % 2;
        binaryNumber = remainder.ToString() + binaryNumber;
        decimalNumber /= 2;
    }

    return binaryNumber;
}

static string[] DecimalArrayToBinaryArray(int[] decimalArray)
{
    string[] binaryArray = new string[decimalArray.Length];

    for (int i = 0; i < decimalArray.Length; i++)
    {
        binaryArray[i] = DecimalToBinary(decimalArray[i]);
    }

    return binaryArray;
}";
                    Console.WriteLine();
                    Console.WriteLine("Press Enter To Choose Number Again.");
                    Console.ReadLine();
                    break;
                case "2":
                    Arrayrun();
                    Console.WriteLine();
                    Console.WriteLine("Press Enter to exit and choose number again.");
                    Console.ReadLine();
                    break;
                case "3":
                    showSubMenu = false;
                    break;
                default:
                    Console.WriteLine("Please enter a valid option (1-3).");
                    Console.ReadLine();
                    break;
            }
        }
    }
    static void Arrayrun()
    {
        do
        {
            Console.Write("Enter a decimal number: ");
            int decimalNumber = int.Parse(Console.ReadLine());

            string binaryNumber = DecimalToBinary(decimalNumber);

            Console.WriteLine("Binary equivalent: " + binaryNumber);

            Console.Write("Do you want to continue? (YES/NO): ");
        } while (Console.ReadLine().ToLower() == "yes");
    }

    static string DecimalToBinary(int decimalNumber)
    {
        string binaryNumber = "";

        while (decimalNumber > 0)
        {
            int remainder = decimalNumber % 2;
            binaryNumber = remainder.ToString() + binaryNumber;
            decimalNumber /= 2;
        }

        return binaryNumber;
    }

    static string[] DecimalArrayToBinaryArray(int[] decimalArray)
    {
        