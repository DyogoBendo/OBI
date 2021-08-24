{ Solucao para o problema "Caçadores de Mito" da OBI 2009
   por: Igor Ribeiro de Assis }

program mito;

const
   MAXX	= 510;
   MAXY	= 510;

var
   N, x, y, i, j, caiu : longint;
   { para marcar onde cairam os raios }
   mapa		       : array[1..MAXX] of array[1..MAXY] of longint;

begin

   readln(N);
   for i := 1 to MAXX do
      for j := 1 to MAXY do
	 mapa[i][j] := 0;

   caiu := 0;
   for i := 1 to N do begin
      readln(x, y);
      { se mapa[x][y] >= 1, entao já caiu um raio nesse quadrante }
      if mapa[x][y] > 0 then
	 caiu := 1;
      mapa[x][y] += 1;
   end;

   writeln(caiu);
         
end.