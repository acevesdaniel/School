

#include <stdio.h>

int main(void) {

    int array[300];
    int lowerLimit;
    int upperLimit;
    int counter;
    int i;

    printf("Please enter two numbers between -100 and 100 (type the numbers only, separate them with a space): ");
    scanf("%d %d", &lowerLimit, &upperLimit);

    if (upperLimit < lowerLimit) {
    
        int tempForSwap;
        tempForSwap = lowerLimit;
        lowerLimit = upperLimit;
        upperLimit = tempForSwap;
    }
    
    while ((lowerLimit < -100) || (lowerLimit == upperLimit)) {
        printf("Invalid lower limit, please try again: ");
        scanf("%d", &lowerLimit);
    }

    while ((upperLimit > 100) || (lowerLimit == upperLimit)) {
        printf("Invalid upper limit, please try again: ");
        scanf("%d", &upperLimit);
    }

    printf("Range is from %d to %d.\n", lowerLimit, upperLimit);

    counter = upperLimit - lowerLimit;

    if ((lowerLimit % 2) == 0) {
    
        lowerLimit++;

        for (i = 0; i < counter; i++) {
        array[i]= lowerLimit;
        lowerLimit +=2;
        }

        for (i = 0; i < (counter/2); i++) {
    
        printf("%d ", array[i]);
        }
    }

    else if ((lowerLimit % 2) != 0) {

        for (i = 0; i < counter; i++) {
            
            array[i]= lowerLimit;
            lowerLimit +=2;
        }

        for (i = 0; i < ((counter/2) + 1); i++) {
    
            printf("%d ", array[i]);
        }
    }


return 0;
}


/*  Today's class regards functions.

-All languages have native library funcitons.
-Moving forward, user should be able to create 'user-defined-functions'.

***         ***         ***
function syntax:

retrun_type function_name (argument_list)

(
    set of statements - Block of code
)
***         ***         ***

-Functions typically named after what they do.

In example:
    A function is created to add numbers.
    The function is named 'Add'.
    If you would like to have some sort of output, the function is a 'Return type'.

    int add (int x, int y) {
    
    return x,y;
    }
    
    -The 'int' specifies the type
    -'Add' is the name of the function.
    -The '()' next to 'Add' is the argument list (parameters), input goes here;
    -The body of the function completes required tasks necessary to perform said function.

'int main()' tell the compiler to execute the code within.

*** Function Call:
    -To call the function
        use name(and arguments);
        ex: Add(5,6);

***SEE BELOW***
*/

/*

#include <stdio.h>

int Add(int x, int y) { //Retrun type, name, argurments.

    int z;
    z = x + y;
    return z;
}

int main() {

    int x;
    x = Add(4, 7);  //Function call.
    printf("%d\n\n", x);

return 0;
}

*/

/*

//The following code is the same as above, except that the funciton is defined after being called. Function prototype prevents compiler errors.

#include <stdio.h>

int Add(int, int); //Function prototype.

int main() {

    int x;
    x = Add(4, 7);  //Function call.
    printf("%d\n\n", x);

return 0;
}

int Add(int x, int y) { //Retrun type, name, argurments.

    int z;
    z = x + y;
    return z;
}

*/