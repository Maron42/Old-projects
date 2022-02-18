using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Цикл_if_и_question_mark_и_switch
{

    class Program
    {
        
        static void Main(string[] args)
        {
            Random rand = new Random(); //Задаем Random
            int input = int.Parse(Console.ReadLine()); //Задаем input?
            // var just = input == 10 ? "Yep" : "Nope"; // Истина или ложь как проверка используется
            
            string s = Console.ReadLine(); //Вводим переменную s и переводим ее в int, сейчас это не использующейся счетчик
            int q = Convert.ToInt32(s);

            if (input == 1) //цикл пошел
            {
                Console.WriteLine(rand.Next(20, 1000)); // Выводим рандомное число в диапазоне 
            }
            else if(input == 2)
            {
                Console.WriteLine(rand.Next(100000)); // Тут диапазон от нуля
            }
            else if (input == 3)
            {
                Console.WriteLine(rand.Next(0)); // Тут диапазон от нуля
            }
            else
            {
                Console.WriteLine("Э");
            }

            switch (input) //Как я понял, тот же цикл
            {
                case 1:
                    break;
                case 2:
                    break;
                default:
                    break;
            }

            Console.ReadKey();
        }
    }
}
