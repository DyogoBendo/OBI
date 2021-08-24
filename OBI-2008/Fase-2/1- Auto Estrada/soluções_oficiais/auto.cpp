#include <stdio.h>

int main (void) {
  int size; 
  char track;
  int walls = 0;
  scanf ("%d", &size);
  for(int i = 0; i < size; i++) {
    scanf(" %c", &track);
    switch(track) {
    case 'C':
    case 'P':
      walls += 2; break;
    case 'A':
      walls += 1; break;
    case 'D':
      break;
    }
  }
  printf ("%d\n", walls);
  return (0);
}
