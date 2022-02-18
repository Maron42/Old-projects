using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Консоль_и_цвет_конслоли_с_4_сообщениями
{
    class Program
    {
        static void Main(string[] args)
        {
            byte R = 0; // Меньше объема занимает, чем int. Byte от 0 до 255
            byte i = 5;

            Console.ForegroundColor = ConsoleColor.Magenta; //Задаем цвет букв консоли
            Console.WriteLine("Hello.Sam."); 
            Console.ReadKey(); // Каждый раз задерживаем сообщение

            Console.Clear(); // Очищаем конслоль и снова выводим что-то новое

            Console.WriteLine("I'm real!");
            Console.ReadKey();

            Console.Clear();

            Console.WriteLine("Stop! Don't do like that!");
            Console.ReadKey();

            Console.Clear();

            Console.WriteLine("Ok! I leave!");
            while (R != 5) // Задаем цикл, который делает обратный отсчет
            {
                Console.WriteLine(i);
                i = i - 1;
                Thread.Sleep(1000); // Ожидание: 1 секунда
                R += 1;
            }
                

        }
    }
}
