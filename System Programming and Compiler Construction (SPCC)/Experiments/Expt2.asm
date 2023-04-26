MACRO MUL_DIV &A,&B,&C
    MULT &A,&B
    DIV &A,&C
MEND

MAIN:
    LDR R1, &X
    MUL_DIV R1,R2,R3
    STR R1, &Y
END MAIN

&X, #10
&Y, #0
&A, #1
&B, #2
&C, #3