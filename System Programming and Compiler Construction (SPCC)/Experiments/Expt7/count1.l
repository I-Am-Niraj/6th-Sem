/*This program is going to count total number of lines and total number of
Characters present in input file*/
%{

int num_lines = 0, num_chars = 0;
%}

%%

\n      ++num_lines;
.       ++num_chars;


%%

main(void)
	{
	yyin= fopen("a.txt","r");  
	yylex();
	//printf(" This File contains ...");
	printf("\n\t%d lines", num_lines);
	//printf("\n\t%d words",words);
	//printf("\n\t%d small letters", s_letters);
	//printf("\n\t%d capital letters",c_letters);
	//printf("\n\t%d digits", num);
	printf("\n\t%d Total characters\n",num_chars);
	//printf("\n\tIn total %d characters.\n",total);
	}


