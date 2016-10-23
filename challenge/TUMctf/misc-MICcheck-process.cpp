#include <bits/stdc++.h>

using namespace std;
char s[20000];
int main(){
	freopen("flag.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	while(gets(s) != NULL && strlen(s) != 0){
		for(int i = 0; i < strlen(s); ++i){
			if(s[i] >= '0' && s[i] <= '9' && s[i+1] >= '0' && s[i+1] <='9'){
				printf("%c", (s[i]-'0')*16+s[i+1]-'0');
				i++;
			}
		}
		puts("");
	}
	return 0;
}
