%{
int dcount=0,ccount=0;
%}

%%
0|1|2|3|4|5|6|7|8|9     {dcount++; printf("\n\n%s is a Digit",yytext); }
[a-zA-Z]                {ccount++; printf("\n\n%s is a character",yytext);}
.    {}

%%



main()
	{
	FILE *fp;
	fp=fopen("a.txt","r");
	yyin=fp;
	/*printf("\n %d no if digis are there",dcount);
	printf("\n %d no of Character are there",ccount);*/
	yylex();
	printf("\n %d no if digis are there",dcount);
	printf("\n %d no of Character are there",ccount);
	}