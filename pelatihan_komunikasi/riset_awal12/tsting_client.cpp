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

//IP Robot1 sampai 3
char* IPRobot1 = "192.168.245.168";
int PortRobot1 = 9979;
char* IPRobot2 = "192.168.245.168";
int PortRobot2 = 9979;
char* IPRobot3 = "192.168.245.168";
int PortRobot3 = 9979;

//command
char maju[100] = "maju";
char mundur[100] = "mundur";
char tendang[100] = "tendang";

//untuk robot 1
void mengirimKeRobot1(char* buffer, char* IPP, int Portnya)
{   
    int fd;
    fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd == -1) 
    {
        perror("Socket Creation Has Failed : ");
        exit(-1);
    }
    struct sockaddr_in s_addr;
    s_addr.sin_family = AF_INET;
    // s_addr.sin_port = htons(80);
    s_addr.sin_port = Portnya;
    inet_aton(IPP, &s_addr.sin_addr);
    socklen_t s_addr_len = sizeof(s_addr);
    sendto(fd, buffer, strlen(buffer),0,(const struct sockaddr*) &s_addr, s_addr_len);
}

int main()
{   
    mengirimKeRobot1(maju, IPRobot1, PortRobot1);
}