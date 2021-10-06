using System;
using System.Collections.Generic;
using System.Linq;

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      List<string> heroes = new List<string> { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
      
      // Approach 1: without LINQ
      List<string> longLoudHeroes = new List<string>();
      
      foreach (string hero in heroes)
      {
        if (hero.Length > 6)
        {
          string formatted = hero.ToUpper();
          longLoudHeroes.Add(formatted);
        }
      }
      
      // Approach 2: with LINQ
      var longLoudHeroes2 = from h in heroes
            where h.Length > 6
            select h.ToUpper();
      
      // Printing...
      Console.WriteLine("Your long loud heroes are...");
      
      foreach (string hero in longLoudHeroes2)
      {
        Console.WriteLine(hero);
      }
        
      var heroesWithI = from hero in heroes
                        where hero.Contains("i")
                        select hero; 

      var underscored = from hero in heroes
                        select hero.Replace(" ", "_");
      
      //lambda method-syntax query 
      var heroesWithI = heroes.Where(hero => hero.Contains("i"));

      foreach (string hero in heroesWithI) {
        Console.WriteLine(hero);
      }

      
    }
  }
}
