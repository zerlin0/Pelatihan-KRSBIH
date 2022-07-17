#include <iostream>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>

using namespace std;

// char* bufferToCString(char *buff, int buffSize, char *str)
// {
//     memset(str, '\0', buffSize + 1);
//     return(strncpy(str, buff, buffSize));
// }

void Mendengarkan(void)
{
    int fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd == -1) 
    {
        perror("Socket Creation Has Failed : ");
        exit(-1);
    }
    struct sockaddr_in addr;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_family = AF_INET;
    // addr.sin_port = htons(80);
    addr.sin_port = 9979;
    if (bind(fd, (const struct sockaddr *) &addr, sizeof(addr)) == -1)
    {
        perror("Listening Failed on the Socket : ");
        exit(-1);
    }
    struct sockaddr_in cliaddr;
    socklen_t cliaddr_len = sizeof(cliaddr);
    char buffer[1024];
    while(1)
    {
        recvfrom(fd, buffer, 2048,0,(struct sockaddr *) &cliaddr, &cliaddr_len);
        char str[2048];
        // char* kondisi;
        // kondisi = bufferToCString(buffer, sizeof(buffer), str);
        cout<<buffer<<endl;
        if(strncmp(buffer, "berhenti", 8) == 0)
        {
            cout<<"robot berhenti"<<endl;
        }
    }
}

int main()
{
    Mendengarkan();
    return 0;
}