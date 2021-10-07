using System;

namespace SwitchStatement
{
  class Program
  {
    static void Main(string[] args)
    {
      
      Console.WriteLine("Pick a movie genre:");
      string genre = Console.ReadLine();
      
      switch(genre.ToLower()) {
        case "drama":
          Console.WriteLine("Citizen Kane");
          break;
        case "comedy":
          Console.WriteLine("Duck Soup");
          break;
        case "adventure":
          Console.WriteLine("King Kong");
          break;
        case "horror":
          Console.WriteLine("Psycho");
          break;
        case "science fiction":
          Console.WriteLine("	2001: A Space Odyssey");
          break;
        default:
          Console.WriteLine("No movie found");
          break;
        } 
      }

    }
  }
