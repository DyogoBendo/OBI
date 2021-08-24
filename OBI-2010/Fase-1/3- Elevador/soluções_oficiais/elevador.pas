program elevador;

var
   N: integer;
   C: integer;
   S: integer;
   E: integer;
   i: integer;
   cur: integer;
   ans: boolean;
begin
   readln(N, C);
   cur := 0;
   ans := false;
   for i := 1 to N do begin
      readln(S, E);
      cur := cur - S + E;
      if cur > C then begin
         ans := true;
      end;
   end;
   if ans = true then begin
      writeln('S');
   end else begin
      writeln('N');
   end;
end.
