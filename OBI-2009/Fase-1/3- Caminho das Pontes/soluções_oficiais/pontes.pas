{ Solucao para o problema "Caminho das Pontes" da OBI 2009
  por: Igor Ribeiro de Assis }

program pontes;

const
   INF	= 1000000;
   MAXN	= 1010;

var
   A	     : array[1..MAXN] of array[1..MAXN] of longint; {matriz adjacencias}
   visitado  : array[1..MAXN] of boolean;
   dis	     : array[1..MAXN] of longint;
   n, m, i,j : longint;
   s, t, b   : longint;

  function dijkstra : longint;

  var
     i, no : longint;

  begin 
     for i := 1 to n do begin
	dis[i] := INF;  	{ distancia inicial infinita }
	visitado[i] := false;
     end;
     dis[1] := 0;

     while true do begin
	no := -1;
	for i := 1 to n do
	   if (not visitado[i]) and ((no = -1) or (dis[i] < dis[no])) then
	      no := i;

	if no = -1 then
	   break;
	visitado[no] := true;

	for i := 1 to n do
	   if dis[no] + A[no][i] < dis[i] then
	      dis[i] := dis[no] + A[no][i];
     end;

     dijkstra := dis[n];
  end;

begin

   readln(n, m);
   n += 2;			{ imagina as bordas como pilares }
   for i := 1 to n do
      for j := 1 to n do
	 A[i][j] := INF;	{ numero de buracos infinito }
   
   for i := 1 to m do begin
      readln(s, t, b);
      s += 1; t += 1;
      A[s][t] := b; A[t][s] := b;
   end;

   writeln(dijkstra());
   
end.