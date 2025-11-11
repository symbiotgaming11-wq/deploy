import streamlit as st
import html
import streamlit.components.v1 as components

st.set_page_config(page_title="PIC Programs", layout="wide")

# Hide the main area watermark and menu
st.markdown("""
    <style>
        
    </style>
""", unsafe_allow_html=True)

PIC_PROGRAMS = {
    "1FACTORIAL OF NUMBER,FIRST 50 PRIME NUMBERS,SUM AND AVERAGE": r"""
//FACTORIAL OF NUMBER
package finale;
import java.util.Scanner;
public class Prac {
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
        System.out.println("Enter the number to calculate its factorial:");
        int num = in.nextInt();
        int i = 1;
        long fact = 1;
        while (i <= num) 
       {    fact = fact * i;
             i++;
        }
System.out.println("Factorial = " + fact);
		in.close();
	}
}

// EXPERIMENT: PROGRAM TO PRINT THE FIRST 50 PRIME NUMBERS
package finale;

public class Prac {
    public static void main(String[] args) {
        int count = 0, num = 2;

        while (count < 50) {
            boolean prime = true;

            for (int i = 2; i <= num / 2; i++) {
                if (num % i == 0) {
                    prime = false;
                    break;
                }
            }

            if (prime) {
                System.out.println(num);
                count++;
            }
            num++;
        }
    }
}

// EXPERIMENT: PROGRAM TO CALCULATE THE SUM AND AVERAGE OF N NUMBERS
package finale;
import java.util.Scanner;
public class Prac {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
        System.out.print("How many numbers you want to enter: ");
        int n = sc.nextInt();
        int count = 0;
        double sum = 0;
        while (count < n) {
            System.out.print("Enter the number: ");
            double no = sc.nextDouble();
            sum += no;
            count++;
        }
        double avg = sum / n;
        System.out.println("Average of " + n + " numbers is " + avg);
        System.out.println("Sum of " + n + " numbers is " + sum);

	} }


""",
    "2.CALCULATOR": r"""
//CALCULATOR
package finale;
import java.util.Scanner;
public class Prac {

	public static void main(String[] args) {

				Scanner in = new Scanner(System.in);
				int choice;
				int no1, no2, result;
				
				do{
					System.out.println("1.Add");
					System.out.println("2.Subtract");
					System.out.println("3.Multiply");
					System.out.println("4.Divide");
					System.out.println("5.Factorial");
					System.out.println("6.Exit");
					
					System.out.println("Enter your choice:");
					choice = in.nextInt();
					
					switch(choice){
					case 1 :
						System.out.println("Enter First Number");
						no1 = in.nextInt();
						
						System.out.println("Enter Second Number");
						no2 = in.nextInt();
						
						result = no1+no2;
						
						System.out.println("Addition : " + result );
						break;
					case 2 :
						System.out.println("Enter First Number");
						no1 = in.nextInt();
						
						System.out.println("Enter Second Number");
						no2 = in.nextInt();
						
						result = no1-no2;
						
						System.out.println("Subtraction : " + result );
						break;
					case 3 :
						System.out.println("Enter First Number");
						no1 = in.nextInt();
						
						System.out.println("Enter Second Number");
						no2 = in.nextInt();
						
						result = no1*no2;
						
						System.out.println("Multiplication : " + result );
						break;
					case 4 :
						System.out.println("Enter First Number");
						no1 = in.nextInt();
						
						System.out.println("Enter Second Number");
						no2 = in.nextInt();
						
						result = no1/no2;
						
						System.out.println("Division : " + result );
						break;
					case 5 :
						System.out.println( "Enter number :");
						no1 = in.nextInt();
						
						result = 1;
						
						for(int i =1; i <= no1;++i){
							result *=i;
						}
						
						System.out.println("Factorial of " + no1 + " is "+result);
						break;
										
					case 6 :
						System.out.println("Terminating");
						break;
					default :
						System.out.println("Wrong Choice");
						break;
					}
					
				}while ( choice != 6);
			
		}

	}

""",
    "3.COMPARE TWO RECTANGLES": r"""
// EXPERIMENT: PROGRAM TO COMPARE TWO RECTANGLES BASED ON AREA AND COLOR

import java.util.Scanner;

public class rect {
	int length,width,area;
	String colour;
	void getlength() {
		Scanner sc=new Scanner(System.in);
		System.out.println("len is ");
		length= sc.nextInt();
		sc.close();
	}	
	void getwidth() {
		Scanner sc=new Scanner(System.in);
		System.out.println("wid is ");
		width= sc.nextInt();
		sc.close();
	}
	void getcolour() {
		Scanner sc=new Scanner(System.in);
		System.out.println("wid is ");
		colour= sc.next();
		sc.close();
	}
	void area() {
		area=length*width;
	}
}
class rectd{
	public static void main(String[] args) {
		rect r1=new rect();
		rect r2=new rect();
		
		System.out.println("enter rect 1 details");
		r1.getlength();
		r1.getwidth();
		r1.getcolour();
		r1.area();
		
		System.out.println("enter rect 2 details");
		r2.getlength();
		r2.getwidth();
		r2.getcolour();
		r2.area();
		
		if(r1.area==r2.area && r1.colour.equalsIgnoreCase(r2.colour)) {
			System.out.print("is same");
		}
		else {
			System.out.print("not same");
		}
	}
}

""",
"4.METHOD OVERLOADING(BY NUMBER OF ARGUMENTS& BY DATA TYPE),CONSTRUCTOR OVERLOADING": r"""'
// EXPERIMENT: PROGRAM TO DEMONSTRATE METHOD OVERLOADING (BY NUMBER OF ARGUMENTS)
package finale;

class Add {
    // Method to add two numbers
    static int add(int a, int b) {
        return a + b;
    }

    // Method to add three numbers (same name, different parameter count)
    static int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Prac {
    public static void main(String[] args) {
        System.out.println("Addition of 2 numbers: " + Add.add(10, 20));
        System.out.println("Addition of 3 numbers: " + Add.add(10, 20, 30));
    }
}


// EXPERIMENT: PROGRAM TO DEMONSTRATE METHOD OVERLOADING (BY DATA TYPE)
package finale;

class Add {
    // Add integers
    static int add(int a, int b) {
        return a + b;
    }

    // Add doubles (same name, different parameter types)
    static double add(double a, double b) {
        return a + b;
    }
}

public class Prac {
    public static void main(String[] args) {
        System.out.println("Addition of integers: " + Add.add(5, 10));
        System.out.println("Addition of doubles: " + Add.add(2.5, 3.7));
    }
}

// EXPERIMENT: PROGRAM TO DEMONSTRATE CONSTRUCTOR OVERLOADING

package finale;

class Student {
    int roll;
    String name;

    // Default constructor
    Student() {
        roll = 0;
        name = "Unknown";
    }

    // Parameterized constructor
    Student(int r, String n) {
        roll = r;
        name = n;
    }

    // Display student details
    void display() {
        System.out.println("Roll: " + roll + ", Name: " + name);
    }
}

public class Prac {
    public static void main(String[] args) {
        Student s1 = new Student();                // calls default constructor
        Student s2 = new Student(101, "aahh");   // calls parameterized constructor

        s1.display();
        s2.display();
    }
}

""",

    "5.SORT NAME,LIST OF INTEGERS": r"""
// EXPERIMENT: PROGRAM TO SORT NAMES IN ASCENDING ORDER

package finale;
import java.util.Arrays;
import java.util.Scanner;

public class Prac {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Ask how many names user wants to enter
        System.out.print("Enter number of names: ");
        int n = sc.nextInt();
        sc.nextLine(); // Consume leftover newline after integer input

        // Create an array to store names
        String[] name = new String[n];

        // Input all names
        System.out.println("Enter the names:");
        for (int i = 0; i < n; i++) {
            name[i] = sc.nextLine();
        }

        // Sort names in ascending (alphabetical) order
        Arrays.sort(name);

        // Display sorted names
        System.out.println("\nSorted Names:");
        for (String s : name) {
            System.out.println(s);
        }

        sc.close();
    }
}


// EXPERIMENT: PROGRAM TO SORT A LIST OF INTEGERS IN ASCENDING ORDER

package finale;
import java.util.Arrays;
import java.util.Scanner;

public class Prac {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Ask how many numbers user wants to enter
        System.out.print("Enter number of integers: ");
        int n = sc.nextInt();

        // Create an array to store integers
        int[] nums = new int[n];

        // Input all numbers
        System.out.println("Enter the integers:");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        // Sort integers in ascending order
        Arrays.sort(nums);

        // Display sorted list
        System.out.println("\nSorted Integers:");
        for (int x : nums) {
            System.out.println(x);
        }

        sc.close();
    }
}

""",
    "6.ADD TWO MATRICES": r"""
// EXPERIMENT: PROGRAM TO ADD TWO MATRICES

package finale;
import java.util.Scanner;

public class Prac {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter rows and columns: ");
        int r = sc.nextInt();
        int c = sc.nextInt();

        int[][] A = new int[r][c];
        int[][] B = new int[r][c];
        int[][] sum = new int[r][c];

        System.out.println("Enter Matrix A:");
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                A[i][j] = sc.nextInt();

        System.out.println("Enter Matrix B:");
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                B[i][j] = sc.nextInt();

        System.out.println("Sum of matrices:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                sum[i][j] = A[i][j] + B[i][j];
                System.out.print(sum[i][j] + "\t");
            }
            System.out.println();
        }
        sc.close();
    }
}

""",

    "7.INHERITANCE USING PLAYER CLASS": r"""
// EXPERIMENT: PROGRAM TO DEMONSTRATE INHERITANCE USING PLAYER CLASS

package finale;
import java.util.Scanner;

// Parent class
class Player {
    String name;
    int age;

    // Method to input player details
    void getData(Scanner sc) {
        System.out.print("Enter player name: ");
        name = sc.nextLine();
        System.out.print("Enter player age: ");
        age = sc.nextInt();
        sc.nextLine(); // clear newline
    }

    // Method to display player details
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Child class 1: Cricket player
class Cricket_player extends Player {
    String role;

    void getCricketData(Scanner sc) {
        System.out.print("Enter cricket role (Batsman/Bowler/All-rounder): ");
        role = sc.nextLine();
    }

    void showCricketPlayer() {
        System.out.println("\n--- Cricket Player Details ---");
        display();
        System.out.println("Role: " + role);
    }
}

// Child class 2: Football player
class Football_player extends Player {
    String position;

    void getFootballData(Scanner sc) {
        System.out.print("Enter football position (Goalkeeper/Striker/etc): ");
        position = sc.nextLine();
    }

    void showFootballPlayer() {
        System.out.println("\n--- Football Player Details ---");
        display();
        System.out.println("Position: " + position);
    }
}

// Child class 3: Hockey player
class Hockey_player extends Player {
    String fieldPosition;

    void getHockeyData(Scanner sc) {
        System.out.print("Enter hockey field position: ");
        fieldPosition = sc.nextLine();
    }

    void showHockeyPlayer() {
        System.out.println("\n--- Hockey Player Details ---");
        display();
        System.out.println("Field Position: " + fieldPosition);
    }
}

// Main class
public class Prac {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Cricket player
        Cricket_player c = new Cricket_player();
        System.out.println("\nEnter Cricket Player details:");
        c.getData(sc);
        c.getCricketData(sc);

        // Football player
        Football_player f = new Football_player();
        System.out.println("\nEnter Football Player details:");
        f.getData(sc);
        f.getFootballData(sc);

        // Hockey player
        Hockey_player h = new Hockey_player();
        System.out.println("\nEnter Hockey Player details:");
        h.getData(sc);
        h.getHockeyData(sc);

        // Display all players
        c.showCricketPlayer();
        f.showFootballPlayer();
        h.showHockeyPlayer();

        sc.close();
    }
}

""",

    "9.EXCEPTION HANDLING": r"""
// EXPERIMENT:EXCEPTION HANDLING(TRY AND CATCH)

package finale;
import java.util.Scanner; 
public class Prac { 
public static void main(String[] args) { 
Scanner a= new Scanner(System.in); 
try { 
System.out.println("Enter numerator:"); 
int n= a.nextInt(); 
System.out.println("Enter denominator:"); 
int m= a.nextInt(); 
int result= n/m; 
System.out.println("Result:" + result); 
} catch(ArithmeticException E) { 
System.out.println("Cannot divide by zero"); 
} 
a.close(); 
} 
} 
""",
    "10.File Handling": r"""
//Program to demonstrate File Handling using FileWriter and FileReader

package finale;// FileExample.java

import java.io.*;

public class Prac {
 public static void main(String[] args) {
     try {
         // Writing data to a file
         FileWriter fw = new FileWriter("sample.txt");
         fw.write("Hello, this is a FileWriter and FileReader example in Java.\n");
         fw.write("File handling allows reading and writing data to files easily.");
         fw.close();
         System.out.println(" Data successfully written to file: sample.txt");

         // Reading data from the same file
         FileReader fr = new FileReader("sample.txt");
         int i;
         System.out.println("\n Reading data from file:");
         while ((i = fr.read()) != -1) {
             System.out.print((char) i);
         }
         fr.close();
     } 
     catch (IOException e) {
         System.out.println(" An error occurred: " + e.getMessage());
     }
 }
}
""",
}

st.sidebar.title("-")
sel = st.sidebar.radio("Select", list(PIC_PROGRAMS.keys()))
code = PIC_PROGRAMS[sel]

# Create a JS-safe version of the raw code to copy via clipboard (escape backticks and backslashes)
js_safe = code.replace('\\','\\\\').replace('`','\\`')

# Persistent copy button in the sidebar — always available and will copy the raw code even if the
# main code panel is not visible.
with st.sidebar:
    components.html(f"""
    <div style='padding:6px;display:flex;justify-content:flex-end;'>
        <button style='padding:6px 10px;border-radius:4px;border:none;background:#28a745;color:#fff;cursor:pointer;font-weight:600;' onclick="navigator.clipboard.writeText(`{js_safe}`)">Copy</button>
    </div>
    """, height=60)

pre_id = f"code_{abs(hash(sel))}"
esc = html.escape(code)
components.html(f"""
<div style='background:#f1f1f1;padding:10px;border-radius:6px;position:relative;'>
    <button style='position:absolute;top:8px;left:8px;padding:6px 10px;border-radius:4px;border:none;background:#007bff;color:#fff;cursor:pointer;z-index:2;font-weight:600;display:inline-flex;align-items:center;gap:4px;' 
        onclick="(() => {{
            const btn = event.target;
            const text = document.getElementById('{pre_id}').innerText;
            navigator.clipboard.writeText(text)
                .then(() => {{
                    btn.innerHTML = '✓ Copied';
                    setTimeout(() => btn.innerHTML = 'Copy', 1000);
                }})
                .catch(err => alert('Failed to copy: ' + err));
        }})()">Copy</button>
    <pre id='{pre_id}' style='white-space:pre-wrap;font-family:monospace;margin-top:36px;max-height:500px;overflow-y:auto;'>{esc}</pre>
</div>
""",height=700)

# Keep the download button but hide code display
if sel:
    st.download_button("Download", code, file_name=sel+".c")
