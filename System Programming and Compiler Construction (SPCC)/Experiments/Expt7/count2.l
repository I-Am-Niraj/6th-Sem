/*This program is going to count total number of lines and total number of
Characters present in input file*/
%{
#include <stdlib.h>

%}

KEYWORD  void|int|float|char|return|for|if|else|while
DIGIT    [0-9]
ID       [a-zA-z][a-zA-z0-9]*
INT      {DIGIT}+
REAL     {DIGIT}*"."{DIGIT}+


%%

{KEYWORD}   {
		printf("The keyword :%s\n",yytext);
	    }


{INT}       {
            printf( "An integer: %s (%d)\n", yytext,
                    atoi( yytext ) );
            }

{REAL}      {
            printf( "A float: %s (%g)\n", yytext,
                    atof( yytext ) );
            }

if          {printf( "The keyword: %s\n", yytext );
            }
            

{ID}        printf( "An identifier: %s\n", yytext );



[ \t\n]+          /* eat up whitespace */

.           printf( "Unrecognized character: %s\n", yytext );

%%

main(void)
	{
	yyin= fopen("myfile.txt","r");  
	yylex();
	//printf(" This File contains ...");
	//printf("\n\t%d lines", num_lines);
	//printf("\n\t%d words",words);
	//printf("\n\t%d small letters", s_letters);
	//printf("\n\t%d capital letters",c_letters);
	//printf("\n\t%d digits", num);
	//printf("\n\t%d Total characters\n",num_chars);
	//printf("\n\tIn total %d characters.\n",total);
	}


