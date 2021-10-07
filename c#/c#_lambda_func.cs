using System;

namespace AlternateExpressions
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] spaceRocks = {"meteoroid", "meteor", "meteorite"};
      
      // lambda 
      bool makesContact = Array.Exists(spaceRocks, s => s == "meteorite");
      
      if (makesContact)
      {
        Console.WriteLine("At least one space rock has reached the Earth's surface!");
      } 
    } 
  }
}
