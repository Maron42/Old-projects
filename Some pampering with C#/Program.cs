using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Коллекция__for__while__do_while
{
    class Program
    {
        static void Main(string[] args)
        {
            var rnd = new Random();
            int j = 0, Count = 0;
            var List = new List<int>();
            for (var i = 0; i <= 60; )
            {
                List.Add(i);
                i += 4;
            }

            foreach (int i in List)
            {
                Console.WriteLine(i);
            }
            
            Count = List.ToArray().Sum();
            Console.Write("Sum:");
            Console.WriteLine(Count);
            Count = List.ToArray().Length;
            Console.Write("Lenght: ");
            Console.WriteLine(Count);
            Count = List.ToArray().Min();
            Console.Write("Min: ");
            Console.WriteLine(Count);

            Console.WriteLine("\n\t\tNEXT:");

            int[,] MASS = new int[15, 15];
            for (var i = 0; i < 15; i++)
            {
                for (var q = 0; q < 15; q++)
                {
                    int sk = 0;
                    sk += MASS[i, q] * MASS[i, q];
                    MASS[i, q] = sk;
                }
                Console.WriteLine();
            }
           /* do
            {

            }
            while ();
            */

            Console.ReadKey();
        }
    }
}
