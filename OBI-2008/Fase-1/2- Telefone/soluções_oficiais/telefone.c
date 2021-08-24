#include <stdio.h>
#include <ctype.h>

int main() {
	char ch;
	int dig;
	while ((ch = getc(stdin)) != EOF) {
		if (isalpha(ch)) {
			if (ch >= 'Q') {
				ch--;
			}
			dig = (ch - 'A') / 3;
			putc('2' + dig, stdout);
		} else {
			putc(ch, stdout);
		}
	}
	return 0;
}
