using System;

namespace ForLoop
{
  class Program
  {
    static void Main(string[] args)
    { 
      // for loop
      for (int i = 1; i<17; i++) {
        int week = i;
        CreateTemplate(i);
      }
      
      string[] items = { "potion", "dagger", "shield", "plant" };
      
      // for each loop
      foreach (string item in items)
      {
      Console.WriteLine(item);
      }

    }
    
    static void CreateTemplate(int week)
    {
      Console.WriteLine($"Week {week}");
      Console.WriteLine("Announcements: \n \n \n ");
      Console.WriteLine("Report Backs: \n \n \n");
      Console.WriteLine("Discussion Items: \n \n \n");
    }
    
    
  }
}
