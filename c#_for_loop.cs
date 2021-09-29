using System;

namespace ForLoop
{
  class Program
  {
    static void Main(string[] args)
    { 
      
      for (int i = 1; i<17; i++) {
        int week = i;
        CreateTemplate(i);
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
