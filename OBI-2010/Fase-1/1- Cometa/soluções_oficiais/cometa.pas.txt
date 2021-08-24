program cometa;

var
   N: integer;
   time: integer;
   ans: integer;
begin
   readln(N);
   time := N - 1986;
   ans := 2062 + time - (time mod 76);
   writeln(ans);
end.
