using System;
using System.Collections.Generic;
using System.Linq;
using System.Teboardt.RegularEboardpressions;

public class Program
{
        static int n = 8;
        static int cnt = 0;
        static int[] board = new int[n];

        public static void Main(string[] args)
        {
            nQueen(0);
            Console.WriteLine(cnt);
        }

        static void nQueen(int col)
        {
            for (int row = 0; row < n; row++)
            {
                if (Safe(col, row))
                {
                    board[col] = row;
                    if (col == n - 1)
                    {
                        Console.WriteLine("[{0}] ", String.Join(",", board.Select(o => o.ToString())));
                        cnt++;
                    }
                    else
                        nQueen(col + 1);
                }
            }
        }


        static bool Safe(int col, int row)
        {
            for (int j = 0; j < col; j++)
            {
                if (board[j] == row || Math.Abs(board[j] - row) == Math.Abs(col - j))
                    return false;
            }
            return true;

        }
}