%{
int wcount=0,lcount=0;
%}

word  [^\n\t]+
eol   \n


%%
{word}   {wcount++;}
{eol}    {lcount++;}
%%



main()
	{
	FILE *fp;
	fp=fopen("a.txt","r");
	yyin=fp;
	/*printf("\n %d no if digis are there",dcount);
	printf("\n %d no of Character are there",ccount);*/
	yylex();
	/*printf("\n %d no if digis are there",dcount);
	printf("\n %d no of Character are there",ccount);*/
	printf("\nTotal Word=%d",wcount);
	printf("\nTotal Lines=%d",lcount);
	printf("\n");
	}
