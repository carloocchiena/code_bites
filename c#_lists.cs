using System;
using System.Collections.Generic;

namespace LearnLists
{
  class Program
  {
    static void Main()
    { 
      List<string> runners = new List<string> { "Jemima Sumgong", "Tiki Gelana", "Constantina Tomescu", "Mizuki Noguchi" };
      Random rand = new Random();
      
      Console.WriteLine("In reverse chronological order, the gold medalists are...");
      
      // First loop
      for (int i = 0; i < runners.Count; i++)
      {
        Console.WriteLine($"{i+1}: {runners[i]}");
      }
      
      Console.WriteLine("\nPrinting runner bibs...");
      
      // Second loop
      foreach (string i in runners)
      {
        string name = i.ToUpper();
        int id = rand.Next(100, 1000);
        Console.WriteLine($"{id} - {name}");
      }

    }
  }
}
