program quadrado;

const
	MAXN = 1000;
	
var
	mtx : array [1..MAXN] of array [1..MAXN] of longint;
	N, S: longint;
	
procedure initialize;
var i, j, k : longint;
begin
	k := 0;
	for i := 1 to N do
		for j := 1 to N do begin
			mtx[i][j] := k;
			k := k + 1
		end
end;

function current_s : longint;
var i, acc : longint;
begin
	acc := 0;
	for i := 1 to N do
		acc := acc + mtx[i][i];
	current_s := acc;
end;

procedure compensate;
var curs, j : longint;
begin
	curs := current_s;
	if S < curs then
		for j := 1 to N do
			mtx[1][j] := mtx[1][j] - (curs - S)
	else if S > curs then
		for j := 1 to N do
			mtx[N][j] := mtx[N][j] + (S - curs)
end;

procedure print_matrix;
var i, j : longint;
begin
	for i := 1 to N do begin
		for j := 1 to N do
			write(mtx[i][j], ' ');
		writeln
	end
end;

begin
	readln(N, S);
	initialize;
	compensate;
	print_matrix
end.
