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
      
      // Query syntax
      var longLoudheroes = from h in heroes
      where h.Length > 6
      select h.ToUpper();
 
      // Method syntax - separate statements
      var longHeroes = heroes.Where(h => h.Length > 6);
      var longLoudHeroes = longHeroes.Select(h => h.ToUpper());

      // Method syntax - chained expressions
      var longLoudHeroes2 = heroes
                            .Where(h => h.Length > 6)
                            .Select(h => h.ToUpper());

      var dude = heroes.Select(h => $"Introducing...{h}!");

      var test = from hero in heroes
      where hero.Contains(" ")
      select hero.IndexOf(" ");

      var caso = heroes
      .Where(h=> h.Contains(" "))
      .Select(h=> h.IndexOf(" "));

      foreach (string i in dude) {
        Console.WriteLine(i);
      }

      foreach (int i in test) {
        Console.WriteLine(i);
      }

      foreach (int i in caso) {
        Console.WriteLine(i);
      }
      
      
    }
  }
}
