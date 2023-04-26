%{

#include<stdio.h>        
int lines=0, words=0,s_letters=0,c_letters=0, num=0, spl_char=0,total=0; //Global variable declaration

%}

%%

\n { lines++; words++;}      //\n represent new line plus end of one word

[\t ' ']+ words++;       // 0 or more \t or space represent recognition of one word

[A-Z] c_letters++;     //any upper case letter recognize upper case letter

[a-z] s_letters++;   //any lower case letter recognize lower case letter

[0-9] num++;       //any digit from 0 to 9 recognize digit

. spl_char++;     //any other character (do not match with above RE) recognize special character



%%

main(void)
	{
	yyin= fopen("myfile.txt","r");  
	yylex();
	total=s_letters+c_letters+num+spl_char;
	printf(" This File contains ...");
	printf("\n\t%d lines", lines);
	printf("\n\t%d words",words);
	printf("\n\t%d small letters", s_letters);
	printf("\n\t%d capital letters",c_letters);
	printf("\n\t%d digits", num);
	printf("\n\t%d special characters",spl_char);
	printf("\n\tIn total %d characters.\n",total);
	}