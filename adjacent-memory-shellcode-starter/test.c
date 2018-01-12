#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
     char copy_buff[263];
     char exploit_string[1024];
     char vuln_array[256];

     if(argc <= 2){
          printf("Usage: %s <name> <message>.\n", argv[0]);
          exit(0);}

     strncpy(vuln_array, argv[1], sizeof(vuln_array));
     strncpy(exploit_string, argv[2], sizeof(exploit_string));
     
     sprintf(copy_buff, "MSG: %s\n", vuln_array);
     printf("%s\n", copy_buff);
     return(0);
}
