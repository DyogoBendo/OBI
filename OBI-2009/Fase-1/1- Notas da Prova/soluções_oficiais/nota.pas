{ Solucao para o problema "Notas da Prova" da OBI 2009
  por: Igor Ribeiro de Assis }

program nota;

var
   N : longint;

begin

   readln(N);
   if N >= 86 then
      writeln('A')
   else if N >= 61 then
      writeln('B')
   else if N >= 36 then
      writeln('C')
   else if N >= 1 then
      writeln('D')
   else
      writeln('E');
      
end.

