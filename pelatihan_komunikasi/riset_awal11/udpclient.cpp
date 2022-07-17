#include <iostream>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

using namespace std;
int main()
{
    int fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd == -1) 
    {
        perror("Socket Creation Has Failed : ");
        exit(-1);
    }

    struct sockaddr_in s_addr;
    s_addr.sin_family = AF_INET;
    // s_addr.sin_port = htons(80);
    s_addr.sin_port = 9979;
    inet_aton("127.0.0.1", &s_addr.sin_addr);
    socklen_t s_addr_len = sizeof(s_addr);
    char buffer[100];
    
    while(1)
    {
        cout<<"Type The  Message : ";
        fgets(buffer, 100, stdin);
        sendto(fd, buffer, strlen(buffer),0,(const struct sockaddr*) &s_addr, s_addr_len);
        int n = recvfrom(fd, buffer, 100,0,(struct sockaddr*) &s_addr, &s_addr_len);
        cout<<"\nClient : "<<buffer<<endl;
    }
    return 0;
}