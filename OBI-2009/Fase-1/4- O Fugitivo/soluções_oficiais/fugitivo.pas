{ Solucao para o problema "O Fugitivo" da OBI 2009
   por: Igor Ribeiro de Assis }

program fugitivo;

var
   N, i, delta, afastou	: longint;
   dir			: char;
   x, y, M		: int64;
   
begin 
   readln(N, M);
   M *= M;
   x := 0; y := 0; afastou := 0;
   for i := 1 to N do begin
      readln(dir, delta);
      case dir of
	'N' : y += delta;
	'S' : y -= delta;
	'L' : x += delta;
	'O' : x -= delta;
      end;

      if x*x + y*y > M then
	 afastou := 1;
   end;
   
   writeln(afastou);
end.
