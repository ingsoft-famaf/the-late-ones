#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct _split_t {
    char *begin;
    char *end;
    char *buffer;
    bool new_line;
};

typedef struct _split_t *split_t;

char* strcopy(const char *src, unsigned int start,unsigned int end)
{
    unsigned int i,j = start,k = end, n;
    char* dest = NULL;
    dest = calloc(strlen(src)-1,sizeof(char));
        n = 0;
        for (i = j; i < k; i++) {
            dest[n] = src[i];
            n++;
           
}
   return dest;
}

split_t sig_split(char *word_input) {

    split_t result = NULL;
    char * word = NULL;
    unsigned int i = 0, j = 0, k = 0;

    result = calloc(1,sizeof(split_t));


    result->new_line = false; //inicializamos los saltos de linea

    if(word_input!=NULL){
        if((char)word_input[strlen(word_input)-1]=='\n'){
            result->new_line = true;
            if(strlen(word_input)!=1){
                word = calloc(strlen(word_input)-1,sizeof(char));
                word = strcopy(word_input,0,(strlen(word_input)-1));
            } else {    word = calloc(strlen(word_input),sizeof(char));
                        strcpy(word,word_input);}
        } else {
            word = calloc(strlen(word_input),sizeof(char));
            strcpy(word,word_input);
        }

        if(word!=NULL){    
            while((char)word[i]=='(' || (char)word[i]=='"' || (char)word[i]=='{' || (char)word[i]=='[' || (char)word[i]=='\''){
                    i++;
            }
                j = 1;
            while((char)word[strlen(word)-j]=='.' || (char)word[strlen(word)-j]==',' || (char)word[strlen(word)-j]==';' 
                || (char)word[strlen(word)-j]=='?' || (char)word[strlen(word)-j]=='!' || (char)word[strlen(word)-j]==':'
                || (char)word[strlen(word)-j]==')' || (char)word[strlen(word)-j]=='}' || (char)word[strlen(word)-j]==']'
                || (char)word[strlen(word)-j]=='"'){
                    j++;
            }
            j = strlen(word)-(j-1);
            k = strlen(word);

                result->begin = strcopy(word,0,i);
                result->buffer = strcopy(word,i,j);
                result->end = strcopy(word,j,k);

            }
        free(word);
        word = NULL;
        }
    return result;
    }



int main(void) {

split_t result = NULL;
char *word = "hol,";
int i=0,j=0;


i =strcspn(word,"í");
j = strlen(word);
result = sig_split(word);
printf("%s\n",word);
printf("%d\n",i);
printf("%d\n",j);
printf("p:%s\n",result->begin);
printf("s: %s\n",result->buffer);
printf("t: %s\n",result->end);

free(result);
result = NULL;

return(0);


}

