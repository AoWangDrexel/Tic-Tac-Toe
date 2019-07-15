import java.util.Scanner;

public class TicTacToe {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		char[][] board = new char[3][3];
		int lenRow = board.length;
		int lenCol = board[0].length;

		for (int row = 0; row < lenRow; row++) {
			for (int col = 0; col < lenCol; col++) {
				board[row][col] = '-';
			}
		}

		System.out.println("Hello, welcome to the Tic Tac Toe Game!");
		System.out.println("Player One (x) : ");
		String name1 = scan.nextLine();
		System.out.println("Player Two (o) : ");
		String name2 = scan.nextLine();
		int row = 0;
		int col = 0;
		int counter = 0;

		while (!winChecker(board) && counter != 9) {
			boolean pass = false;

			if (counter % 2 == 0) {
				System.out.println("Make your move, " + name1);
				while (!pass) {
					System.out.println("Row:");
					row = scan.nextInt();
					System.out.println("Column:");
					col = scan.nextInt();
					if (placeTicOrTac(row, col, board, 'x')) {
						pass = true;
					} else {
						System.out.println("Please try again");
					}
				}

			} else {
				System.out.println("Make your move, " + name2);
				while (!pass) {
					System.out.println("Row:");
					row = scan.nextInt();
					System.out.println("Column:");
					col = scan.nextInt();
					if (placeTicOrTac(row, col, board, 'o')) {
						pass = true;
					} else {
						System.out.println("Please try again");
					}
				}

			}

			counter++;

			for (int rows = 0; rows < lenRow; rows++) {
				for (int cols = 0; cols < lenCol; cols++) {
					System.out.print(board[rows][cols] + " ");
				}
				System.out.println();
			}
			System.out.println();
		}

		if (counter % 2 == 0) {
			System.out.println(name2 + " wins!");
		} else if (counter == 9) {
			System.out.println("It's a tie!");
		} else {
			System.out.println(name1 + " wins!");
		}

	}

	static public boolean winChecker(char[][] board) {

		int lenRow = board.length;
		int lenCol = board[0].length;

		int sumOfRow = 0;
		int sumOfCol = 0;
		for (int row = 0; row < lenRow; row++) {
			for (int col = 0; col < lenCol; col++) {
				sumOfRow += board[row][col];
				sumOfCol += board[col][row];

			}
			if (sumOfRow == 360 || sumOfRow == 333 || sumOfCol == 360 || sumOfCol == 333) {
				return true;
			} else {
				sumOfRow = 0;
				sumOfCol = 0;
			}
		}

		int diagonalLeft = board[0][0] + board[1][1] + board[2][2];
		int diagonalRight = board[0][2] + board[1][1] + board[2][0];
		if (diagonalLeft == 360 || diagonalLeft == 333 || diagonalRight == 360 || diagonalRight == 333) {
			return true;
		}
		return false;
	}

	static public boolean placeTicOrTac(int row, int col, char[][] board, char mark) {
		if (row < board.length && col < board[0].length && board[row][col] != 'x' && board[row][col] != 'o') {
			board[row][col] = mark;
			return true;
		} else {
			return false;
		}

	}

}
