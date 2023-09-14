%{
#include <stdio.h>
%}

%%

[a-zA-Z]+   { printf("%s\n", yytext); } // Match and print words
.|\n        ; // Ignore other characters

%%

int main(int argc, char* argv[]) {
    yylex(); // Start lexical analysis
    return 0;
}
