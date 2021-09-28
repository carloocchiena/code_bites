using System;

namespace BuiltInMethods
{
  class Program
  {
    static void Main(string[] args)
    {     
      string[] summerStrut;
      
      summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };
      
      int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

      int rate = Array.IndexOf(ratings, 3);
      Console.WriteLine(rate);

      string song = summerStrut[rate];
      Console.WriteLine($"Song {song} is rated 3 number 4");
      
      string song2 = Array.Find(summerStrut, length => length.Length > 10);

      Console.WriteLine($"The song is {song2}");

      Array.Sort(summerStrut);

      Console.WriteLine($"{summerStrut[0]}, {summerStrut[summerStrut.Length-1]}");


    }
  }
}
