#include <stdio.h>
#include<stdlib.h>

#include<math.h>

float diff (float t, float y) 
{
return y-t*t+1;
}
float y(float t)
{
return (t+1)*(t+1)-0.5*exp(t);
}

int main ()
{
float h=0.2;
float t[11]={0};
for (int i=0; i<11; i++) {t[i]=i*0.2;}
float w[11]={0.5};
for (int i=0; i<10; i++) {w[i+1]=w[i]+h*diff(t[i],w[i]);}
printf("Q15.ntttwtterror_boundstabs_errorsn");
for (int i=0; i<11; i++)
{
printf("%ft%ft%ft%fn",t[i],w[i],0.1*(0.5*exp(2)-2)*(exp(t[i])-1),y(t[i])-w[i]); 
}
printf("t=mesh points, w=approximate (numerical) solution."); 
return 0;
} 